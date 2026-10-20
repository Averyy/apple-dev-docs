# DDDevicePairingViewController

**Framework**: DeviceDiscoveryUI  
**Kind**: class  
**Role**: Class

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
- [init(listenerProvider: any ListenerProvider, access: DDDevicePairingAccess)](./dddevicepairingviewcontroller/init%28listenerprovider,access%29.md)
  Initializes a device-pairing view controller with the provided listener and requested access level for device discovery.
### Configuring a device-pairing view
- [func viewDidLoad()](./dddevicepairingviewcontroller/viewdidload%28%29.md)
  Configures the view after the framework loads the view controller’s view into memory.
### Determining device support
- [static func isSupported(any ListenerProvider) -> Bool](./dddevicepairingviewcontroller/issupported%28_%29.md)
  Returns a Boolean value that indicates whether the current device supports device discovery using Wi-FI Aware.

## Relationships

### Inherits From
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Publishing service availability
- [Building peer-to-peer apps](../WiFiAware/building-peer-to-peer-apps.md)
  Communicate with nearby devices over a secure, high-throughput, low-latency connection by using Wi-Fi Aware.
- [struct DevicePairingView](./devicepairingview.md)
  A control that allows a user to become discoverable and advertise to local devices.
- [struct DDDevicePairingAccess](./dddevicepairingaccess.md)
  Specifies the access level requested for device discovery.
- [NSApplicationServices](../BundleResources/information-property-list/nsapplicationservices.md)
  A list of service providers and the devices that they support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/dddevicepairingviewcontroller)*