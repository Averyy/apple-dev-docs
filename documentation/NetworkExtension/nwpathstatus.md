# NWPathStatus

**Framework**: Network Extension  
**Kind**: enum

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum NWPathStatus
```

## Topics

### Path Statuses
- [NWPathStatus.invalid](nwpathstatus/invalid.md)
  The path cannot be evaluated.
- [NWPathStatus.satisfied](nwpathstatus/satisfied.md)
  The path is ready to be used for network connections.
- [NWPathStatus.unsatisfied](nwpathstatus/unsatisfied.md)
  The path for network connections is not available, either due to lack of network connectivity or being prohibited by system policy.
- [NWPathStatus.satisfiable](nwpathstatus/satisfiable.md)
  The path is not currently satisfied, but may become satisfied upon a connection attempt. This can be due to a service, such as a VPN or a cellular data connection not being activated.
### Initializers
- [init?(rawValue: Int)](nwpathstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var status: NWPathStatus](nwpath/status.md)
  The evaluated status of the network path.
- [var isExpensive: Bool](nwpath/isexpensive.md)
  A Boolean that indicates whether or not the path uses an expensive interface.
- [var isConstrained: Bool](nwpath/isconstrained.md)
  A Boolean that indicates whether or not the path uses a constrained interface, such as when using low-data mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwpathstatus)*