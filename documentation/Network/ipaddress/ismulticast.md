# isMulticast

**Framework**: Network  
**Kind**: property  
**Required**: Yes

A Boolean indicating whether this address is a multicast address.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var isMulticast: Bool { get }
```

## See Also

- [var rawValue: Data](ipaddress/rawvalue.md)
  The raw data of an IP address.
- [var interface: NWInterface?](ipaddress/interface.md)
  The interface associated with this address, such as the IPv6 scoped interface.
- [var isLinkLocal: Bool](ipaddress/islinklocal.md)
  A Boolean indicating whether this address is in a link-local range.
- [var isLoopback: Bool](ipaddress/isloopback.md)
  A Boolean indicating whether this address is a loopback address for the local device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/ipaddress/ismulticast)*