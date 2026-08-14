# DDDevicePairingViewController

**Framework**: DeviceDiscoveryUI  
**Kind**: class

A UIKit view that displays and manages the device discovery and pairing process.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
@objc @preconcurrency final class DDDevicePairingViewController
```

## Topics

### Creating a device-pairing view controller
- [init(listenerProvider: any ListenerProvider, access: DDDevicePairingAccess)](dddevicepairingviewcontroller/init(listenerprovider:access:).md)
  Initializes a device-pairing view controller with the provided listener and requested access level for device discovery.
### Configuring a device-pairing view
- [func viewDidLoad()](dddevicepairingviewcontroller/viewdidload.md)
  Configures the view after the framework loads the view controller’s view into memory.
### Determining device support
- [static func isSupported(any ListenerProvider) -> Bool](dddevicepairingviewcontroller/issupported(_:).md)
  Returns a Boolean value that indicates whether the current device supports device discovery using Wi-FI Aware.

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

- [Building peer-to-peer apps](../wifiaware/building-peer-to-peer-apps.md)
  Communicate with nearby devices over a secure, high-throughput, low-latency connection by using Wi-Fi Aware.
- [struct DevicePairingView](devicepairingview.md)
  A control that allows a user to become discoverable and advertise to local devices.
- [struct DDDevicePairingAccess](dddevicepairingaccess.md)
  Specifies the access level requested for device discovery.
- [NSApplicationServices](../bundleresources/information-property-list/nsapplicationservices.md)
  A list of service providers and the devices that they support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/dddevicepairingviewcontroller)*