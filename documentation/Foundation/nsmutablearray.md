# NSMutableArray

**Framework**: Foundation  
**Kind**: class

A dynamic ordered collection of objects.

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
class NSMutableArray
```

#### Overview

You can use this type in Swift instead of an [`Array`](https://developer.apple.com/documentation/Swift/Array) variable in cases that require reference semantics.

The `NSMutableArray` class declares the programmatic interface to objects that manage a modifiable array of objects. This class adds insertion and deletion operations to the basic array-handling behavior inherited from [`NSArray`](nsarray.md).

NSMutableArray is “toll-free bridged” with its Core Foundation counterpart, [`CFMutableArray`](https://developer.apple.com/documentation/CoreFoundation/CFMutableArray). See [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information.

##### Accessing Values Using Subscripting

In addition to the provided instance methods, such as [`replaceObject(at:with:)`](nsmutablearray/replaceobject(at:with:).md), you can access `NSArray` values by their indexes using .

##### Subclassing Notes

There is typically little reason to subclass `NSMutableArray`. The class does well what it is designed to do—maintain a mutable, ordered collection of objects. But there are situations where a custom `NSArray` object might come in handy. Here are a few possibilities:

- Changing how `NSMutableArray` stores the elements of its collection. You might do this for performance reasons or for better compatibility with legacy code.
- Acquiring more information about what is happening to the collection (for example, statistics gathering).

###### Methods to Override

`NSMutableArray` defines five primitive methods:

- [`insert(_:at:)`](nsmutablearray/insert(_:at:)-5dbx5.md)
- [`removeObject(at:)`](nsmutablearray/removeobject(at:).md)
- [`add(_:)`](nsmutablearray/add(_:).md)
- [`removeLastObject()`](nsmutablearray/removelastobject().md)
- [`replaceObject(at:with:)`](nsmutablearray/replaceobject(at:with:).md)

In a subclass, you must override all these methods. You must also override the primitive methods of the [`NSArray`](nsarray.md) class.

## Topics

### Creating and Initializing a Mutable Array
- [init?(contentsOfURL: URL)](nsmutablearray/init(contentsofurl:).md)
  Creates and returns a mutable array containing the contents specified by a given URL.
- [init()](nsmutablearray/init.md)
  Initializes a newly allocated array.
- [init(capacity: Int)](nsmutablearray/init(capacity:).md)
  Returns an array, initialized with enough memory to initially hold a given number of objects.
### Adding Objects
- [func add(Any)](nsmutablearray/add(_:).md)
  Inserts a given object at the end of the array.
- [func addObjects(from: [Any])](nsmutablearray/addobjects(from:).md)
  Adds the objects contained in another given array to the end of the receiving array’s content.
- [func insert(Any, at: Int)](nsmutablearray/insert(_:at:)-5dbx5.md)
  Inserts a given object into the array’s contents at a given index.
- [func insert([Any], at: IndexSet)](nsmutablearray/insert(_:at:)-73pln.md)
  Inserts the objects in the provided array into the receiving array at the specified indexes.
### Removing Objects
- [func removeAllObjects()](nsmutablearray/removeallobjects.md)
  Empties the array of all its elements.
- [func removeLastObject()](nsmutablearray/removelastobject.md)
  Removes the object with the highest-valued index in the array
- [func remove(Any)](nsmutablearray/remove(_:).md)
  Removes all occurrences in the array of a given object.
- [func remove(Any, in: NSRange)](nsmutablearray/remove(_:in:).md)
  Removes all occurrences within a specified range in the array of a given object.
- [func removeObject(at: Int)](nsmutablearray/removeobject(at:).md)
  Removes the object at `index` .
- [func removeObjects(at: IndexSet)](nsmutablearray/removeobjects(at:).md)
  Removes the objects at the specified indexes from the array.
- [func removeObject(identicalTo: Any)](nsmutablearray/removeobject(identicalto:).md)
  Removes all occurrences of a given object in the array.
- [func removeObject(identicalTo: Any, in: NSRange)](nsmutablearray/removeobject(identicalto:in:).md)
  Removes all occurrences of `anObject` within the specified range in the array.
- [func removeObjects(fromIndices: UnsafeMutablePointer<Int>, numIndices: Int)](nsmutablearray/removeobjects(fromindices:numindices:).md)
  Removes the specified number of objects from the array, beginning at the specified index.
- [func removeObjects(in: [Any])](nsmutablearray/removeobjects(in:)-4yb26.md)
  Removes from the receiving array the objects in another given array.
- [func removeObjects(in: NSRange)](nsmutablearray/removeobjects(in:)-1udmn.md)
  Removes from the array each of the objects within a given range.
### Replacing Objects
- [func replaceObject(at: Int, with: Any)](nsmutablearray/replaceobject(at:with:).md)
  Replaces the object at `index` with `anObject`.
- [func replaceObjects(at: IndexSet, with: [Any])](nsmutablearray/replaceobjects(at:with:).md)
  Replaces the objects in the receiving array at locations specified with the objects from a given array.
- [func replaceObjects(in: NSRange, withObjectsFrom: [Any], range: NSRange)](nsmutablearray/replaceobjects(in:withobjectsfrom:range:).md)
  Replaces the objects in the receiving array specified by one given range with the objects in another array specified by another range.
- [func replaceObjects(in: NSRange, withObjectsFrom: [Any])](nsmutablearray/replaceobjects(in:withobjectsfrom:).md)
  Replaces the objects in the receiving array specified by a given range with all of the objects from a given array.
- [func setArray([Any])](nsmutablearray/setarray(_:).md)
  Sets the receiving array’s elements to those in another given array.
### Filtering Content
- [func filter(using: NSPredicate)](nsmutablearray/filter(using:).md)
  Evaluates a given predicate against the array’s content and leaves only objects that match.
### Rearranging Content
- [func exchangeObject(at: Int, withObjectAt: Int)](nsmutablearray/exchangeobject(at:withobjectat:).md)
  Exchanges the objects in the array at given indexes.
- [func sort(using: [NSSortDescriptor])](nsmutablearray/sort(using:)-4eh07.md)
  Sorts the receiver using a given array of sort descriptors.
- [func sort(comparator: (Any, Any) -> ComparisonResult)](nsmutablearray/sort(comparator:).md)
  Sorts the receiver in ascending order using the comparison method specified by a given [`Comparator`](comparator.md) block.
- [func sort(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult)](nsmutablearray/sort(options:usingcomparator:).md)
  Sorts the receiver in ascending order using the specified options and the comparison method specified by a given [`Comparator`](comparator.md) block.
- [func sort((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?)](nsmutablearray/sort(_:context:).md)
  Sorts the receiver in ascending order as defined by the comparison function `compare`.
- [func sort(using: Selector)](nsmutablearray/sort(using:)-537vs.md)
  Sorts the receiver in ascending order, as determined by the comparison method specified by a given selector.
### Initializers
- [init?(coder: NSCoder)](nsmutablearray/init(coder:).md)

## Relationships

### Inherits From
- [NSArray](nsarray.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray)*