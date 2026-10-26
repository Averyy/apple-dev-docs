# NSMutableArray

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSMutableArray : NSArray
```

#### Overview

You can use this type in Swift instead of an [`Array`](../Swift/array.md) variable in cases that require reference semantics.

The `NSMutableArray` class declares the programmatic interface to objects that manage a modifiable array of objects. This class adds insertion and deletion operations to the basic array-handling behavior inherited from [`NSArray`](./nsarray.md).

NSMutableArray is “toll-free bridged” with its Core Foundation counterpart, [`CFMutableArray`](../CoreFoundation/cfmutablearray.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information.

##### Accessing Values Using Subscripting

In addition to the provided instance methods, such as [`replaceObject(at:with:)`](./nsmutablearray/replaceobject%28at,with%29.md), you can access `NSArray` values by their indexes using *subscripting*.

**Swift**:

```swift
mutableArray[3] = "someValue"
```

**Objective-C**:

```objc
mutableArray[3] = @"someValue";
```

##### Subclassing Notes

There is typically little reason to subclass `NSMutableArray`. The class does well what it is designed to do—maintain a mutable, ordered collection of objects. But there are situations where a custom `NSArray` object might come in handy. Here are a few possibilities:

- Changing how `NSMutableArray` stores the elements of its collection. You might do this for performance reasons or for better compatibility with legacy code.
- Acquiring more information about what is happening to the collection (for example, statistics gathering).

###### Methods to Override

`NSMutableArray` defines five primitive methods:

- [`insert(_:at:)`](./nsmutablearray/insert%28_,at%29-5dbx5.md)
- [`removeObject(at:)`](./nsmutablearray/removeobject%28at%29.md)
- [`add(_:)`](./nsmutablearray/add%28_%29.md)
- [`removeLastObject()`](./nsmutablearray/removelastobject%28%29.md)
- [`replaceObject(at:with:)`](./nsmutablearray/replaceobject%28at,with%29.md)

In a subclass, you must override all these methods. You must also override the primitive methods of the [`NSArray`](./nsarray.md) class.

## Topics

### Creating and Initializing a Mutable Array
- [init?(contentsOfURL: URL)](./nsmutablearray/init%28contentsofurl%29.md)
  Creates and returns a mutable array containing the contents specified by a given URL.
- [init()](./nsmutablearray/init%28%29.md)
  Initializes a newly allocated array.
- [init(capacity: Int)](./nsmutablearray/init%28capacity%29.md)
  Returns an array, initialized with enough memory to initially hold a given number of objects.
- [+ arrayWithCapacity:](./nsmutablearray/arraywithcapacity_.md)
  Creates and returns an `NSMutableArray` object with enough allocated memory to initially hold a given number of objects.
- [+ arrayWithContentsOfFile:](./nsmutablearray/arraywithcontentsoffile_.md)
  Creates and returns a mutable array containing the contents of the file specified by the given path.
- [- initWithContentsOfFile:](./nsmutablearray/initwithcontentsoffile_.md)
  Initializes a newly allocated mutable array with the contents of the file specified by a given path
- [- initWithContentsOfURL:](./nsmutablearray/initwithcontentsofurl_.md)
  Initialized a newly allocated mutable array with the contents of the location specified by a given URL.
### Adding Objects
- [func add(Any)](./nsmutablearray/add%28_%29.md)
  Inserts a given object at the end of the array.
- [func addObjects(from: [Any])](./nsmutablearray/addobjects%28from%29.md)
  Adds the objects contained in another given array to the end of the receiving array’s content.
- [func insert(Any, at: Int)](./nsmutablearray/insert%28_,at%29-5dbx5.md)
  Inserts a given object into the array’s contents at a given index.
- [func insert([Any], at: IndexSet)](./nsmutablearray/insert%28_,at%29-73pln.md)
  Inserts the objects in the provided array into the receiving array at the specified indexes.
### Removing Objects
- [func removeAllObjects()](./nsmutablearray/removeallobjects%28%29.md)
  Empties the array of all its elements.
- [func removeLastObject()](./nsmutablearray/removelastobject%28%29.md)
  Removes the object with the highest-valued index in the array
- [func remove(Any)](./nsmutablearray/remove%28_%29.md)
  Removes all occurrences in the array of a given object.
- [func remove(Any, in: NSRange)](./nsmutablearray/remove%28_,in%29.md)
  Removes all occurrences within a specified range in the array of a given object.
- [func removeObject(at: Int)](./nsmutablearray/removeobject%28at%29.md)
  Removes the object at `index` .
- [func removeObjects(at: IndexSet)](./nsmutablearray/removeobjects%28at%29.md)
  Removes the objects at the specified indexes from the array.
- [func removeObject(identicalTo: Any)](./nsmutablearray/removeobject%28identicalto%29.md)
  Removes all occurrences of a given object in the array.
- [func removeObject(identicalTo: Any, in: NSRange)](./nsmutablearray/removeobject%28identicalto,in%29.md)
  Removes all occurrences of `anObject` within the specified range in the array.
- [func removeObjects(fromIndices: UnsafeMutablePointer<Int>, numIndices: Int)](./nsmutablearray/removeobjects%28fromindices,numindices%29.md)
  Removes the specified number of objects from the array, beginning at the specified index.
- [func removeObjects(in: [Any])](./nsmutablearray/removeobjects%28in%29-4yb26.md)
  Removes from the receiving array the objects in another given array.
- [func removeObjects(in: NSRange)](./nsmutablearray/removeobjects%28in%29-1udmn.md)
  Removes from the array each of the objects within a given range.
### Replacing Objects
- [func replaceObject(at: Int, with: Any)](./nsmutablearray/replaceobject%28at,with%29.md)
  Replaces the object at `index` with `anObject`.
- [func replaceObjects(at: IndexSet, with: [Any])](./nsmutablearray/replaceobjects%28at,with%29.md)
  Replaces the objects in the receiving array at locations specified with the objects from a given array.
- [func replaceObjects(in: NSRange, withObjectsFrom: [Any], range: NSRange)](./nsmutablearray/replaceobjects%28in,withobjectsfrom,range%29.md)
  Replaces the objects in the receiving array specified by one given range with the objects in another array specified by another range.
- [func replaceObjects(in: NSRange, withObjectsFrom: [Any])](./nsmutablearray/replaceobjects%28in,withobjectsfrom%29.md)
  Replaces the objects in the receiving array specified by a given range with all of the objects from a given array.
- [func setArray([Any])](./nsmutablearray/setarray%28_%29.md)
  Sets the receiving array’s elements to those in another given array.
- [- setObject:atIndexedSubscript:](./nsmutablearray/setobject_atindexedsubscript_.md)
  Replaces the object at the index with the new object, possibly adding the object.
### Filtering Content
- [func filter(using: NSPredicate)](./nsmutablearray/filter%28using%29.md)
  Evaluates a given predicate against the array’s content and leaves only objects that match.
### Rearranging Content
- [func exchangeObject(at: Int, withObjectAt: Int)](./nsmutablearray/exchangeobject%28at,withobjectat%29.md)
  Exchanges the objects in the array at given indexes.
- [func sort(using: [NSSortDescriptor])](./nsmutablearray/sort%28using%29-4eh07.md)
  Sorts the receiver using a given array of sort descriptors.
- [func sort(comparator: (Any, Any) -> ComparisonResult)](./nsmutablearray/sort%28comparator%29.md)
  Sorts the receiver in ascending order using the comparison method specified by a given [`Comparator`](./comparator.md) block.
- [func sort(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult)](./nsmutablearray/sort%28options,usingcomparator%29.md)
  Sorts the receiver in ascending order using the specified options and the comparison method specified by a given [`Comparator`](./comparator.md) block.
- [func sort((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?)](./nsmutablearray/sort%28_,context%29.md)
  Sorts the receiver in ascending order as defined by the comparison function `compare`.
- [func sort(using: Selector)](./nsmutablearray/sort%28using%29-537vs.md)
  Sorts the receiver in ascending order, as determined by the comparison method specified by a given selector.
### Initializers
- [init?(coder: NSCoder)](./nsmutablearray/init%28coder%29.md)
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](./nsmutablearray/init%28objects,count%29.md)
### Default Implementations
- [NSMutableArray Implementations](./nsmutablearray/nsmutablearray-implementations.md)
### Instance Methods
- [- applyDifference:](./nsmutablearray/applydifference_.md)
### Type Methods
- [+ arrayWithContentsOfURL:](./nsmutablearray/arraywithcontentsofurl_.md)
  Creates and returns a mutable array containing the contents specified by a given URL.

## Relationships

### Inherits From
- [NSArray](./nsarray.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
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

### Basic Collections
- [NSArray](./nsarray.md)
  A static ordered collection of objects.
- [NSDictionary](./nsdictionary.md)
  A static collection of objects associated with unique keys.
- [NSMutableDictionary](./nsmutabledictionary.md)
  A dynamic collection of objects associated with unique keys.
- [NSSet](./nsset.md)
  A static, unordered collection of unique objects.
- [NSMutableSet](./nsmutableset.md)
  A dynamic unordered collection of unique objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray)*