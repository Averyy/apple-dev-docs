# Discovering game controllers

**Framework**: Game Controller

Implement connection and input handling to provide seamless physical controller support for players.

#### Overview

Physical game controllers enhance the gaming experience by providing tactile feedback and precise input control. When using a controller, you might make it the exclusive source of input data to your game or it may be only one of many sources of input data. You choose how to best use the controller in your game.

The Game Controller framework provides standardized APIs for connection monitoring and input handling. The framework supports Made-for-iPhone (MFi) controllers, console controllers, and platform-specific input devices like the Siri Remote for Apple TV. Use this framework to:

- Monitor controller connection and disconnection events.
- Configure controller properties like player indices and LED indicators.
- Handle input from different controller profiles consistently.
- Support accessibility features and assistive technologies.

For more information on designing game experiences using controllers, see Human Interface Guidelines > Inputs > [`Game Controls`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/game-controls).

#### Discover Wireless Controllers

A wireless controller isn’t visible to the device until it’s explicitly paired with the device. Before retrieving controller connection states and handling input, players need to pair their controller with the device your game supports. To pair a device:

1. On iOS, iPadOS, tvOS, or visionOS, open the Settings app; on macOS, open System Settings.
2. On tvOS, choose Remotes and Devices; otherwise, choose Bluetooth.
3. Activate pairing mode on the controller to connect. Check your controller’s documentation on how to do this.
4. Select the controller when it appears under “Other Devices”

If the device was previously paired, select it from the “My Devices” list to connect.

When connecting a controller to an iOS or iPadOS device using a USB cable, the controller connects automatically. When connecting a controller to a Mac, the person receives a system prompt that they need to approve before the controller is available to your game.

#### Monitor for Controller Connections

