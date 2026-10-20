# CWChannel

**Framework**: Core WLAN  
**Kind**: class  
**Role**: Class

Encapsulates an IEEE 802.11 channel.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class CWChannel
```

```objc
@interface CWChannel : NSObject
```

## Topics

### Comparing channels
- [func isEqual(to: CWChannel) -> Bool](./cwchannel/isequal%28to%29.md)
  Determine CWChannel object equality.
### Instance Properties
- [var channelBand: CWChannelBand](./cwchannel/channelband.md)
  The channel band.
- [var channelNumber: Int](./cwchannel/channelnumber.md)
  The channel number.
- [var channelWidth: CWChannelWidth](./cwchannel/channelwidth.md)
  The channel width.
### Initializers
- [init?(coder: NSCoder)](./cwchannel/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Classes
- [class CWConfiguration](./cwconfiguration.md)
  Encapsulates an immutable configuration for an AirPort WLAN interface.
- [class CWInterface](./cwinterface.md)
  Encapsulates an IEEE 802.11 interface.
- [class CWMutableConfiguration](./cwmutableconfiguration.md)
  Encapsulates a mutable configuration for an AirPort WLAN interface.
- [class CWMutableNetworkProfile](./cwmutablenetworkprofile.md)
  Encapsulates a mutable network profile entry.
- [class CWNetwork](./cwnetwork.md)
  Encapsulates an IEEE 802.11 network, providing read-only accessors to various properties of the network.
- [class CWNetworkProfile](./cwnetworkprofile.md)
  Encapsulates an immutable network profile entry.
- [class CWWiFiClient](./cwwificlient.md)
  A wrapper around the entire Wi-Fi subsystem that you use to access interfaces and set up event notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwchannel)*