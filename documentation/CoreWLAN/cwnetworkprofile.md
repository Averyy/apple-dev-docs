# CWNetworkProfile

**Framework**: Core WLAN  
**Kind**: class

Encapsulates an immutable network profile entry.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class CWNetworkProfile
```

## Topics

### Getting a network profile
- [init()](cwnetworkprofile/init.md)
  Creates and returns a CWNetworkProfile object.
- [init(networkProfile: CWNetworkProfile)](cwnetworkprofile/init(networkprofile:).md)
  Creates and returns a CWNetworkProfile object initialized with the given CWNetworkProfile object.
### Comparing network profiles
- [func isEqual(to: CWNetworkProfile) -> Bool](cwnetworkprofile/isequal(to:).md)
  Determine CWNetworkProfile object equality.
### Instance Properties
- [var security: CWSecurity](cwnetworkprofile/security.md)
  The security mode for the network profile.
- [var ssid: String?](cwnetworkprofile/ssid.md)
  The service set identifier (SSID) for the network profile, encoded as a string.
- [var ssidData: Data?](cwnetworkprofile/ssiddata.md)
  The service set identifier (SSID) for the network profile, returned as data.
### Initializers
- [init?(coder: NSCoder)](cwnetworkprofile/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [CWMutableNetworkProfile](cwmutablenetworkprofile.md)
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
- [class CWMutableNetworkProfile](cwmutablenetworkprofile.md)
  Encapsulates a mutable network profile entry.
- [class CWNetwork](cwnetwork.md)
  Encapsulates an IEEE 802.11 network, providing read-only accessors to various properties of the network.
- [class CWWiFiClient](cwwificlient.md)
  A wrapper around the entire Wi-Fi subsystem that you use to access interfaces and set up event notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwnetworkprofile)*