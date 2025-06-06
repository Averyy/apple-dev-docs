# NSSet

**Framework**: Foundation  
**Kind**: class

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

## Mentions

- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md)

#### Overview

The [`NSSet`](nsset.md), [`NSMutableSet`](nsmutableset.md), and [`NSCountedSet`](nscountedset.md) classes declare the programmatic interface to an unordered collection of objects.

[`NSSet`](nsset.md) declares the programmatic interface for static sets of distinct objects. You establish a static set’s entries when it’s created, and can’t modify the entries after that. [`NSMutableSet`](nsmutableset.md), on the other hand, declares a programmatic interface for dynamic sets of distinct objects. A dynamic — or mutable — set allows the addition and deletion of entries at any time, automatically allocating memory as needed.

Use sets as an alternative to arrays when the order of elements isn’t important and you need to consider performance in testing whether the set contains an object. With an array, testing for membership is slower than with sets.

[`NSSet`](nsset.md) is “toll-free bridged” with its Core Foundation counterpart, [`CFSet`](https://developer.apple.com/documentation/CoreFoundation/CFSet). See [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

In Swift, use this class instead of a [`Set`](https://developer.apple.com/documentation/Swift/Set) constant in cases where you require reference semantics.

##### Subclassing Notes

There should be little need of subclassing. If you need to customize behavior, it’s often better to consider composition instead of subclassing.

###### Methods to Override

In a subclass, you must override all of its primitive methods:

- [`count`](nsset/count.md)
- [`member(_:)`](nsset/member(_:).md)
- [`objectEnumerator()`](nsset/objectenumerator().md)

###### Alternatives to Subclassing

Before making a custom class of [`NSSet`](nsset.md), investigate [`NSHashTable`](nshashtable.md) and the corresponding Core Foundation type, [`CFSet`](https://developer.apple.com/documentation/CoreFoundation/CFSet). Because [`NSSet`](nsset.md) and [`CFSet`](https://developer.apple.com/documentation/CoreFoundation/CFSet) are “toll-free bridged,” you can substitute a [`CFSet`](https://developer.apple.com/documentation/CoreFoundation/CFSet) object for a [`NSSet`](nsset.md) object in your code (with appropriate casting). Although they’re corresponding types, [`CFSet`](https://developer.apple.com/documentation/CoreFoundation/CFSet) and [`NSSet`](nsset.md) don’t have identical interfaces or implementations, and you can sometimes do things with [`CFSet`](https://developer.apple.com/documentation/CoreFoundation/CFSet) that you can’t easily do with [`NSSet`](nsset.md).

If the behavior you want to add supplements that of the existing class, you could write a category on [`NSSet`](nsset.md). Keep in mind, however, that this category affects all instances of [`NSSet`](nsset.md) that you use, and this might have unintended consequences. Alternatively, you could use composition to achieve the desired behavior.

## Topics

### Creating a Set
- [convenience init(object: Any)](nsset/init(object:).md)
  Creates and returns a set that contains a single given object.
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](nsset/init(objects:count:)-65ni4.md)
  Creates and returns a set containing a specified number of objects from a given C array of objects.
- [func adding(Any) -> Set<AnyHashable>](nsset/adding(_:).md)
  Returns a new set formed by adding a given object to the receiving set.
- [func addingObjects(from: Set<AnyHashable>) -> Set<AnyHashable>](nsset/addingobjects(from:)-2i31h.md)
  Returns a new set formed by adding the objects in a given set to the receiving set.
- [func addingObjects(from: [Any]) -> Set<AnyHashable>](nsset/addingobjects(from:)-544m9.md)
  Returns a new set formed by adding the objects in a given array to the receiving set.
### Initializing a Set
- [convenience init(array: [Any])](nsset/init(array:).md)
  Initializes a newly allocated set with the objects that are contained in a given array.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](nsset/init(objects:count:)-7kift.md)
  Initializes a newly allocated set with a specified number of objects from a given C array of objects.
- [convenience init(set: Set<AnyHashable>)](nsset/init(set:)-1xovx.md)
  Initializes a newly allocated set and adds to it objects from another given set.
- [convenience init(set: Set<AnyHashable>, copyItems: Bool)](nsset/init(set:copyitems:).md)
  Initializes a newly allocated set and adds to it members of another given set.
- [init()](nsset/init.md)
  Initializes a newly allocated set.
### Counting Entries
- [var count: Int](nsset/count.md)
  The number of members in the set.
### Accessing Set Members
- [var allObjects: [Any]](nsset/allobjects.md)
  An array containing the set’s members, or an empty array if the set has no members.
- [func anyObject() -> Any?](nsset/anyobject.md)
  Returns one of the objects in the set, or `nil` if the set contains no objects.
- [func contains(Any) -> Bool](nsset/contains(_:).md)
  Returns a Boolean value that indicates whether a given object is present in the set.
- [func filtered(using: NSPredicate) -> Set<AnyHashable>](nsset/filtered(using:).md)
  Evaluates a given predicate against each object in the receiving set and returns a new set containing the objects for which the predicate returns true.
- [func member(Any) -> Any?](nsset/member(_:).md)
  Determines whether a given object is present in the set, and returns that object if it is.
- [func objectEnumerator() -> NSEnumerator](nsset/objectenumerator.md)
  Returns an enumerator object that lets you access each object in the set.
- [func enumerateObjects((Any, UnsafeMutablePointer<ObjCBool>) -> Void)](nsset/enumerateobjects(_:).md)
  Executes a given block using each object in the set.
- [func enumerateObjects(options: NSEnumerationOptions, using: (Any, UnsafeMutablePointer<ObjCBool>) -> Void)](nsset/enumerateobjects(options:using:).md)
  Executes a given block using each object in the set, using the specified enumeration options.
- [func objects(passingTest: (Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>](nsset/objects(passingtest:).md)
  Returns a set of objects that pass a test in a given block.
- [func objects(options: NSEnumerationOptions, passingTest: (Any, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Set<AnyHashable>](nsset/objects(options:passingtest:).md)
  Returns a set of objects that pass a test in a given block, using the specified enumeration options.
### Comparing Sets
- [func isSubset(of: Set<AnyHashable>) -> Bool](nsset/issubset(of:).md)
  Returns a Boolean value that indicates whether every object in the receiving set is also present in another given set.
- [func intersects(Set<AnyHashable>) -> Bool](nsset/intersects(_:).md)
  Returns a Boolean value that indicates whether at least one object in the receiving set is also present in another given set.
- [func isEqual(to: Set<AnyHashable>) -> Bool](nsset/isequal(to:).md)
  Compares the receiving set to another set.
- [func value(forKey: String) -> Any](nsset/value(forkey:).md)
  Return a set containing the results of invoking `valueForKey:` on each of the receiving set’s members.
- [func setValue(Any?, forKey: String)](nsset/setvalue(_:forkey:).md)
  Invokes `setValue:forKey:` on each of the set’s members.
### Creating a Sorted Array
- [func sortedArray(using: [NSSortDescriptor]) -> [Any]](nsset/sortedarray(using:).md)
  Returns an array of the set’s content sorted as specified by a given array of sort descriptors.
### Key-Value Observing
- [func addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](nsset/addobserver(_:forkeypath:options:context:).md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](nsset/removeobserver(_:forkeypath:context:).md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String)](nsset/removeobserver(_:forkeypath:).md)
  Raises an exception.
### Describing a Set
- [var description: String](nsset/description.md)
  A string that represents the contents of the set, formatted as a property list.
- [func description(withLocale: Any?) -> String](nsset/description(withlocale:).md)
  Returns a string that represents the contents of the set, formatted as a property list.
### Initializers
- [init?(coder: NSCoder)](nsset/init(coder:).md)
- [convenience init(collectionViewIndexPath: IndexPath)](nsset/init(collectionviewindexpath:).md)
- [convenience init(collectionViewIndexPaths: [IndexPath])](nsset/init(collectionviewindexpaths:).md)
- [convenience init(objects: Any...)](nsset/init(objects:).md)
- [convenience init(set: NSSet)](nsset/init(set:)-7a7ws.md)
### Instance Methods
- [func enumerateIndexPaths(options: NSEnumerationOptions, using: (IndexPath, UnsafeMutablePointer<ObjCBool>) -> Void)](nsset/enumerateindexpaths(options:using:).md)
### Default Implementations
- [Sequence Implementations](nsset/sequence-implementations.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSMutableSet](nsmutableset.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
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
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsset)*