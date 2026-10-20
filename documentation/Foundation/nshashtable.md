# NSHashTable

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSHashTable : NSObject
```

#### Overview

The hash table is modeled after [`NSSet`](./nsset.md) with the following differences:

- It can hold weak references to its members.
- Its members may be copied on input or may use pointer identity for equality and hashing.
- It can contain arbitrary pointers (its members are not constrained to being objects).

You can configure an [`NSHashTable`](./nshashtable.md) instance to operate on arbitrary pointers and not just objects, although typically you are encouraged to use the C function API for void * pointers. The object-based API (such as [`add(_:)`](./nshashtable/add%28_%29.md)) will not work for non-object pointers without type-casting.

Because of its options, `NSHashTable` is not a set because it can behave differently (for example, if pointer equality is specified two `isEqual:` strings will both be entered).

When configuring hash tables, note that only the options listed in [`NSHashTableOptions`](./nshashtableoptions.md) guarantee that the rest of the API will work correctly—including copying, archiving, and fast enumeration. While other [`NSPointerFunctions`](./nspointerfunctions.md) options are used for certain configurations, such as to hold arbitrary pointers, not all combinations of the options are valid. With some combinations the hash table may not work correctly, or may not even be initialized correctly.

##### Subclassing Notes

`NSHashTable` is not suitable for subclassing.

## Topics

### Initialization
- [init(options: NSPointerFunctions.Options, capacity: Int)](./nshashtable/init%28options,capacity%29.md)
  Returns a hash table initialized with the given attributes.
- [init(pointerFunctions: NSPointerFunctions, capacity: Int)](./nshashtable/init%28pointerfunctions,capacity%29.md)
  Returns a hash table initialized with the given functions and capacity.
### Convenience Constructors
- [class func weakObjects() -> NSHashTable<ObjectType>](./nshashtable/weakobjects%28%29.md)
  Returns a new hash table for storing weak references to its contents.
- [init(options: NSPointerFunctions.Options)](./nshashtable/init%28options%29.md)
  Returns a hash table with given pointer functions options.
### Accessing Content
- [var anyObject: ObjectType?](./nshashtable/anyobject.md)
  One of the objects in the hash table.
- [var allObjects: [ObjectType]](./nshashtable/allobjects.md)
  The hash table’s members.
- [var setRepresentation: Set<AnyHashable>](./nshashtable/setrepresentation.md)
  A set that contains the hash table’s members.
- [var count: Int](./nshashtable/count.md)
  The number of elements in the hash table.
- [func contains(ObjectType?) -> Bool](./nshashtable/contains%28_%29.md)
  Returns a Boolean value that indicates whether the hash table contains a given object.
- [func member(ObjectType?) -> ObjectType?](./nshashtable/member%28_%29.md)
  Determines whether the hash table contains a given object, and returns that object if it is present
- [func objectEnumerator() -> NSEnumerator](./nshashtable/objectenumerator%28%29.md)
  Returns an enumerator object that lets you access each object in the hash table.
### Manipulating Membership
- [func add(ObjectType?)](./nshashtable/add%28_%29.md)
  Adds a given object to the hash table.
- [func remove(ObjectType?)](./nshashtable/remove%28_%29.md)
  Removes a given object from the hash table.
- [func removeAllObjects()](./nshashtable/removeallobjects%28%29.md)
  Removes all objects from the hash table.
### Comparing Hash Tables
- [func intersect(NSHashTable<ObjectType>)](./nshashtable/intersect%28_%29.md)
  Removes from the receiving hash table each element that isn’t a member of another given hash table.
- [func intersects(NSHashTable<ObjectType>) -> Bool](./nshashtable/intersects%28_%29.md)
  Returns a Boolean value that indicates whether a given hash table intersects with the receiving hash table.
- [func isSubset(of: NSHashTable<ObjectType>) -> Bool](./nshashtable/issubset%28of%29.md)
  Returns a Boolean value that indicates whether every element in the receiving hash table is also present in another given hash table.
- [func isEqual(to: NSHashTable<ObjectType>) -> Bool](./nshashtable/isequal%28to%29.md)
  Returns a Boolean value that indicates whether a given hash table is equal to the receiving hash table.
### Set Functions
- [func minus(NSHashTable<ObjectType>)](./nshashtable/minus%28_%29.md)
  Removes each element in another given hash table from the receiving hash table, if present.
- [func union(NSHashTable<ObjectType>)](./nshashtable/union%28_%29.md)
  Adds each element in another given hash table to the receiving hash table, if not present.
### Accessing Pointer Functions
- [var pointerFunctions: NSPointerFunctions](./nshashtable/pointerfunctions.md)
  The pointer functions for the hash table.
- [class NSPointerFunctions](./nspointerfunctions.md)
  An instance of `NSPointerFunctions` defines callout functions appropriate for managing a pointer reference held somewhere else.
### Constants
- [typealias NSHashTableOptions](./nshashtableoptions.md)
  Components in a bit-field to specify the behavior of elements in an [`NSHashTable`](./nshashtable.md) object.
### Deprecated
- [Legacy Hash Table Implementation](./legacy-hash-table-implementation.md)
### Initializers
- [init?(coder: NSCoder)](./nshashtable/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSFastEnumeration](./nsfastenumeration.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)

## See Also

### Pointer Collections
- [class NSPointerArray](./nspointerarray.md)
  A collection similar to an array, but with a broader range of available memory semantics.
- [class NSMapTable](./nsmaptable.md)
  A collection similar to a dictionary, but with a broader range of available memory semantics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtable)*