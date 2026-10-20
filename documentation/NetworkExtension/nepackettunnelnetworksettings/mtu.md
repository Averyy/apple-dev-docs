# mtu

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The size of the maximum trasnmission unit, in bytes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var mtu: NSNumber? { get set }
```

```objc
@property (copy, nullable) NSNumber * MTU;
```

#### Discussion

The maximum transmission unit (MTU) size represents the largest number of bytes that anything can assign to the TUN interface.

> **Note**:  The system ignores the [`tunnelOverheadBytes`](./tunneloverheadbytes.md) property when this property is non-`nil`.

## See Also

### Accessing network properties
- [var ipv4Settings: NEIPv4Settings?](./ipv4settings.md)
  The tunnel IP version 4 settings.
- [class NEIPv4Settings](../neipv4settings.md)
  The IPv4 settings of an IP layer network tunnel.
- [var ipv6Settings: NEIPv6Settings?](./ipv6settings.md)
  The tunnel IP version 6 settings.
- [class NEIPv6Settings](../neipv6settings.md)
  The IPv6 settings of an IP layer network tunnel.
- [var tunnelOverheadBytes: NSNumber?](./tunneloverheadbytes.md)
  The number of bytes added to each tunneled packet for storing tunneling protocol headers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/mtu)*