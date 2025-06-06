# NSSortDescriptor

**Framework**: Foundation  
**Kind**: class

An immutable description of how to order a collection of objects according to a property common to all the objects.

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
class NSSortDescriptor
```

#### Overview

You construct instances of [`NSSortDescriptor`](nssortdescriptor.md) by specifying the key path of the property to compare and the order of the sort (ascending or descending). Optionally, you can also specify a selector to use to perform the comparison, which allows you to specify other comparison selectors, such as [`localizedStandardCompare(_:)`](nsstring/localizedstandardcompare(_:).md) and [`localizedCaseInsensitiveCompare(_:)`](nsstring/localizedcaseinsensitivecompare(_:).md). Sorting raises an exception if the objects don’t respond to the sort descriptor’s comparison selector.

You can use sort descriptors for the following:

- Sorting an array (an instance of [`NSArray`](nsarray.md) or [`NSMutableArray`](nsmutablearray.md) — see [`sortedArray(using:)`](nsarray/sortedarray(using:)-82wi1.md) and [`sort(using:)`](nsmutablearray/sort(using:)-4eh07.md))
- Comparing two objects directly (see [`compare(_:to:)`](nssortdescriptor/compare(_:to:).md))
- Specifying the order of objects that return from a Core Data fetch request (see [`sortDescriptors`](https://developer.apple.com/documentation/CoreData/NSFetchRequest/sortDescriptors))

## Topics

### Creating a Sort Descriptor
- [init(key: String?, ascending: Bool)](nssortdescriptor/init(key:ascending:).md)
  Creates a sort descriptor with a specified string key path and sort order.
- [init(key: String?, ascending: Bool, selector: Selector?)](nssortdescriptor/init(key:ascending:selector:).md)
  Creates a sort descriptor with a specified string key path, ordering, and comparison selector.
- [convenience init<Root, Value>(keyPath: KeyPath<Root, Value>, ascending: Bool)](nssortdescriptor/init(keypath:ascending:).md)
  Creates a sort descriptor with a specified key path and ordering.
- [init(key: String?, ascending: Bool, comparator: Comparator)](nssortdescriptor/init(key:ascending:comparator:).md)
  Creates a sort descriptor with a specified string key path and ordering, and a comparator block.
- [convenience init<Root, Value>(keyPath: KeyPath<Root, Value>, ascending: Bool, comparator: Comparator)](nssortdescriptor/init(keypath:ascending:comparator:).md)
  Creates a sort descriptor with a specified key path and ordering, and a comparator block.
- [init?(coder: NSCoder)](nssortdescriptor/init(coder:).md)
  Creates a sort descriptor by decoding from the coder you specify.
- [convenience init<Compared>(SortDescriptor<Compared>)](nssortdescriptor/init(_:)-7qf91.md)
  Creates a sort descriptor using a sort descriptor you specify.
### Getting Information About a Sort Descriptor
- [var ascending: Bool](nssortdescriptor/ascending.md)
  A Boolean value that indicates whether the receiver specifies sorting in ascending order.
- [var key: String?](nssortdescriptor/key.md)
  The key that specifies the property to compare during sorting.
- [var keyPath: AnyKeyPath?](nssortdescriptor/keypath.md)
  The key path that specifies the property to compare during sorting.
- [var selector: Selector?](nssortdescriptor/selector.md)
  The selector for comparing objects.
- [var comparator: Comparator](nssortdescriptor/comparator.md)
  The comparator for the sort descriptor.
### Using Sort Descriptors
- [func compare(Any, to: Any) -> ComparisonResult](nssortdescriptor/compare(_:to:).md)
  Returns a comparison result value that indicates the sort order of two objects.
- [var reversedSortDescriptor: Any](nssortdescriptor/reversedsortdescriptor.md)
  Returns a sort descriptor that reverses the sort order.
- [func allowEvaluation()](nssortdescriptor/allowevaluation.md)
  Forces a securely decoded sort descriptor to allow evaluation.
### Initializers
- [convenience init<Compared>(SortDescriptor<Compared>)](nssortdescriptor/init(_:)-527yl.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)

## See Also

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
- [enum SortOrder](sortorder.md)
  The orderings that you can perform sorts with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssortdescriptor)*