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
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Building peer-to-peer apps](../WiFiAware/Building-peer-to-peer-apps.md)
  Communicate with nearby devices over a secure, high-throughput, low-latency connection by using Wi-Fi Aware.
- [struct DevicePairingView](devicepairingview.md)
  A control that allows a user to become discoverable and advertise to local devices.
- [struct DDDevicePairingAccess](dddevicepairingaccess.md)
  Specifies the access level requested for device discovery.
- [NSApplicationServices](../BundleResources/Information-Property-List/NSApplicationServices.md)
  A list of service providers and the devices that they support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/dddevicepairingviewcontroller)*