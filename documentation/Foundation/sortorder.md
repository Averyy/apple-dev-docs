# SortOrder

**Framework**: Foundation  
**Kind**: enum

The orderings that you can perform sorts with.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@frozen
enum SortOrder
```

## Topics

### Using Sort Orders
- [SortOrder.forward](sortorder/forward.md)
  The ordering that places the first item before the second when comparing two items using an ascending order.
- [SortOrder.reverse](sortorder/reverse.md)
  The ordering that places the first item after the second when comparing two items using an ascending order.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSSortDescriptor](nssortdescriptor.md)
  An immutable description of how to order a collection of objects according to a property common to all the objects.
- [enum ComparisonResult](comparisonresult.md)
  Constants that indicate sort order.
- [struct SortDescriptor](sortdescriptor.md)
  A serializable description of how to sort numerics and strings.
- [protocol SortComparator](sortcomparator.md)
  A comparison algorithm for a specified type.
- [struct ComparableComparator](comparablecomparator.md)
  A comparator that compares types according to their conformance to the comparable protocol.
- [struct KeyPathComparator](keypathcomparator.md)
  A comparator that uses another sort comparator to provide the comparison of values at a key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/sortorder)*