# NSSet

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A static, unordered collection of unique objects.

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
class NSSet
```

```objc
@interface NSSet : NSObject
```

## Mentions

- [Implementing Handoff in Your App](./implementing-handoff-in-your-app.md)

## Overview

The [`NSSet`](./nsset.md), [`NSMutableSet`](./nsmutableset.md), and [`NSCountedSet`](./nscountedset.md) classes declare the programmatic interface to an unordered collection of objects.

[`NSSet`](./nsset.md) declares the programmatic interface for static sets of distinct objects. You establish a static set’s entries when it’s created, and can’t modify the entries after that. [`NSMutableSet`](./nsmutableset.md), on the other hand, declares a programmatic interface for dynamic sets of distinct objects. A dynamic — or mutable — set allows the addition and deletion of entries at any time, automatically allocating memory as needed.

Use sets as an alternative to arrays when the order of elements isn’t important and you need to consider performance in testing whether the set contains an object. With an array, testing for membership is slower than with sets.

[`NSSet`](./nsset.md) is “toll-free bridged” with its Core Foundation counterpart, [`CFSet`](../CoreFoundation/cfset.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

In Swift, use this class instead of a [`Set`](../Swift/set.md) constant in cases where you require reference semantics.

### Subclassing Notes

There should be little need of subclassing. If you need to customize behavior, it’s often better to consider composition instead of subclassing.

#### Methods to Override

In a subclass, you must override all of its primitive methods:

- [`count`](./nsset/count.md)
- [`member(_:)`](./nsset/member%28_%29.md)
- [`objectEnumerator()`](./nsset/objectenumerator%28%29.md)

#### Alternatives to Subclassing

Before making a custom class of [`NSSet`](./nsset.md), investigate [`NSHashTable`](./nshashtable.md) and the corresponding Core Foundation type, [`CFSet`](../CoreFoundation/cfset.md). Because [`NSSet`](./nsset.md) and [`CFSet`](../CoreFoundation/cfset.md) are “toll-free bridged,” you can substitute a [`CFSet`](../CoreFoundation/cfset.md) object for a [`NSSet`](./nsset.md) object in your code (with appropriate casting). Although they’re corresponding types, [`CFSet`](../CoreFoundation/cfset.md) and [`NSSet`](./nsset.md) don’t have identical interfaces or implementations, and you can sometimes do things with [`CFSet`](../CoreFoundation/cfset.md) that you can’t easily do with [`NSSet`](./nsset.md).

If the behavior you want to add supplements that of the existing class, you could write a category on [`NSSet`](./nsset.md). Keep in mind, however, that this category affects all instances of [`NSSet`](./nsset.md) that you use, and this might have unintended consequences. Alternatively, you could use composition to achieve the desired behavior.

## Topics

### Creating a Set
- [convenience init(object: Any)](./nsset/init%28object%29.md)
  Creates and returns a set that contains a single given object.
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](./nsset/init%28objects,count%29-65ni4.md)
  Creates and returns a set containing a specified number of objects from a given C array of objects.
- [func adding(Any) -> Set<AnyHashable>](./nsset/adding%28_%29.md)
  Returns a new set formed by adding a given object to the receiving set.
- [func addingObjects(from: Set<AnyHashable>) -> Set<AnyHashable>](./nsset/addingobjects%28from%29-2i31h.md)
  Returns a new set formed by adding the objects in a given set to the receiving set.
- [func addingObjects(from: [Any]) -> Set<AnyHashable>](./nsset/addingobjects%28from%29-544m9.md)
  Returns a new set formed by adding the objects in a given array to the receiving set.
- [+ set](./nsset/set.md)
  Creates and returns an empty set.
- [+ setWithArray:](./nsset/setwitharray_.md)
  Creates and returns a set containing a uniqued collection of the objects contained in a given array.
- [+ setWithObjects:](./nsset/setwithobjects_.md)
  Creates and returns a set containing the objects in a given argument list.
- [+ setWithSet:](./nsset/setwithset_.md)
  Creates and returns a set containing the objects from another set.
### Initializing a Set
- [convenience init(array: [Any])](./nsset/init%28array%29.md)
  Initializes a newly allocated set with the objects that are contained in a given array.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](./nsset/init%28objects,count%29-7kift.md)
  Initializes a newly allocated set with a specified number of objects from a given C array of objects.
- [convenience init(set: Set<AnyHashable>)](./nsset/init%28set%29-1xovx.md)
  Initializes a newly allocated set and adds to it objects from another given set.
- [convenience init(set: Set<AnyHashable>, copyItems: Bool)](./nsset/init%28set,copyitems%29.md)
  Initializes a newly allocated set and adds to it members of another given set.
- [init()](./nsset/init%28%29.md)
  Initializes a newly allocated set.
- [- initWithObjects:](./nsset/initwithobjects_.md)
  Initializes a newly allocated set with members taken from the specified list of objects.
### Counting Entries
- [var count: Int](./nsset/count.md)
  The number of members in the set.
### Accessing Set Members
- [var allObjects: [Any]](./nsset/allobjects.md)
  An array containing the set’s members, or an empty array if the set has no members.
- [func anyObject() -> Any?](./nsset/anyobject%28%29.md)
  Returns one of the objects in the set, or `nil` if the set contains no objects.
- [func contains(Any) -> Bool](./nsset/contains%28_%29.md)
  Returns a Boolean value that indicates whether a given object is present in the set.
- [func filtered(using: NSPredicate) -> Set<AnyHashable>](./nsset/filtered%28using%29.md)
  Evaluates a given predicate against each object in the receiving set and returns a new set containing the objects for which the predicate returns true.
- [func member(Any) -> Any?](./nsset/member%28_%29.md)
  Determines whether a given object is present in the set, and returns that object if it is.
- [func objectEnumerator() -> NSEnumerator](./nsset/objectenumerator%28%29.md)
  Returns an enumerator object that lets you access each object in the set.
- [func enumerateObjects((Any, UnsafeMutablePointer<ObjCBool>) -> Void)](./nsset/enumerateobjects%28_%29.md)
  Executes a given block using each object in the set.
- [func enumerateObjects(options: NSEnumerationOptions, using: (Any, UnsafeMutablePointer<ObjCBool>) -> Void)](./nsset/enumerateobjects%28options,using%29.md)
  Executes a given block using each object in the set, using the specified enumeration options.
- [func objects(passingTest: (Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>](./nsset/objects%28passingtest%29.md)
  Returns a set of objects that pass a test in a given block.
- [func objects(options: NSEnumerationOptions, passingTest: (Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>](./nsset/objects%28options,passingtest%29.md)
  Returns a set of objects that pass a test in a given block, using the specified enumeration options.
- [- makeObjectsPerformSelector:](./nsset/makeobjectsperformselector_.md)
  Sends a message specified by a given selector to each object in the set.
- [- makeObjectsPerformSelector:withObject:](./nsset/makeobjectsperformselector_withobject_.md)
  Sends a message specified by a given selector to each object in the set.
### Comparing Sets
- [func isSubset(of: Set<AnyHashable>) -> Bool](./nsset/issubset%28of%29.md)
  Returns a Boolean value that indicates whether every object in the receiving set is also present in another given set.
- [func intersects(Set<AnyHashable>) -> Bool](./nsset/intersects%28_%29.md)
  Returns a Boolean value that indicates whether at least one object in the receiving set is also present in another given set.
- [func isEqual(to: Set<AnyHashable>) -> Bool](./nsset/isequal%28to%29.md)
  Compares the receiving set to another set.
- [func value(forKey: String) -> Any](./nsset/value%28forkey%29.md)
  Return a set containing the results of invoking `valueForKey:` on each of the receiving set’s members.
- [func setValue(Any?, forKey: String)](./nsset/setvalue%28_,forkey%29.md)
  Invokes `setValue:forKey:` on each of the set’s members.
### Creating a Sorted Array
- [func sortedArray(using: [NSSortDescriptor]) -> [Any]](./nsset/sortedarray%28using%29.md)
  Returns an array of the set’s content sorted as specified by a given array of sort descriptors.
### Key-Value Observing
- [func addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](./nsset/addobserver%28_,forkeypath,options,context%29.md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](./nsset/removeobserver%28_,forkeypath,context%29.md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String)](./nsset/removeobserver%28_,forkeypath%29.md)
  Raises an exception.
### Describing a Set
- [var description: String](./nsset/description.md)
  A string that represents the contents of the set, formatted as a property list.
- [func description(withLocale: Any?) -> String](./nsset/description%28withlocale%29.md)
  Returns a string that represents the contents of the set, formatted as a property list.
### Initializers
- [init?(coder: NSCoder)](./nsset/init%28coder%29.md)
- [convenience init(collectionViewIndexPath: IndexPath)](./nsset/init%28collectionviewindexpath%29.md)
- [convenience init(collectionViewIndexPaths: [IndexPath])](./nsset/init%28collectionviewindexpaths%29.md)
- [convenience init(objects: Any...)](./nsset/init%28objects%29.md)
- [convenience init(set: NSSet)](./nsset/init%28set%29-7a7ws.md)
  Initializes a newly allocated set and adds to it objects from another given set.
### Instance Methods
- [func enumerateIndexPaths(options: NSEnumerationOptions, using: (IndexPath, UnsafeMutablePointer<ObjCBool>) -> Void)](./nsset/enumerateindexpaths%28options,using%29.md)
### Default Implementations
- [Sequence Implementations](./nsset/sequence-implementations.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NSMutableSet](./nsmutableset.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSFastEnumeration](./nsfastenumeration.md)
- [NSMutableCopying](./nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Basic Collections
- [NSArray](./nsarray.md)
  A static ordered collection of objects.
- [NSMutableArray](./nsmutablearray.md)
  A dynamic ordered collection of objects.
- [NSDictionary](./nsdictionary.md)
  A static collection of objects associated with unique keys.
- [NSMutableDictionary](./nsmutabledictionary.md)
  A dynamic collection of objects associated with unique keys.
- [NSMutableSet](./nsmutableset.md)
  A dynamic unordered collection of unique objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset)*