# NWPath.Status

**Framework**: Network  
**Kind**: enum

Status values indicating whether a path can be used by connections.

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
enum Status
```

## Topics

### Status Values
- [NWPath.Status.unsatisfied](nwpath/status-swift.enum/unsatisfied.md)
  The path is not available for use.
- [NWPath.Status.satisfied](nwpath/status-swift.enum/satisfied.md)
  The path is available to establish connections and send data.
- [NWPath.Status.requiresConnection](nwpath/status-swift.enum/requiresconnection.md)
  The path is not currently available, but establishing a new connection may activate the path.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let status: NWPath.Status](nwpath/status-swift.property.md)
  A status indicating whether a path can be used by connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwpath/status-swift.enum)*