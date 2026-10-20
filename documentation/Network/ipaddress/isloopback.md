# isLoopback

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean indicating whether this address is a loopback address for the local device.

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
var isLoopback: Bool { get }
```

## See Also

### Inspecting Address Properties
- [var rawValue: Data](./rawvalue.md)
  The raw data of an IP address.
- [var interface: NWInterface?](./interface.md)
  The interface associated with this address, such as the IPv6 scoped interface.
- [var isLinkLocal: Bool](./islinklocal.md)
  A Boolean indicating whether this address is in a link-local range.
- [var isMulticast: Bool](./ismulticast.md)
  A Boolean indicating whether this address is a multicast address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/ipaddress/isloopback)*