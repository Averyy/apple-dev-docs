# ARSession.CollaborationData.Priority

**Framework**: ARKit  
**Kind**: enum

Options that help you choose the appropriate network protocol or settings for a given data instance.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum Priority
```

#### Discussion

When you send [`ARSession.CollaborationData`](arsession/collaborationdata.md) over the network by using a protocol that allows you to specify varying reliability, this property provides you with a hint about which reliability setting to use for a given collaboration data instance. Depending on its priority, you may also choose to send a given collaboration data instance using different protocols.

## Topics

### Enumeration Cases
- [ARSession.CollaborationData.Priority.critical](arsession/collaborationdata/priority-swift.enum/critical.md)
  A priority that indicates that collaboration depends on this data.
- [ARSession.CollaborationData.Priority.optional](arsession/collaborationdata/priority-swift.enum/optional.md)
  A priority that indicates that collaboration can continue without this data.
### Initializers
- [init?(rawValue: Int)](arsession/collaborationdata/priority-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var priority: ARSession.CollaborationData.Priority](arsession/collaborationdata/priority-swift.property.md)
  A property that gives you a hint about how to send a given data instance over the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/collaborationdata/priority-swift.enum)*