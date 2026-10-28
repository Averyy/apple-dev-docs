# ARSession.CollaborationData.Priority

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

Options that help you choose the appropriate network protocol or settings for a given data instance.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
enum Priority
```

```c
enum ARCollaborationDataPriority : NSInteger;
```

## Discussion

When you send [`ARSession.CollaborationData`](../collaborationdata.md) over the network by using a protocol that allows you to specify varying reliability, this property provides you with a hint about which reliability setting to use for a given collaboration data instance. Depending on its priority, you may also choose to send a given collaboration data instance using different protocols.

## Topics

### Enumeration Cases
- [ARSession.CollaborationData.Priority.critical](./priority-swift.enum/critical.md)
  A priority that indicates that collaboration depends on this data.
- [ARSession.CollaborationData.Priority.optional](./priority-swift.enum/optional.md)
  A priority that indicates that collaboration can continue without this data.
### Initializers
- [init?(rawValue: Int)](./priority-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Observing Priority
- [var priority: ARSession.CollaborationData.Priority](./priority-swift.property.md)
  A property that gives you a hint about how to send a given data instance over the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/collaborationdata/priority-swift.enum)*