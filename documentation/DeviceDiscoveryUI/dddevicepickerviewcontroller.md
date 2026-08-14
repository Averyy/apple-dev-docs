# DDDevicePickerViewController

**Framework**: DeviceDiscoveryUI  
**Kind**: class

A UIKit view that displays other devices on the network, and creates an encrypted connection to a copy of your app running on that device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 16.0+

## Declaration

```swift
class DDDevicePickerViewController
```

## Mentions

- [Connecting a tvOS app to other devices over the local network](connecting-a-tvos-app-to-other-devices-over-the-local-network.md)

#### Overview

Always display the device picker as a full-screen, modal view. If the user selects a device, the system sets the `endpoint` property and calls the `endpointPickedHandler`.

```swift
// This example uses the default application services parameters;
// however, you can add a `NWProtocolFramer` to provide application-level messaging.
let parameters = NWParameters.applicationService

// Create the view controller for the endpoint picker.
let devicePickerController =
DDDevicePickerViewController(browseDescriptor: NWBrowser.Descriptor.applicationService(name: "MyAppService"),
                               parameters: parameters)

// Show the network device picker as a full-screen, modal view.
devicePickerController.modalTransitionStyle = .coverVertical
show(devicePickerController, sender: nil)

let endpoint: NWEndpoint
do {
    endpoint = try await devicePickerController.endpoint
} catch {
    // A person canceled the endpoint picker view.
    return
}

// Use the endpoint here.
myDeviceConnectionManager.connectTo(endpoint: endpoint)
```

## Topics

### Creating device picker view controllers
- [convenience init?(browseDescriptor: NWBrowser.Descriptor, parameters: NWParameters?)](dddevicepickerviewcontroller/init(browsedescriptor:parameters:).md)
  Creates a view controller that displays the available devices on your local network.
- [convenience init?(browseDescriptor: NWBrowser.Descriptor, parameters: NWParameters?, access: DDDevicePairingAccess)](dddevicepickerviewcontroller/init(browsedescriptor:parameters:access:).md)
  Creates a view controller with the parameters and access level you specify that displays the available devices on network.
### Determining device support
- [static func isSupported(NWBrowser.Descriptor, using: NWParameters?) -> Bool](dddevicepickerviewcontroller/issupported(_:using:).md)
  Returns a Boolean value that indicates whether the current device supports device discovery.
### Accessing the selected endpoint
- [var endpoint: NWEndpoint](dddevicepickerviewcontroller/endpoint.md)
  A network connection endpoint for the device that a person selected.

## Relationships

### Inherits From
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [struct DevicePicker](devicepicker.md)
  A SwiftUI view that displays other devices on the network, and creates an encrypted connection to a copy of your app running on that device.
- [struct DevicePickerSupportedAction](devicepickersupportedaction.md)
  An environment value that indicates whether the current device supports device discovery.
- [Connecting a tvOS app to other devices over the local network](connecting-a-tvos-app-to-other-devices-over-the-local-network.md)
  Display a view in your tvOS app that lists available iOS, iPadOS, and watchOS devices that the user can connect to over their local network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/dddevicepickerviewcontroller)*