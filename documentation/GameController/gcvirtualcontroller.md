# GCVirtualController

**Framework**: Game Controller  
**Kind**: class

A software emulation of a real controller that you configure specifically for your game.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
class GCVirtualController
```

## Mentions

- [Adding touch controls to games that support game controllers in iOS](adding-touch-controls-to-games-that-support-game-controllers-in-ios.md)

#### Overview

Use a virtual controller to display software controls that you can customize over your game. You create a virtual controller from a configuration where you choose the input elements to display. You can even customize the images for the elements. When you connect the controller to the device, users interact with it similarly to a real controller.

![Screenshot of a virtual controller showing left and right thumbsticks with A and B buttons on the right thumbstick.](https://docs-assets.developer.apple.com/published/028437930f5ac469e6f776b5673ad0f2/media-3830787%402x.png)

To add a virtual controller to your game, create a [`GCVirtualController.Configuration`](gcvirtualcontroller/configuration.md) object containing the elements you want to appear in the controller. Then create the virtual controller by passing the configuration to the [`init(configuration:)`](gcvirtualcontroller/init(configuration:).md) method. Use the [`connect(replyHandler:)`](gcvirtualcontroller/connect(replyhandler:).md) method to display the virtual controller on the screen.

To customize an element in the virtual controller, pass a new [`GCVirtualController.ElementConfiguration`](gcvirtualcontroller/elementconfiguration.md) object for the element to the [`updateConfiguration(forElement:configuration:)`](gcvirtualcontroller/updateconfiguration(forelement:configuration:).md) method.

You process input from a virtual controller similarly to a real controller. Use the [`controller`](gcvirtualcontroller/controller.md) property to get the underlying [`GCController`](gccontroller.md) object. You can either poll the elements of the controller object or set the element’s handlers to get callbacks when their input values change.

## Topics

### Creating virtual controllers
- [init(configuration: GCVirtualController.Configuration)](gcvirtualcontroller/init(configuration:).md)
  Creates a new virtual controller using the configuration you specify.
- [GCVirtualController.Configuration](gcvirtualcontroller/configuration.md)
  The configuration of a virtual controller.
### Customizing the elements
- [func updateConfiguration(forElement: String, configuration: (GCVirtualController.ElementConfiguration) -> GCVirtualController.ElementConfiguration)](gcvirtualcontroller/updateconfiguration(forelement:configuration:).md)
  Changes the configuration for one of the virtual controller’s input elements.
- [GCVirtualController.ElementConfiguration](gcvirtualcontroller/elementconfiguration.md)
  The properties of a virtual controller’s element that you can customize.
### Accessing the elements
- [var controller: GCController?](gcvirtualcontroller/controller.md)
  The underlying controller object that you use to access input elements.
### Connecting and displaying virtual controllers
- [func connect(replyHandler: (((any Error)?) -> Void)?)](gcvirtualcontroller/connect(replyhandler:).md)
  Connects the virtual controller to the device and displays it on the screen.
- [func disconnect()](gcvirtualcontroller/disconnect.md)
  Disconnects the virtual controller from the device and removes it from the screen.
### Presenting a custom interface
- [func setPosition(CGPoint, forDirectionPadElement: String)](gcvirtualcontroller/setposition(_:fordirectionpadelement:).md)
  Changes the value of a directional pad element in the virtual controller.
- [func setValue(CGFloat, forButtonElement: String)](gcvirtualcontroller/setvalue(_:forbuttonelement:).md)
  Changes the value of a button element in the virtual controller.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Adding touch controls to games that support game controllers in iOS](adding-touch-controls-to-games-that-support-game-controllers-in-ios.md)
  Use touch input and virtual controllers to make your game available to players without controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcvirtualcontroller)*