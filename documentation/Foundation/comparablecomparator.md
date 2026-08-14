# ComparableComparator

**Framework**: Foundation  
**Kind**: struct

A comparator that compares types according to their conformance to the comparable protocol.

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
struct ComparableComparator<Compared> where Compared : Comparable
```

#### Overview

The comparator uses the relevant type’s [`Comparable`](https://developer.apple.com/documentation/swift/comparable) implementation to compare instances.

## Topics

### Using a Comparator
- [func compare(Compared, Compared) -> ComparisonResult](comparablecomparator/compare(_:_:).md)
  Provides the relative ordering of two elements.
### Inspecting a Comparator
- [var order: SortOrder](comparablecomparator/order.md)
  The sort order that the comparator uses to compare.
### Initializers
- [init(order: SortOrder)](comparablecomparator/init(order:).md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SortComparator](sortcomparator.md)

## See Also

- [class NSSortDescriptor](nssortdescriptor.md)
  An immutable description of how to order a collection of objects according to a property common to all the objects.
- [enum ComparisonResult](comparisonresult.md)
  Constants that indicate sort order.
- [struct SortDescriptor](sortdescriptor.md)
  A serializable description of how to sort numerics and strings.
- [protocol SortComparator](sortcomparator.md)
  A comparison algorithm for a specified type.
- [struct KeyPathComparator](keypathcomparator.md)
  A comparator that uses another sort comparator to provide the comparison of values at a key path.
- [enum SortOrder](sortorder.md)
  The orderings that you can perform sorts with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/comparablecomparator)*