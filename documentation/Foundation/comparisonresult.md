# ComparisonResult

**Framework**: Foundation  
**Kind**: enum

Constants that indicate sort order.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
enum ComparisonResult
```

#### Overview

These constants are used to indicate how items in a request are ordered, from the first one given in a method invocation or function call to the last (that is, left to right in code).

## Topics

### Constants
- [ComparisonResult.orderedAscending](comparisonresult/orderedascending.md)
  The left operand is smaller than the right operand.
- [ComparisonResult.orderedSame](comparisonresult/orderedsame.md)
  The two operands are equal.
- [ComparisonResult.orderedDescending](comparisonresult/ordereddescending.md)
  The left operand is greater than the right operand.
- [ComparisonResult.orderedAscending](comparisonresult/orderedascending.md)
  The left operand is smaller than the right operand.
- [ComparisonResult.orderedSame](comparisonresult/orderedsame.md)
  The two operands are equal.
- [ComparisonResult.orderedDescending](comparisonresult/ordereddescending.md)
  The left operand is greater than the right operand.
### Initializers
- [init?(rawValue: Int)](comparisonresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSSortDescriptor](nssortdescriptor.md)
  An immutable description of how to order a collection of objects according to a property common to all the objects.
- [struct SortDescriptor](sortdescriptor.md)
  A serializable description of how to sort numerics and strings.
- [protocol SortComparator](sortcomparator.md)
  A comparison algorithm for a specified type.
- [struct ComparableComparator](comparablecomparator.md)
  A comparator that compares types according to their conformance to the comparable protocol.
- [struct KeyPathComparator](keypathcomparator.md)
  A comparator that uses another sort comparator to provide the comparison of values at a key path.
- [enum SortOrder](sortorder.md)
  The orderings that you can perform sorts with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/comparisonresult)*