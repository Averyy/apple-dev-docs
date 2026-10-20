# CWMutableNetworkProfile

**Framework**: Core WLAN  
**Kind**: class  
**Role**: Class

Encapsulates a mutable network profile entry.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class CWMutableNetworkProfile
```

```objc
@interface CWMutableNetworkProfile : CWNetworkProfile
```

#### Overview

Use this class to change profile properties. To commit Wi-Fi network profile changes, use [`networkProfiles`](./cwmutableconfiguration/networkprofiles.md) and [`commitConfiguration(_:authorization:)`](./cwinterface/commitconfiguration%28_,authorization%29.md).

## Topics

### Configuring Network Profiles
- [var ssidData: Data?](./cwmutablenetworkprofile/ssiddata.md)
  The service set identifier (SSID).
- [var security: CWSecurity](./cwmutablenetworkprofile/security.md)
  The security type.

## Relationships

### Inherits From
- [CWNetworkProfile](./cwnetworkprofile.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Classes
- [class CWChannel](./cwchannel.md)
  Encapsulates an IEEE 802.11 channel.
- [class CWConfiguration](./cwconfiguration.md)
  Encapsulates an immutable configuration for an AirPort WLAN interface.
- [class CWInterface](./cwinterface.md)
  Encapsulates an IEEE 802.11 interface.
- [class CWMutableConfiguration](./cwmutableconfiguration.md)
  Encapsulates a mutable configuration for an AirPort WLAN interface.
- [class CWNetwork](./cwnetwork.md)
  Encapsulates an IEEE 802.11 network, providing read-only accessors to various properties of the network.
- [class CWNetworkProfile](./cwnetworkprofile.md)
  Encapsulates an immutable network profile entry.
- [class CWWiFiClient](./cwwificlient.md)
  A wrapper around the entire Wi-Fi subsystem that you use to access interfaces and set up event notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwmutablenetworkprofile)*