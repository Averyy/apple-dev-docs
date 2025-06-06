# Connecting a tvOS app to other devices over the local network

**Framework**: DeviceDiscoveryUI

Display a view in your tvOS app that lists available iOS, iPadOS, and watchOS devices that the user can connect to over their local network.

#### Overview

The DeviceDiscoveryUI framework provides a view that shows all the available iOS, iPadOS, and watchOS devices on your local network. Present this view in your tvOS app, to let the user select a device. The framework then creates an encrypted connection between your tvOS app and the selected device. This lets user’s enhance the tvOS experience. For example, they could control a tvOS game from their iPad, or send heart rate data from their watchOS app to the tvOS workout app. It also lets your app connect to devices across the local network, without giving your app access to the entire network.

To create a network connection, start by defining which devices your app can connect with. Your app defines one or more application services. Each application service represents a different type of connection that can support a different subset of devices. Next display the list of available devices in a device picker view in your tvOS app using one of the application services. If the user selects a device, the device picker view returns an [`NWEndpoint`](https://developer.apple.com/documentation/NetworkExtension/NWEndpoint) for the selected device. Use this endpoint to create a connection, and then use the connection to communicate with the device.

In your iOS, iPadOS, or watchOS app, declare that your app listens for DeviceDiscoveryUI connections. Then, as soon as your app launches, create an [`NWListener`](https://developer.apple.com/documentation/Network/NWListener). When the tvOS app connects to the listener, the listener returns a connection that your app can use to communicate with the tvOS app.

You use DeviceDiscoveryUI to present the device picker view, and then use the [`Network`](https://developer.apple.com/documentation/Network) framework to create the listeners, create the connections, and send and receive messages.

##### Define the Supported Devices in Tvos

Start by defining the application service identifiers that your apps use to establish their connections. Use the [`NSApplicationServices`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSApplicationServices) key to define the application services for your app. You provide a service identifier, a usage description, and a list of supported devices for each service. You can define more than one application service for your apps. Each service has it’s own identifier, and can connect to a different subset of devices.

Declare the application services in your app target’s Info tab, or in its `Info.plist` file.

```plist
<key>NSApplicationServices</key>
<dict>
    <key>Browses</key>
    <array>
        <dict>
            <key>NSApplicationServiceIdentifier</key>
            <string>MyApp-Controller</string>
            <key>NSApplicationServiceUsageDescription</key>
            <string>You can control this app using an iOS device.</string>
            <key>NSApplicationServicePlatformSupport</key>
            <array>
                <string>iOS</string>
                <string>iPadOS</string>
            </array>
        </dict>
        <dict>
            <key>NSApplicationServiceIdentifier</key>
            <string>MyApp-Workout</string>
            <key>NSApplicationServiceUsageDescription</key>
            <string>Connects to a watchOS app to read heart-rate and active calories burned from a workout session.</string>
            <key>NSApplicationServicePlatformSupport</key>
            <array>
                <string>watchOS</string>
            </array>
        </dict>
    </array>
</dict>
```

You can use the human-readable key names in Xcode’s property list editor.

![A screenshot showing the Application Services settings in Xcode’s property list editor.](https://docs-assets.developer.apple.com/published/cf9a6dfa9f67b5902bd2e32c0021352c/media-4030765%402x.png)

##### Display the List of Available Devices

Next, create and display the device picker view in your tvOS app. The following code creates and displays a [`DevicePicker`](devicepicker.md) view using SwiftUI.

```swift
@State var showDevicePicker = false

var body: some View {
    VStack {
        Text(deviceName)
        Button("Connect") {
            showDevicePicker = true
        }
    }
    .padding()
    .fullScreenCover(isPresented: $showDevicePicker) {
        // Display the device picker view.
        DevicePicker(
            .applicationService(name: "MyAppService")) { endpoint in
                myDeviceManager.connectTo(endpoint: endpoint)
            } label: {
                Text("Connect to a local device.")
            } parameters: {
                // This example uses the default application services parameters;
                // however, you can add an NWProtocolFramer to provide application-level
                // messaging.
                .applicationService
            }
    }
}
```

Display the [`DevicePicker`](devicepicker.md) as a modal view that covers the full screen. This example uses [`fullScreenCover(isPresented:onDismiss:content:)`](https://developer.apple.com/documentation/SwiftUI/View/fullScreenCover(isPresented:onDismiss:content:)) to display the device picker view when the user clicks the Connect button.

To create the device picker view, pass an [`NWBrowser.Descriptor`](https://developer.apple.com/documentation/Network/NWBrowser/Descriptor-swift.enum) that you created using the `NWBrowser.Descriptor.applicationService(name:options:)` method. Use the identifier that you defined in your app’s `Info.plist` file for the descriptor’s name.

Next, provide an `onSelect` closure that takes a single [`NWEndpoint`](https://developer.apple.com/documentation/NetworkExtension/NWEndpoint) value. The system calls this closure after the user selects a device to connect to. Use the closure to set up a connection to the endpoint.

Then include a [`Label`](https://developer.apple.com/documentation/SwiftUI/Label) view to represent your app in the device picker view, and pass the default application service parameters using the [`applicationService`](https://developer.apple.com/documentation/Network/NWParameters/applicationService) property. The default parameters create an encrypted, optimized connection between two devices on your local network. You can also add protocols defined with an [`NWProtocolFramer`](https://developer.apple.com/documentation/Network/NWProtocolFramer) to these defaults to support application-level messaging in your app.

When presented, the view shows all the supported devices on the local network.

These devices:

- Are logged into your local network.
- Are logged into the iCloud account (or another account in the iCloud family) of the default user on Apple TV.
- Match the device type specified in your `NSApplicationServicePlatformSupport` key.

If the user selects a device, the system calls your `onSelect` closure. If they dismiss the device picker view, control returns to the view that displayed the device picker view.

> **Note**:  While you can display the [`DevicePicker`](devicepicker.md) view in Simulator, it won’t show any devices on the local network. To test connections, run your code on a test device instead.

 While you can display the [`DevicePicker`](devicepicker.md) view in Simulator, it won’t show any devices on the local network. To test connections, run your code on a test device instead.

If you’re using [`UIKit`](https://developer.apple.com/documentation/UIKit), use a [`DDDevicePickerViewController`](dddevicepickerviewcontroller.md) to present the device picker view.

```swift
// This example uses the default application services parameters;
// however, you can add a NWProtocolFramer to provide application-level
// messaging.
let parameters = NWParameters.applicationService

// Create the view controller for the endpoint picker.
let myEndpointPickerHandler =
NWEndpointPickerViewController(browseDescriptor: NWBrowser.Descriptor.applicationService(name: "MyAppService"),
                               parameters: parameters)

// Show the network device picker as a full-screen, modal view.
myEndpointPickerHandler.modalTransitionStyle = .coverVertical
show(myEndpointPickerHandler, sender: nil)

let endpoint: NWEndpoint
do {
    endpoint = try await myEndpointPickerHandler.endpoint
} catch {
    // The user canceled the endpoint picker view.
    return
}

// Use the endpoint here.
myDeviceConnectionManager.connectTo(endpoint: endpoint)
```

This view controller works similarly to the [`DevicePicker`](devicepicker.md) view. The biggest difference is how your app receives the selected endpoint. In this sample, your app awaits a read on the controller’s `endpoint` property. This causes execution to pause at that point. When the user selects a device, the system returns an endpoint for that device, and execution continues. If the user dismisses the view, the controller throws an error.

Alternatively, you can pass a block to the [`DDDevicePickerViewController`](dddevicepickerviewcontroller.md) object’s [`setDevicePickerCompletionHandler:`](dddevicepickerviewcontroller/setdevicepickercompletionhandler:.md) method, and the system calls this block when the user selects a device from the device picker view.

##### Connect to the Provided Endpoint

As soon as the user selects a device, the system passes you an [`NWEndpoint`](https://developer.apple.com/documentation/NetworkExtension/NWEndpoint). Use this endpoint to connect to the selected device. Create an [`NWConnection`](https://developer.apple.com/documentation/Network/NWConnection), passing it both the endpoint and the parameters that you used to create the device picker view.

```swift
func connectTo(endpoint: NWEndpoint) {
    
    // This example uses the default application services parameters;
    // however, you can add a NWProtocolFramer to provide application-level
    // messaging.
    connection = NWConnection(to: endpoint,
                              using: .applicationService)
}
```

You can then use this connection to send or receive messages to the connected device.

##### Declare That Other Devices Listen for Connections

Before a device can appear in the picker view, declare that the iOS, iPadOS, or watchOS version of your app listens for connections.

Start by defining the application service in your app target’s Info tab, or in its `Info.plist` file. Make sure the `NSApplicationServiceIdentifier` matches the value specified in your tvOS app. The following example shows setting up the `MyApp-Workout` identifier on a watchOS app.

```plist
<key>NSApplicationServices</key>
<dict>
    <key>Advertises</key>
    <array>
        <dict>
            <key>NSApplicationServiceIdentifier</key>
            <string>MyApp-Workout</string>
        </dict>
    </array>
</dict>
```

You can use the human-readable key names in Xcode’s property list editor.

![A screenshot showing the application services settings in Xcode’s property list editor.](https://docs-assets.developer.apple.com/published/caa062010907505ea9fffc771d37efd9/media-4030764%402x.png)

##### Set Up the Listeners on Ios Ipados or Watchos

Next, to connect to your tvOS app, other versions of your app must set up a listener as soon as the app launches. The network picker can then connect to this listener.

To create a listener, use the [`init(applicationService:)`](https://developer.apple.com/documentation/Network/NWListener/Service-swift.struct/init(applicationService:)) initializer, and pass the same application service name that you used in your tvOS app.

```swift
// Set up the listener.
do {
    // This example uses the default application services parameters;
    // however, you can add a NWProtocolFramer to provide application-level
    // messaging.
    myListener = try NWListener(using: .applicationService)
    
    // Add your application service.
    myListener?.service = NWListener.Service(applicationService: "MyAppService")
}
catch {
    fatalError("*** An error occurred: \(error.localizedDescription) ***")
}
```

Then, create a connection handler for the listener. The system calls this closure when it creates the connection to your tvOS app. You can use this connection to read and write messages.

```swift
// Respond to new connections.
myListener?.newConnectionHandler = { connection in
    myConnectionManager.set(connection: connection)
}
```

You can also define a state change update handler to track changes to the listener’s state.

```swift
// Respond to listener state changes.
myListener?.stateUpdateHandler = { listenerState in
    switch(listenerState) {
    case .setup:
        myLogger.debug("Listener switched to the Setup state.")
    case .waiting(let error):
        myLogger.debug("Listener switched to the Waiting state. error \(error.localizedDescription)")
    case .ready:
        myLogger.debug("Listener switched to the Ready state.")
    case .failed(let error):
        myLogger.debug("Listener switched to the Failed state. error: \(error.localizedDescription)")
    case .cancelled:
        myLogger.debug("Listener switched to the Cancelled state.")
    @unknown default:
        myLogger.debug("Listener switched to an unknown state.")
    }
}
```

Finally, start the listener.

```swift
// Start the listener.
myListener?.start(queue: myBackgroundQueue)
```

Start the listener as quickly as possible after your app launches. This ensures that the listener is ready and waiting when the tvOS app attempts to connect.

## See Also

- [struct DevicePicker](devicepicker.md)
  A SwiftUI view that displays other devices on the network, and creates an encrypted connection to a copy of your app running on that device.
- [class DDDevicePickerViewController](dddevicepickerviewcontroller.md)
  A UIKit view that displays other devices on the network, and creates an encrypted connection to a copy of your app running on that device.
- [struct DevicePickerSupportedAction](devicepickersupportedaction.md)
  An environment value that indicates whether the current device supports device discovery.
- [NSApplicationServices](../BundleResources/Information-Property-List/NSApplicationServices.md)
  A list of service providers and the devices that they support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/connecting-a-tvos-app-to-other-devices-over-the-local-network)*