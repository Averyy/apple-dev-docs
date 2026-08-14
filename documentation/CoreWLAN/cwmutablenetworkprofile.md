# CWMutableNetworkProfile

**Framework**: Core WLAN  
**Kind**: class

Encapsulates a mutable network profile entry.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class CWMutableNetworkProfile
```

#### Overview

Use this class to change profile properties. To commit Wi-Fi network profile changes, use [`networkProfiles`](cwmutableconfiguration/networkprofiles.md) and [`commitConfiguration(_:authorization:)`](cwinterface/commitconfiguration(_:authorization:).md).

## Topics

### Configuring Network Profiles
- [var ssidData: Data?](cwmutablenetworkprofile/ssiddata.md)
  The service set identifier (SSID).
- [var security: CWSecurity](cwmutablenetworkprofile/security.md)
  The security type.

## Relationships

### Inherits From
- [CWNetworkProfile](cwnetworkprofile.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSMutableCopying](../foundation/nsmutablecopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class CWChannel](cwchannel.md)
  Encapsulates an IEEE 802.11 channel.
- [class CWConfiguration](cwconfiguration.md)
  Encapsulates an immutable configuration for an AirPort WLAN interface.
- [class CWInterface](cwinterface.md)
  Encapsulates an IEEE 802.11 interface.
- [class CWMutableConfiguration](cwmutableconfiguration.md)
  Encapsulates a mutable configuration for an AirPort WLAN interface.
- [class CWNetwork](cwnetwork.md)
  Encapsulates an IEEE 802.11 network, providing read-only accessors to various properties of the network.
- [class CWNetworkProfile](cwnetworkprofile.md)
  Encapsulates an immutable network profile entry.
- [class CWWiFiClient](cwwificlient.md)
  A wrapper around the entire Wi-Fi subsystem that you use to access interfaces and set up event notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwmutablenetworkprofile)*