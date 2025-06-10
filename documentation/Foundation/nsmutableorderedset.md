# NSMutableOrderedSet

**Framework**: Foundation  
**Kind**: class

A dynamic, ordered collection of unique objects.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSMutableOrderedSet
```

#### Overview

[`NSMutableOrderedSet`](nsmutableorderedset.md) objects are not like C arrays. That is, even though you may specify a size when you create a mutable ordered set, the specified size is regarded as a “hint”; the actual size of the set is still 0. This means that you cannot insert an object at an index greater than the current count of an set. For example, if a set contains two objects, its size is 2, so you can add objects at indices 0, 1, or 2. Index 3 is illegal and out of bounds; if you try to add an object at index 3 (when the size of the array is 2), `NSMutableOrderedSet` raises an exception.

## Topics

### Creating a Mutable Ordered Set
- [init(capacity: Int)](nsmutableorderedset/init(capacity:).md)
  Returns an initialized mutable ordered set with a given initial capacity.
- [init()](nsmutableorderedset/init.md)
  Initializes a newly allocated mutable ordered set.
### Adding, Removing, and Reordering Entries
- [func add(Any)](nsmutableorderedset/add(_:).md)
  Appends a given object to the end of the mutable ordered set, if it is not already a member.
- [func add(UnsafePointer<AnyObject>?, count: Int)](nsmutableorderedset/add(_:count:).md)
  Appends the given number of objects from a given C array to the end of the mutable ordered set.
- [func addObjects(from: [Any])](nsmutableorderedset/addobjects(from:).md)
  Appends to the end of the mutable ordered set each object contained in a given array that is not already a member.
- [func insert(Any, at: Int)](nsmutableorderedset/insert(_:at:)-7qg51.md)
  Inserts the given object at the specified index of the mutable ordered set, if it is not already a member.
- [func insert([Any], at: IndexSet)](nsmutableorderedset/insert(_:at:)-3ncnm.md)
  Inserts the objects in the array at the specified indexes.
- [func remove(Any)](nsmutableorderedset/remove(_:).md)
  Removes a given object from the mutable ordered set.
- [func removeObject(at: Int)](nsmutableorderedset/removeobject(at:).md)
  Removes a the object at the specified index from the mutable ordered set.
- [func removeObjects(at: IndexSet)](nsmutableorderedset/removeobjects(at:).md)
  Removes the objects at the specified indexes from the mutable ordered set.
- [func removeObjects(in: [Any])](nsmutableorderedset/removeobjects(in:)-8h2kh.md)
  Removes the objects in the array from the mutable ordered set.
- [func removeObjects(in: NSRange)](nsmutableorderedset/removeobjects(in:)-9jkis.md)
  Removes from the mutable ordered set each of the objects within a given range.
- [func removeAllObjects()](nsmutableorderedset/removeallobjects.md)
  Removes all the objects from the mutable ordered set.
- [func replaceObject(at: Int, with: Any)](nsmutableorderedset/replaceobject(at:with:).md)
  Replaces the object at the specified index with the new object.
- [func replaceObjects(at: IndexSet, with: [Any])](nsmutableorderedset/replaceobjects(at:with:).md)
  Replaces the objects at the specified indexes with the new objects.
- [func replaceObjects(in: NSRange, with: UnsafePointer<AnyObject>?, count: Int)](nsmutableorderedset/replaceobjects(in:with:count:).md)
  Replaces the objects in the receiving mutable ordered set at the range with the specified number of objects from a given C array.
- [func setObject(Any, at: Int)](nsmutableorderedset/setobject(_:at:).md)
  Appends or replaces the object at the specified index.
- [func moveObjects(at: IndexSet, to: Int)](nsmutableorderedset/moveobjects(at:to:).md)
  Moves the objects at the specified indexes to the new location.
- [func exchangeObject(at: Int, withObjectAt: Int)](nsmutableorderedset/exchangeobject(at:withobjectat:).md)
  Exchanges the object at the specified index with the object at the other index.
- [func filter(using: NSPredicate)](nsmutableorderedset/filter(using:).md)
  Evaluates a given predicate against the mutable ordered set’s content and leaves only objects that match.
### Sorting Entries
- [func sort(using: [NSSortDescriptor])](nsmutableorderedset/sort(using:).md)
  Sorts the receiving ordered set using a given array of sort descriptors.
- [func sort(comparator: (Any, Any) -> ComparisonResult)](nsmutableorderedset/sort(comparator:).md)
  Sorts the mutable ordered set using the comparison method specified by the comparator block.
- [func sort(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult)](nsmutableorderedset/sort(options:usingcomparator:).md)
  Sorts the mutable ordered set using the specified options and the comparison method specified by a given comparator block.
- [func sortRange(NSRange, options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult)](nsmutableorderedset/sortrange(_:options:usingcomparator:).md)
  Sorts the specified range of the mutable ordered set using the specified options and the comparison method specified by a given comparator block.
### Combining and Recombining Entries
- [func intersect(NSOrderedSet)](nsmutableorderedset/intersect(_:).md)
  Removes from the receiving ordered set each object that isn’t a member of another ordered set.
- [func intersectSet(Set<AnyHashable>)](nsmutableorderedset/intersectset(_:).md)
  Removes from the receiving ordered set each object that isn’t a member of another set.
- [func minus(NSOrderedSet)](nsmutableorderedset/minus(_:).md)
  Removes each object in another given ordered set from the receiving mutable ordered set, if present.
- [func minusSet(Set<AnyHashable>)](nsmutableorderedset/minusset(_:).md)
  Removes each object in another given set from the receiving mutable ordered set, if present.
- [func union(NSOrderedSet)](nsmutableorderedset/union(_:).md)
  Adds each object in another given ordered set to the receiving mutable ordered set, if not present.
- [func unionSet(Set<AnyHashable>)](nsmutableorderedset/unionset(_:).md)
  Adds each object in another given set to the receiving mutable ordered set, if not present.
### Initializers
- [init?(coder: NSCoder)](nsmutableorderedset/init(coder:).md)

## Relationships

### Inherits From
- [NSOrderedSet](nsorderedset.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSFastEnumeration](nsfastenumeration.md)
- [NSMutableCopying](nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [class NSCountedSet](nscountedset.md)
  A mutable, unordered collection of distinct objects that may appear more than once in the collection.
- [class NSOrderedSet](nsorderedset.md)
  A static, ordered collection of unique objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableorderedset)*