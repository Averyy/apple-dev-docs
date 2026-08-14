# DDDevicePairingAccess

**Framework**: DeviceDiscoveryUI  
**Kind**: struct

Specifies the access level requested for device discovery.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct DDDevicePairingAccess
```

## Topics

### Type Properties
- [static var `default`: DDDevicePairingAccess](dddevicepairingaccess/default.md)
  Use the system’s default access for the device selected by the user.
- [static var permanent: DDDevicePairingAccess](dddevicepairingaccess/permanent.md)
  Grant the app permanent access to the device selected by the user for future use.

## See Also

- [Building peer-to-peer apps](../wifiaware/building-peer-to-peer-apps.md)
  Communicate with nearby devices over a secure, high-throughput, low-latency connection by using Wi-Fi Aware.
- [struct DevicePairingView](devicepairingview.md)
  A control that allows a user to become discoverable and advertise to local devices.
- [class DDDevicePairingViewController](dddevicepairingviewcontroller.md)
  A UIKit view that displays and manages the device discovery and pairing process.
- [NSApplicationServices](../bundleresources/information-property-list/nsapplicationservices.md)
  A list of service providers and the devices that they support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/dddevicepairingaccess)*