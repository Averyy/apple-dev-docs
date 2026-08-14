# DevicePairingView

**Framework**: DeviceDiscoveryUI  
**Kind**: struct

A control that allows a user to become discoverable and advertise to local devices.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
@preconcurrency struct DevicePairingView<Label, Fallback> where Label : View, Fallback : View
```

#### Overview

A `DevicePairingView` should be used to become discoverable to local devices from the user through a button interface.

## Topics

### Initializers
- [init(any ListenerProvider, access: DDDevicePairingAccess, label: () -> Label, fallback: () -> Fallback)](devicepairingview/init(_:access:label:fallback:).md)
  Creates a `DevicePairingView` which, when pressed, will display a local device advertiser interface.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [View](../swiftui/view.md)

## See Also

- [Building peer-to-peer apps](../wifiaware/building-peer-to-peer-apps.md)
  Communicate with nearby devices over a secure, high-throughput, low-latency connection by using Wi-Fi Aware.
- [class DDDevicePairingViewController](dddevicepairingviewcontroller.md)
  A UIKit view that displays and manages the device discovery and pairing process.
- [struct DDDevicePairingAccess](dddevicepairingaccess.md)
  Specifies the access level requested for device discovery.
- [NSApplicationServices](../bundleresources/information-property-list/nsapplicationservices.md)
  A list of service providers and the devices that they support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/devicepairingview)*