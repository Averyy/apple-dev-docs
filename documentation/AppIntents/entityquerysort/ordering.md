# EntityQuerySort.Ordering

**Framework**: App Intents  
**Kind**: enum

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
@frozen
enum Ordering
```

## Topics

### Operators
- [static func == (EntityQuerySort<Entity>.Ordering, EntityQuerySort<Entity>.Ordering) -> Bool](entityquerysort/ordering/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [EntityQuerySort.Ordering.ascending](entityquerysort/ordering/ascending.md)
- [EntityQuerySort.Ordering.descending](entityquerysort/ordering/descending.md)
### Instance Properties
- [var hashValue: Int](entityquerysort/ordering/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](entityquerysort/ordering/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](entityquerysort/ordering/equatable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let order: EntityQuerySort<Entity>.Ordering](entityquerysort/order.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquerysort/ordering)*