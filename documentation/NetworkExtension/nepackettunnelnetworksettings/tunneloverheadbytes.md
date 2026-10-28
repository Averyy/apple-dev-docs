# tunnelOverheadBytes

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The number of bytes added to each tunneled packet for storing tunneling protocol headers.

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
var tunnelOverheadBytes: NSNumber? { get set }
```

```objc
@property (copy, nullable) NSNumber * tunnelOverheadBytes;
```

## Discussion

The value of this property is subtracted from the Maximum Transmission Unit (MTU) of the tunnel’s underlying physical network interface to compute the MTU of the TUN interface.

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
- [var mtu: NSNumber?](./mtu.md)
  The size of the maximum trasnmission unit, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/tunneloverheadbytes)*