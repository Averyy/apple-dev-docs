# NSMutableOrderedSet

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSMutableOrderedSet : NSOrderedSet
```

#### Overview

[`NSMutableOrderedSet`](./nsmutableorderedset.md) objects are not like C arrays. That is, even though you may specify a size when you create a mutable ordered set, the specified size is regarded as a “hint”; the actual size of the set is still 0. This means that you cannot insert an object at an index greater than the current count of an set. For example, if a set contains two objects, its size is 2, so you can add objects at indices 0, 1, or 2. Index 3 is illegal and out of bounds; if you try to add an object at index 3 (when the size of the array is 2), `NSMutableOrderedSet` raises an exception.

## Topics

### Creating a Mutable Ordered Set
- [init(capacity: Int)](./nsmutableorderedset/init%28capacity%29.md)
  Returns an initialized mutable ordered set with a given initial capacity.
- [init()](./nsmutableorderedset/init%28%29.md)
  Initializes a newly allocated mutable ordered set.
- [+ orderedSetWithCapacity:](./nsmutableorderedset/orderedsetwithcapacity_.md)
  Creates and returns an mutable ordered set with a given initial capacity.
### Adding, Removing, and Reordering Entries
- [func add(Any)](./nsmutableorderedset/add%28_%29.md)
  Appends a given object to the end of the mutable ordered set, if it is not already a member.
- [func add(UnsafePointer<AnyObject>?, count: Int)](./nsmutableorderedset/add%28_,count%29.md)
  Appends the given number of objects from a given C array to the end of the mutable ordered set.
- [func addObjects(from: [Any])](./nsmutableorderedset/addobjects%28from%29.md)
  Appends to the end of the mutable ordered set each object contained in a given array that is not already a member.
- [func insert(Any, at: Int)](./nsmutableorderedset/insert%28_,at%29-7qg51.md)
  Inserts the given object at the specified index of the mutable ordered set, if it is not already a member.
- [func insert([Any], at: IndexSet)](./nsmutableorderedset/insert%28_,at%29-3ncnm.md)
  Inserts the objects in the array at the specified indexes.
- [func remove(Any)](./nsmutableorderedset/remove%28_%29.md)
  Removes a given object from the mutable ordered set.
- [func removeObject(at: Int)](./nsmutableorderedset/removeobject%28at%29.md)
  Removes a the object at the specified index from the mutable ordered set.
- [func removeObjects(at: IndexSet)](./nsmutableorderedset/removeobjects%28at%29.md)
  Removes the objects at the specified indexes from the mutable ordered set.
- [func removeObjects(in: [Any])](./nsmutableorderedset/removeobjects%28in%29-8h2kh.md)
  Removes the objects in the array from the mutable ordered set.
- [func removeObjects(in: NSRange)](./nsmutableorderedset/removeobjects%28in%29-9jkis.md)
  Removes from the mutable ordered set each of the objects within a given range.
- [func removeAllObjects()](./nsmutableorderedset/removeallobjects%28%29.md)
  Removes all the objects from the mutable ordered set.
- [func replaceObject(at: Int, with: Any)](./nsmutableorderedset/replaceobject%28at,with%29.md)
  Replaces the object at the specified index with the new object.
- [func replaceObjects(at: IndexSet, with: [Any])](./nsmutableorderedset/replaceobjects%28at,with%29.md)
  Replaces the objects at the specified indexes with the new objects.
- [func replaceObjects(in: NSRange, with: UnsafePointer<AnyObject>?, count: Int)](./nsmutableorderedset/replaceobjects%28in,with,count%29.md)
  Replaces the objects in the receiving mutable ordered set at the range with the specified number of objects from a given C array.
- [func setObject(Any, at: Int)](./nsmutableorderedset/setobject%28_,at%29.md)
  Appends or replaces the object at the specified index.
- [func moveObjects(at: IndexSet, to: Int)](./nsmutableorderedset/moveobjects%28at,to%29.md)
  Moves the objects at the specified indexes to the new location.
- [func exchangeObject(at: Int, withObjectAt: Int)](./nsmutableorderedset/exchangeobject%28at,withobjectat%29.md)
  Exchanges the object at the specified index with the object at the other index.
- [func filter(using: NSPredicate)](./nsmutableorderedset/filter%28using%29.md)
  Evaluates a given predicate against the mutable ordered set’s content and leaves only objects that match.
- [- setObject:atIndexedSubscript:](./nsmutableorderedset/setobject_atindexedsubscript_.md)
  Replaces the given object at the specified index of the mutable ordered set.
### Sorting Entries
- [func sort(using: [NSSortDescriptor])](./nsmutableorderedset/sort%28using%29.md)
  Sorts the receiving ordered set using a given array of sort descriptors.
- [func sort(comparator: (Any, Any) -> ComparisonResult)](./nsmutableorderedset/sort%28comparator%29.md)
  Sorts the mutable ordered set using the comparison method specified by the comparator block.
- [func sort(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult)](./nsmutableorderedset/sort%28options,usingcomparator%29.md)
  Sorts the mutable ordered set using the specified options and the comparison method specified by a given comparator block.
- [func sortRange(NSRange, options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult)](./nsmutableorderedset/sortrange%28_,options,usingcomparator%29.md)
  Sorts the specified range of the mutable ordered set using the specified options and the comparison method specified by a given comparator block.
### Combining and Recombining Entries
- [func intersect(NSOrderedSet)](./nsmutableorderedset/intersect%28_%29.md)
  Removes from the receiving ordered set each object that isn’t a member of another ordered set.
- [func intersectSet(Set<AnyHashable>)](./nsmutableorderedset/intersectset%28_%29.md)
  Removes from the receiving ordered set each object that isn’t a member of another set.
- [func minus(NSOrderedSet)](./nsmutableorderedset/minus%28_%29.md)
  Removes each object in another given ordered set from the receiving mutable ordered set, if present.
- [func minusSet(Set<AnyHashable>)](./nsmutableorderedset/minusset%28_%29.md)
  Removes each object in another given set from the receiving mutable ordered set, if present.
- [func union(NSOrderedSet)](./nsmutableorderedset/union%28_%29.md)
  Adds each object in another given ordered set to the receiving mutable ordered set, if not present.
- [func unionSet(Set<AnyHashable>)](./nsmutableorderedset/unionset%28_%29.md)
  Adds each object in another given set to the receiving mutable ordered set, if not present.
### Initializers
- [init?(coder: NSCoder)](./nsmutableorderedset/init%28coder%29.md)
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](./nsmutableorderedset/init%28objects,count%29.md)
### Instance Methods
- [- applyDifference:](./nsmutableorderedset/applydifference_.md)

## Relationships

### Inherits From
- [NSOrderedSet](./nsorderedset.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSFastEnumeration](./nsfastenumeration.md)
- [NSMutableCopying](./nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Specialized Sets
- [class NSCountedSet](./nscountedset.md)
  A mutable, unordered collection of distinct objects that may appear more than once in the collection.
- [class NSOrderedSet](./nsorderedset.md)
  A static, ordered collection of unique objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableorderedset)*