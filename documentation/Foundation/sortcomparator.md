# SortComparator

**Framework**: Foundation  
**Kind**: protocol

A comparison algorithm for a specified type.

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
@preconcurrency
protocol SortComparator<Compared> : Hashable, Sendable
```

#### Overview

Objects that conform to [`SortComparator`](sortcomparator.md) provide a comparison algorithm and storage for the sort order to use when comparing.

## Topics

### Inspecting a Comparator
- [var order: SortOrder](sortcomparator/order.md)
  The sort order that the comparator uses to compare.
- [static var localized: String.Comparator](sortcomparator/localized.md)
  A comparator that compares a string using a localized comparison in the current locale.
- [static var localizedStandard: String.Comparator](sortcomparator/localizedstandard.md)
  A comparator that compares a string using a localized, numeric comparison in the current locale.
### Using a Comparator
- [func compare(Self.Compared, Self.Compared) -> ComparisonResult](sortcomparator/compare(_:_:).md)
  Provides the relative ordering of two elements based on the sort order of the comparator.
- [associatedtype Compared](sortcomparator/compared.md)
  A type that the sort comparator can compare.

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
### Conforming Types
- [ComparableComparator](comparablecomparator.md)
- [KeyPathComparator](keypathcomparator.md)
- [SortDescriptor](sortdescriptor.md)

## See Also

- [class NSSortDescriptor](nssortdescriptor.md)
  An immutable description of how to order a collection of objects according to a property common to all the objects.
- [enum ComparisonResult](comparisonresult.md)
  Constants that indicate sort order.
- [struct SortDescriptor](sortdescriptor.md)
  A serializable description of how to sort numerics and strings.
- [struct ComparableComparator](comparablecomparator.md)
  A comparator that compares types according to their conformance to the comparable protocol.
- [struct KeyPathComparator](keypathcomparator.md)
  A comparator that uses another sort comparator to provide the comparison of values at a key path.
- [enum SortOrder](sortorder.md)
  The orderings that you can perform sorts with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/sortcomparator)*