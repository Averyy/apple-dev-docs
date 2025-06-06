# members

**Framework**: Network  
**Kind**: property

The set of IP multicast group addresses that the connection group joins.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var members: [NWEndpoint] { get }
```

## See Also

- [let sourceFilter: NWEndpoint?](nwmulticastgroup/sourcefilter.md)
  An optional address endpoint you provide to filter received multicast packets.
- [let isUnicastDisabled: Bool](nwmulticastgroup/isunicastdisabled.md)
  A Boolean that specifies whether the connection group rejects unicast traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwmulticastgroup/members)*