# NSCountedSet

**Framework**: Foundation  
**Kind**: class

A mutable, unordered collection of distinct objects that may appear more than once in the collection.

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
class NSCountedSet
```

#### Overview

Each distinct object inserted into an [`NSCountedSet`](nscountedset.md) object has a counter associated with it. [`NSCountedSet`](nscountedset.md) keeps track of the number of times objects are inserted and requires that objects be removed the same number of times. Thus, there is only one instance of an object in an [`NSSet`](nsset.md) object even if the object has been added to the set multiple times. The [`count`](nsset/count.md) method defined by the superclass [`NSSet`](nsset.md) has special significance; it returns the number of distinct objects, not the total number of times objects are represented in the set. The [`NSSet`](nsset.md) and [`NSMutableSet`](nsmutableset.md) classes are provided for static and dynamic sets, respectively, whose elements are distinct.

While [`NSCountedSet`](nscountedset.md) and [`CFBag`](https://developer.apple.com/documentation/CoreFoundation/CFBag) are not toll-free bridged, they provide similar functionality. For more information about `CFBag`, see the [`CFBag`](https://developer.apple.com/documentation/CoreFoundation/CFBag).

##### Subclassing Notes

Because [`NSCountedSet`](nscountedset.md) is not a class cluster, it does not have primitive methods that provide the basis for its implementation. In general, there should be little need for subclassing.

###### Methods to Override

If you subclass [`NSCountedSet`](nscountedset.md), you must override any method of which you want to change the behavior.

If you change the primitive behavior of an [`NSCountedSet`](nscountedset.md), for instance if you change how objects are stored, you must override all of the affected methods. These include:

- [`add(_:)`](nscountedset/add(_:).md)
- [`remove(_:)`](nscountedset/remove(_:).md)
- [`objectEnumerator()`](nscountedset/objectenumerator().md)
- [`count(for:)`](nscountedset/count(for:).md)

If you change the primitive behavior, you must also override the primitive methods of [`NSSet`](nsset.md) and [`NSMutableSet`](nsmutableset.md).

## Topics

### Initializing a Counted Set
- [convenience init(array: [Any])](nscountedset/init(array:).md)
  Returns a counted set object initialized with the contents of a given array.
- [convenience init(set: Set<AnyHashable>)](nscountedset/init(set:).md)
  Returns a counted set object initialized with the contents of a given set.
- [init(capacity: Int)](nscountedset/init(capacity:).md)
  Returns a counted set object initialized with enough memory to hold a given number of objects.
### Adding and Removing Entries
- [func add(Any)](nscountedset/add(_:).md)
  Adds a given object to the set.
- [func remove(Any)](nscountedset/remove(_:).md)
  Removes a given object from the set.
### Examining a Counted Set
- [func count(for: Any) -> Int](nscountedset/count(for:).md)
  Returns the count associated with a given object in the set.
- [func objectEnumerator() -> NSEnumerator](nscountedset/objectenumerator.md)
  Returns an enumerator object that lets you access each object in the set once, independent of its count.

## Relationships

### Inherits From
- [NSMutableSet](nsmutableset.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
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

- [class NSOrderedSet](nsorderedset.md)
  A static, ordered collection of unique objects.
- [class NSMutableOrderedSet](nsmutableorderedset.md)
  A dynamic, ordered collection of unique objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscountedset)*