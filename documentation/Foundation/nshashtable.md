# NSHashTable

**Framework**: Foundation  
**Kind**: class

A collection similar to a set, but with broader range of available memory semantics.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSHashTable<ObjectType> where ObjectType : AnyObject
```

## Mentions

- [NSHashTable](nshashtable.md)

#### Overview

The hash table is modeled after [`NSSet`](nsset.md) with the following differences:

- It can hold weak references to its members.
- Its members may be copied on input or may use pointer identity for equality and hashing.
- It can contain arbitrary pointers (its members are not constrained to being objects).

You can configure an [`NSHashTable`](nshashtable.md) instance to operate on arbitrary pointers and not just objects, although typically you are encouraged to use the C function API for void * pointers. The object-based API (such as [`add(_:)`](nshashtable/add(_:).md)) will not work for non-object pointers without type-casting.

Because of its options, `NSHashTable` is not a set because it can behave differently (for example, if pointer equality is specified two `isEqual:` strings will both be entered).

When configuring hash tables, note that only the options listed in [`NSHashTableOptions`](nshashtableoptions.md) guarantee that the rest of the API will work correctly—including copying, archiving, and fast enumeration. While other [`NSPointerFunctions`](nspointerfunctions.md) options are used for certain configurations, such as to hold arbitrary pointers, not all combinations of the options are valid. With some combinations the hash table may not work correctly, or may not even be initialized correctly.

##### Subclassing Notes

`NSHashTable` is not suitable for subclassing.

## Topics

### Initialization
- [init(options: NSPointerFunctions.Options, capacity: Int)](nshashtable/init(options:capacity:).md)
  Returns a hash table initialized with the given attributes.
- [init(pointerFunctions: NSPointerFunctions, capacity: Int)](nshashtable/init(pointerfunctions:capacity:).md)
  Returns a hash table initialized with the given functions and capacity.
### Convenience Constructors
- [class func weakObjects() -> NSHashTable<ObjectType>](nshashtable/weakobjects.md)
  Returns a new hash table for storing weak references to its contents.
- [init(options: NSPointerFunctions.Options)](nshashtable/init(options:).md)
  Returns a hash table with given pointer functions options.
### Accessing Content
- [var anyObject: ObjectType?](nshashtable/anyobject.md)
  One of the objects in the hash table.
- [var allObjects: [ObjectType]](nshashtable/allobjects.md)
  The hash table’s members.
- [var setRepresentation: Set<AnyHashable>](nshashtable/setrepresentation.md)
  A set that contains the hash table’s members.
- [var count: Int](nshashtable/count.md)
  The number of elements in the hash table.
- [func contains(ObjectType?) -> Bool](nshashtable/contains(_:).md)
  Returns a Boolean value that indicates whether the hash table contains a given object.
- [func member(ObjectType?) -> ObjectType?](nshashtable/member(_:).md)
  Determines whether the hash table contains a given object, and returns that object if it is present
- [func objectEnumerator() -> NSEnumerator](nshashtable/objectenumerator.md)
  Returns an enumerator object that lets you access each object in the hash table.
### Manipulating Membership
- [func add(ObjectType?)](nshashtable/add(_:).md)
  Adds a given object to the hash table.
- [func remove(ObjectType?)](nshashtable/remove(_:).md)
  Removes a given object from the hash table.
- [func removeAllObjects()](nshashtable/removeallobjects.md)
  Removes all objects from the hash table.
### Comparing Hash Tables
- [func intersect(NSHashTable<ObjectType>)](nshashtable/intersect(_:).md)
  Removes from the receiving hash table each element that isn’t a member of another given hash table.
- [func intersects(NSHashTable<ObjectType>) -> Bool](nshashtable/intersects(_:).md)
  Returns a Boolean value that indicates whether a given hash table intersects with the receiving hash table.
- [func isSubset(of: NSHashTable<ObjectType>) -> Bool](nshashtable/issubset(of:).md)
  Returns a Boolean value that indicates whether every element in the receiving hash table is also present in another given hash table.
- [func isEqual(to: NSHashTable<ObjectType>) -> Bool](nshashtable/isequal(to:).md)
  Returns a Boolean value that indicates whether a given hash table is equal to the receiving hash table.
### Set Functions
- [func minus(NSHashTable<ObjectType>)](nshashtable/minus(_:).md)
  Removes each element in another given hash table from the receiving hash table, if present.
- [func union(NSHashTable<ObjectType>)](nshashtable/union(_:).md)
  Adds each element in another given hash table to the receiving hash table, if not present.
### Accessing Pointer Functions
- [var pointerFunctions: NSPointerFunctions](nshashtable/pointerfunctions.md)
  The pointer functions for the hash table.
- [class NSPointerFunctions](nspointerfunctions.md)
  An instance of `NSPointerFunctions` defines callout functions appropriate for managing a pointer reference held somewhere else.
### Constants
- [typealias NSHashTableOptions](nshashtableoptions.md)
  Components in a bit-field to specify the behavior of elements in an [`NSHashTable`](nshashtable.md) object.
### Deprecated
- [Legacy Hash Table Implementation](legacy-hash-table-implementation.md)

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
- [NSFastEnumeration](nsfastenumeration.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)

## See Also

- [class NSPointerArray](nspointerarray.md)
  A collection similar to an array, but with a broader range of available memory semantics.
- [class NSMapTable](nsmaptable.md)
  A collection similar to a dictionary, but with a broader range of available memory semantics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtable)*