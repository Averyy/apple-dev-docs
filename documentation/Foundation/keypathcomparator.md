# KeyPathComparator

**Framework**: Foundation  
**Kind**: struct

A comparator that uses another sort comparator to provide the comparison of values at a key path.

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
struct KeyPathComparator<Compared>
```

## Topics

### Inspecting Key Path Comparators
- [let keyPath: any PartialKeyPath<Compared> & Sendable](keypathcomparator/keypath.md)
  The key path that the comparator uses to compare properties.
### Initializers
- [init<Value, Comparator>(any KeyPath<Compared, Value> & Sendable, comparator: Comparator)](keypathcomparator/init(_:comparator:)-8b13q.md)
- [init<Value, Comparator>(any KeyPath<Compared, Value?> & Sendable, comparator: Comparator)](keypathcomparator/init(_:comparator:)-284rt.md)
- [init<Value, Comparator>(any KeyPath<Compared, Value> & Sendable, comparator: Comparator, order: SortOrder)](keypathcomparator/init(_:comparator:order:)-749jk.md)
- [init<Value, Comparator>(any KeyPath<Compared, Value?> & Sendable, comparator: Comparator, order: SortOrder)](keypathcomparator/init(_:comparator:order:)-3gjxd.md)
- [init<Value>(any KeyPath<Compared, Value> & Sendable, order: SortOrder)](keypathcomparator/init(_:order:)-6r8gw.md)
- [init<Value>(any KeyPath<Compared, Value?> & Sendable, order: SortOrder)](keypathcomparator/init(_:order:)-4hyoi.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
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
- [struct ComparableComparator](comparablecomparator.md)
  A comparator that compares types according to their conformance to the comparable protocol.
- [enum SortOrder](sortorder.md)
  The orderings that you can perform sorts with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/keypathcomparator)*