After your app launches, the system automatically creates a list of connected [`controllers()`](gccontroller/controllers().md) that you use to inspect whether a controller is already in a connected state. When a person connects or disconnects a controller, the system can broadcast these connection events to your app. Use [`NotificationCenter`](https://developer.apple.com/documentation/foundation/notificationcenter) to observe for connection notifications:

```swift
import GameController

class GameControllerManager {

    // The connected controllers, if any.
    private(set) var connectedControllers: [GCController] = []

    // Notification observers for controller connection events.
    private var observers: [NSObjectProtocol] = []
    
    func startMonitoring() {
        // Get the controllers that were connected before the app launched.
        connectedControllers = GCController.controllers()
        
        // The framework posts a connection notification when a controller connects.
        let connectObserver = NotificationCenter.default.addObserver(
            forName: .GCControllerDidConnect,
            object: nil,
            queue: .main
        ) { [weak self] notification in
            guard let controller = notification.object as? GCController else { return }
            self?.handleControllerConnected(controller)
        }
        
        // The framework posts a disconnection notification when a controller disconnects.
        let disconnectObserver = NotificationCenter.default.addObserver(
            forName: .GCControllerDidDisconnect,
            object: nil,
            queue: .main
        ) { [weak self] notification in
            guard let controller = notification.object as? GCController else { return }
            self?.handleControllerDisconnected(controller)
        }
        
        observers = [connectObserver, disconnectObserver]
        
        connectedControllers.forEach { 
            // Update the UI to reflect the change in connection status 
            // for each controller. 
        }
    }
    
    func stopMonitoring() {
        observers.forEach { NotificationCenter.default.removeObserver($0) }
        observers.removeAll()
    }
    
    private func handleControllerConnected(_ controller: GCController) {
        connectedControllers.append(controller)
    }
    
    private func handleControllerDisconnected(_ controller: GCController) {
        connectedControllers.removeAll { $0 == controller }
    }
}
```

The [`controllers()`](gccontroller/controllers().md) method returns an empty array when there are no connected controllers. Observe both [`GCControllerDidConnectNotification`](gccontrollerdidconnectnotification.md) and [`GCControllerDidDisconnectNotification`](gccontrollerdiddisconnectnotification.md) and update your user experience according to the controller a person wants to use. When the connection status changes, the [`object`](https://developer.apple.com/documentation/foundation/nsnotification/object) property contains the [`GCController`](gccontroller.md) object.

Because the number of game controllers may vary, consider modifying your game’s input handling based on the number and types of connected controllers. The [`Game Controller`](GameController.md) framework supports controllers you attach an iPhone into and standalone extended controller designs. When multiple controllers are in a connected state, prioritize making an attached controller the default controller.

```swift
private func updateInputConfiguration(controllers: [GCController]) {
    // Before updating the input configuration, ignore touch controller 
    // instances by filtering them out.
    let physicalControllers = controllers.filter { controller in
        return controller.productCategory != "Touch Controller"
    }

    // Update the input configuration based on the number of physical
    // controllers that are in a connected state.
    switch physicalControllers.count {
    case 0:
        // There are no physical controllers in a connected state.
        // Enable touch controls by using the Touch Controller framework if your
        // game uses the Metal framework; otherwise, use `GCVirtualController`.
        break
    case 1:
        // There is one physical controller connected, always use it.
        break
    default:
        // The device detects multiple controllers. Prioritize selecting an 
        // attached controller by default; otherwise, assign the controllers 
        // based on the order they connected to the device.
        if let attachedController = controllers.first(where: { $0.isAttachedToDevice }) {
            // Make a controller you attach to the device the primary controller.
        } else {
            // Assign physical controllers based on the connection order.
        }
    }
}
```

#### Associate a Game Controller with a Player

Use the [`GCController`](gccontroller.md) to perform common controller-related tasks, like:

- Detect and set an index number for each controller that connects to the device.
- Read the controller object’s profile properties to obtain controller input.
- Access the controller’s battery life, light settings, and haptics information.
- Identify whether the controller directly attaches to the device.

A player index associates a controller with a specific player. Set [`playerIndex`](gccontroller/playerindex.md) to associate each player with the controller they’re using. For example, in a two-player game where both players are using controllers, you set one controller to [`GCControllerPlayerIndex.index1`](gccontrollerplayerindex/index1.md) and the other to [`GCControllerPlayerIndex.index2`](gccontrollerplayerindex/index2.md). If the controller supports it, setting the player index causes a matching LED on the controller to light up.

When a controller is no longer in use by a player, use `GCControllerPlayerIndex/indexunset`.

```swift
private func assignControllersInOrder() {
    for (index, controller) in connectedControllers.enumerated() {
        let playerIndex: GCControllerPlayerIndex
        switch index {
        case 0: playerIndex = .index1
        case 1: playerIndex = .index2
        case 2: playerIndex = .index3
        case 3: playerIndex = .index4
        default: playerIndex = .indexUnset
        }
        
        controller.playerIndex = playerIndex
        
        // Configure input handling for the controller.
    }
}

private func unassignController(_ controller: GCController) {
    controller.playerIndex = .indexUnset
    removeInputHandlers(for: controller)
}
```

#### Choose the Profile Representation and Handle Input

When you add controller support, you choose which controller profiles to support and then set up input handling to read the appropriate elements on those profiles to receive input data. A profile provides a guarantee that the controls you expect to find on a specific controller exist. A game controller can support multiple profiles, ensuring all controls each profile defines are present on the physical controller.

You configure input handling based on the controller’s available input profile that you specify with [`GCSupportedGameControllers`](https://developer.apple.com/documentation/bundleresources/information-property-list/gcsupportedgamecontrollers). The framework supports the following game controller profiles:

- **`Extended`**: Represents an Xbox-like, or console controller-like controller — supporting all controls found on an Xbox controller.
- **`DualShock`**: Represents a PlayStation DUALSHOCK 4 controller for PS4.
- **`DualSense`**: Represents a PlayStation DualSense controller for PS5.
- **`Xbox`**: Represents an Xbox controller.
- **`Micro`**: Represents a directional pad with motion, like the 1st generation Siri Remote.
- **`Directional`**: Represents a directional pad without motion or rotation, like the second generation Siri Remote.
- **`Spatial`**: Represents a spatial gamepad, like a PlayStation VR2 Sense Controller.

The framework maps the actual physical control data to the elements of the profile you choose. When you choose a gamepad representation, you assign a callback for the associated input you want from the profile, like [`GCExtendedGamepad`](gcextendedgamepad.md):

```swift
private func setupExtendedGamepadHandlers(_ gamepad: GCExtendedGamepad, playerIndex: Int) {
    // Configure directional input.
    gamepad.leftThumbstick.valueChangedHandler = { [weak self] _, xValue, yValue in
        // Handle player movement input.
    }
    
    gamepad.dpad.valueChangedHandler = { [weak self] _, xValue, yValue in
        // Handle directional input.
    }
    
    // Configure the action buttons.
    gamepad.buttonA.pressedChangedHandler = { [weak self] _, value, pressed in
        // Handle the primary action button being pressed.
    }
    
    gamepad.buttonB.pressedChangedHandler = { [weak self] _, value, pressed in
        // Handle the secondary action button being pressed.
    }
    
    // Configure shoulder buttons.
    gamepad.leftShoulder.valueChangedHandler = { [weak self] _, value, pressed in
        // Handle the left shoulder button.
    }
    
    gamepad.rightShoulder.valueChangedHandler = { [weak self] _, value, pressed in
        // Handle the right shoulder button.
    }
    
    // Configure the menu button.
    gamepad.buttonMenu.pressedChangedHandler = { [weak self] _, _, pressed in
        // Handle the menu action.
    }
}
```

For more information about handling controller input events, see [`Handling input events`](handling-input-events.md).

#### Use Gamepads on Visionos

Apple Vision Pro supports all of the same game controllers that iOS, iPadOS, tvOS, and macOS support. By default, the system converts gamepad input and a person’s gaze into a pinch events and sends them to the view a person is gazing at. A gaze and gamepad button press results in a [`UIKit`](https://developer.apple.com/documentation/uikit) event or a [`SwiftUI`](https://developer.apple.com/documentation/swiftui) gesture.

A game can override the default behavior and instead receive gamepad input events through the [`Game Controller`](GameController.md) framework when a person is gazing at a game’s content view. To receive game controller events in [`UIKit`](https://developer.apple.com/documentation/uikit), add an instance of [`GCEventInteraction`](gceventinteraction.md) to the view that hosts your game’s [`CAMetalLayer`](https://developer.apple.com/documentation/quartzcore/cametallayer). If you use [`SwiftUI`](https://developer.apple.com/documentation/swiftui), add the [`handlesGameControllerEvents(matching:)`](https://developer.apple.com/documentation/swiftui/view/handlesgamecontrollerevents(matching:)) modifier:

```swift
import SwiftUI
import RealityKit
import GameController

struct VisionContentView: View {
    var body: some View {
        RealityView { content in
            // Your view code.
        }
        // Indicate that your `RealityView` handles game controller input.
        .handlesGameControllerEvents(matching: .gamepad)
    }
}
```

For more information about spatial game controllers, see [`Discovering and tracking spatial game controllers and styli`](discovering-and-tracking-spatial-game-controllers-and-styli.md).

## See Also

- [Game Controller updates](../updates/gamecontroller.md)
  Learn about important changes to Game Controller.
- [Handling input events](handling-input-events.md)
  Receive controller input using either polling or callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/discovering-game-controllers)*