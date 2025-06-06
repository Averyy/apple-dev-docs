# NSArray

**Framework**: Foundation  
**Kind**: class

A static ordered collection of objects.

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
class NSArray
```

## Mentions

- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md)

#### Overview

You can use this type in Swift instead of an [`Array`](https://developer.apple.com/documentation/Swift/Array) constant in cases that require reference semantics.

`NSArray` and its subclass [`NSMutableArray`](nsmutablearray.md) manage ordered collections of objects called . `NSArray` creates static arrays, and `NSMutableArray` creates dynamic arrays. You can use arrays when you need an ordered collection of objects.

`NSArray` is “toll-free bridged” with its Core Foundation counterpart, [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray). See [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

##### Creating Nsarray Objects Using Array Literals

In addition to the provided initializers, such as [`initWithObjects:`](nsarray/initwithobjects:.md), you can create an `NSArray` object using an .

In Objective-C, the compiler generates code that makes an underlying call to the [`init(objects:count:)`](nsarray/init(objects:count:)-7dct1.md) method.

```objc
id objects[] = { someObject, @"Hello, World!", @42 };
NSUInteger count = sizeof(objects) / sizeof(id);
NSArray *array = [NSArray arrayWithObjects:objects
                                     count:count];
```

You should not terminate the list of objects with `nil` when using this literal syntax, and in fact `nil` is an invalid value. For more information about object literals in Objective-C, see [`Working with Objects`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/WorkingwithObjects/WorkingwithObjects.html#//apple_ref/doc/uid/TP40011210-CH4) in [`Programming with Objective-C`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011210).

In Swift, the `NSArray` class conforms to the `ArrayLiteralConvertible` protocol, which allows it to be initialized with array literals. For more information about object literals in Swift, see [`Literal Expression`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/Expressions.html#//apple_ref/doc/uid/TP40014097-CH32-ID390) in [`The Swift Programming Language (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/index.html#//apple_ref/doc/uid/TP40014097).

##### Accessing Values Using Subscripting

In addition to the provided instance methods, such as [`object(at:)`](nsarray/object(at:).md), you can access `NSArray` values by their indexes using .

##### Subclassing Notes

There is typically little reason to subclass `NSArray`. The class does well what it is designed to do—maintain an ordered collection of objects. But there are situations where a custom `NSArray` object might come in handy. Here are a few possibilities:

- Changing how `NSArray` stores the elements of its collection. You might do this for performance reasons or for better compatibility with legacy code.
- Acquiring more information about what is happening to the collection (for example, statistics gathering).

###### Methods to Override

Any subclass of `NSArray`     override the primitive instance methods [`count`](nsarray/count.md) and [`object(at:)`](nsarray/object(at:).md). These methods must operate on the backing store that you provide for the elements of the collection. For this backing store you can use a static array, a standard `NSArray` object, or some other data type or mechanism. You may also choose to override, partially or fully, any other `NSArray` method for which you want to provide an alternative implementation.

You might want to implement an initializer for your subclass that is suited to the backing store that the subclass is managing. If you do, your initializer must invoke one of the designated initializers of the `NSArray` class, either [`init()`](nsarray/init().md) or [`init(objects:count:)`](nsarray/init(objects:count:)-5odxv.md). The `NSArray` class adopts the [`NSCopying`](nscopying.md), [`NSMutableCopying`](nsmutablecopying.md), and [`NSCoding`](nscoding.md) protocols; custom subclasses of `NSArray` should override the methods in these protocols as necessary.

Remember that `NSArray` is the public interface for a class cluster and what this entails for your subclass. You must provide the storage for your subclass and implement the primitive methods that directly act on that storage.

###### Alternatives to Subclassing

Before making a custom subclass of `NSArray`, investigate [`NSPointerArray`](nspointerarray.md) and the corresponding Core Foundation type, [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray). Because `NSArray` and `CFArray` are “toll-free bridged,” you can substitute a `CFArray` object for a `NSArray` object in your code (with appropriate casting). Although they are corresponding types, `CFArray` and `NSArray` do not have identical interfaces or implementations, and you can sometimes do things with `CFArray` that you cannot easily do with `NSArray`. For example, `CFArray` provides a set of callbacks, some of which are for implementing custom retain-release behavior. If you specify `NULL` implementations for these callbacks, you can easily get a non-retaining array.

If the behavior you want to add supplements that of the existing class, you could write a category on `NSArray`. Keep in mind, however, that this category will be in effect for all instances of `NSArray` that you use, and this might have unintended consequences. Alternatively, you could use composition to achieve the desired behavior.

## Topics

### Creating an Array
- [init?(contentsOfURL: URL)](nsarray/init(contentsofurl:)-fk8x.md)
  Creates and returns an array containing the contents specified by a given URL.
- [convenience init(object: Any)](nsarray/init(object:).md)
  Creates and returns an array containing a given object.
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](nsarray/init(objects:count:)-7dct1.md)
  Creates and returns an array that includes a given number of objects from a given C array.
### Initializing an Array
- [init()](nsarray/init.md)
  Initializes a newly allocated array.
- [convenience init(array: [Any])](nsarray/init(array:)-o72h.md)
  Initializes a newly allocated array by placing in it the objects contained in a given array.
- [convenience init(array: [Any], copyItems: Bool)](nsarray/init(array:copyitems:).md)
  Initializes a newly allocated array using `anArray` as the source of data objects for the array.
- [convenience init?(contentsOfFile: String)](nsarray/init(contentsoffile:).md)
  Initializes a newly allocated array with the contents of the file specified by a given path.
- [convenience init?(contentsOfURL: URL)](nsarray/init(contentsofurl:)-5lo2y.md)
  Initializes a newly allocated array with the contents of the location specified by a given URL.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](nsarray/init(objects:count:)-5odxv.md)
  Initializes a newly allocated array to include a given number of objects from a given C array.
### Querying an Array
- [func contains(Any) -> Bool](nsarray/contains(_:).md)
  Returns a Boolean value that indicates whether a given object is present in the array.
- [var count: Int](nsarray/count.md)
  The number of objects in the array.
- [var firstObject: Any?](nsarray/firstobject.md)
  The first object in the array.
- [var lastObject: Any?](nsarray/lastobject.md)
  The last object in the array.
- [func object(at: Int) -> Any](nsarray/object(at:).md)
  Returns the object located at the specified index.
- [subscript(Int) -> Any](nsarray/subscript(_:).md)
  Returns the object at the specified index.
- [func objects(at: IndexSet) -> [Any]](nsarray/objects(at:).md)
  Returns an array containing the objects in the array at the indexes specified by a given index set.
- [func objectEnumerator() -> NSEnumerator](nsarray/objectenumerator.md)
  Returns an enumerator object that lets you access each object in the array.
- [func reverseObjectEnumerator() -> NSEnumerator](nsarray/reverseobjectenumerator.md)
  Returns an enumerator object that lets you access each object in the array, in reverse order.
### Finding Objects in an Array
- [func index(of: Any) -> Int](nsarray/index(of:).md)
  Returns the lowest index whose corresponding array value is equal to a given object.
- [func index(of: Any, in: NSRange) -> Int](nsarray/index(of:in:).md)
  Returns the lowest index within a specified range whose corresponding array value is equal to a given object .
- [func indexOfObjectIdentical(to: Any) -> Int](nsarray/indexofobjectidentical(to:).md)
  Returns the lowest index whose corresponding array value is identical to a given object.
- [func indexOfObjectIdentical(to: Any, in: NSRange) -> Int](nsarray/indexofobjectidentical(to:in:).md)
  Returns the lowest index within a specified range whose corresponding array value is equal to a given object .
- [func indexOfObject(passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](nsarray/indexofobject(passingtest:).md)
  Returns the index of the first object in the array that passes a test in a given block.
- [func indexOfObject(options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](nsarray/indexofobject(options:passingtest:).md)
  Returns the index of an object in the array that passes a test in a given block for a given set of enumeration options.
- [func indexOfObject(at: IndexSet, options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](nsarray/indexofobject(at:options:passingtest:).md)
  Returns the index, from a given set of indexes, of the first object in the array that passes a test in a given block for a given set of enumeration options.
- [func indexesOfObjects(passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsarray/indexesofobjects(passingtest:).md)
  Returns the indexes of objects in the array that pass a test in a given block.
- [func indexesOfObjects(options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsarray/indexesofobjects(options:passingtest:).md)
  Returns the indexes of objects in the array that pass a test in a given block for a given set of enumeration options.
- [func indexesOfObjects(at: IndexSet, options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](nsarray/indexesofobjects(at:options:passingtest:).md)
  Returns the indexes, from a given set of indexes, of objects in the array that pass a test in a given block for a given set of enumeration options.
- [func index(of: Any, inSortedRange: NSRange, options: NSBinarySearchingOptions, usingComparator: (Any, Any) -> ComparisonResult) -> Int](nsarray/index(of:insortedrange:options:usingcomparator:).md)
  Returns the index, within a specified range, of an object compared with elements in the array using a given `NSComparator` block.
### Sending Messages to Elements
- [func enumerateObjects((Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsarray/enumerateobjects(_:).md)
  Executes a given closure or block using each object in the array, starting with the first object and continuing through the array to the last object.
- [func enumerateObjects(options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsarray/enumerateobjects(options:using:).md)
  Executes a given closure or block using each object in the array with the specified options.
- [func enumerateObjects(at: IndexSet, options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsarray/enumerateobjects(at:options:using:).md)
  Executes a given block using the objects in the array at the specified indexes.
### Comparing Arrays
- [func firstObjectCommon(with: [Any]) -> Any?](nsarray/firstobjectcommon(with:).md)
  Returns the first object contained in the receiving array that’s equal to an object in another given array.
- [func isEqual(to: [Any]) -> Bool](nsarray/isequal(to:).md)
  Compares the receiving array to another array.
### Deriving New Arrays
- [func adding(Any) -> [Any]](nsarray/adding(_:).md)
  Returns a new array that is a copy of the receiving array with a given object added to the end.
- [func addingObjects(from: [Any]) -> [Any]](nsarray/addingobjects(from:).md)
  Returns a new array that is a copy of the receiving array with the objects contained in another array added to the end.
- [func filtered(using: NSPredicate) -> [Any]](nsarray/filtered(using:).md)
  Evaluates a given predicate against each object in the receiving array and returns a new array containing the objects for which the predicate returns true.
- [func subarray(with: NSRange) -> [Any]](nsarray/subarray(with:).md)
  Returns a new array containing the receiving array’s elements that fall within the limits specified by a given range.
### Sorting
- [var sortedArrayHint: Data](nsarray/sortedarrayhint.md)
  Analyzes the array and returns a “hint” that speeds the sorting of the array when the hint is supplied to [`sortedArray(_:context:hint:)`](nsarray/sortedarray(_:context:hint:).md).
- [func sortedArray((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?) -> [Any]](nsarray/sortedarray(_:context:).md)
  Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [func sortedArray((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?, hint: Data?) -> [Any]](nsarray/sortedarray(_:context:hint:).md)
  Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [func sortedArray(using: [NSSortDescriptor]) -> [Any]](nsarray/sortedarray(using:)-82wi1.md)
  Returns a copy of the receiving array sorted as specified by a given array of sort descriptors.
- [func sortedArray(using: Selector) -> [Any]](nsarray/sortedarray(using:)-9nhh9.md)
  Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given selector.
- [func sortedArray(comparator: (Any, Any) -> ComparisonResult) -> [Any]](nsarray/sortedarray(comparator:).md)
  Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [func sortedArray(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult) -> [Any]](nsarray/sortedarray(options:usingcomparator:).md)
  Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [typealias Comparator](comparator.md)
  Defines the signature for a block object used for comparison operations.
### Working with String Elements
- [func componentsJoined(by: String) -> String](nsarray/componentsjoined(by:).md)
  Constructs and returns an `NSString` object that is the result of interposing a given separator between the elements of the array.
### Creating a Description
- [var description: String](nsarray/description.md)
  A string that represents the contents of the array, formatted as a property list.
- [func description(withLocale: Any?) -> String](nsarray/description(withlocale:).md)
  Returns a string that represents the contents of the array, formatted as a property list.
- [func description(withLocale: Any?, indent: Int) -> String](nsarray/description(withlocale:indent:).md)
  Returns a string that represents the contents of the array, formatted as a property list.
### Storing Arrays
- [func write(toFile: String, atomically: Bool) -> Bool](nsarray/write(tofile:atomically:).md)
  Writes the contents of the array to a file at a given path.
- [func write(to: URL, atomically: Bool) -> Bool](nsarray/write(to:atomically:).md)
  Writes the contents of the array to the location specified by a given URL.
### Collecting Paths
- [func pathsMatchingExtensions([String]) -> [String]](nsarray/pathsmatchingextensions(_:).md)
  Returns an array containing all the pathname elements in the receiving array that have filename extensions from a given array.
### Key-Value Observing
- [func addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](nsarray/addobserver(_:forkeypath:options:context:).md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String)](nsarray/removeobserver(_:forkeypath:).md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](nsarray/removeobserver(_:forkeypath:context:).md)
  Raises an exception.
- [func removeObserver(NSObject, fromObjectsAt: IndexSet, forKeyPath: String, context: UnsafeMutableRawPointer?)](nsarray/removeobserver(_:fromobjectsat:forkeypath:context:).md)
  Raises an exception.
- [func addObserver(NSObject, toObjectsAt: IndexSet, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](nsarray/addobserver(_:toobjectsat:forkeypath:options:context:).md)
  Registers an observer to receive key value observer notifications for the specified key-path relative to the objects at the indexes.
- [func removeObserver(NSObject, fromObjectsAt: IndexSet, forKeyPath: String)](nsarray/removeobserver(_:fromobjectsat:forkeypath:).md)
  Removes `anObserver` from all key value observer notifications associated with the specified `keyPath` relative to the array’s objects at `indexes`.
### Key-Value Coding
- [func setValue(Any?, forKey: String)](nsarray/setvalue(_:forkey:).md)
  Invokes [`setValue(_:forKey:)`](nsarray/setvalue(_:forkey:).md) on each of the array’s items using the specified `value` and `key`.
- [func value(forKey: String) -> Any](nsarray/value(forkey:).md)
  Returns an array containing the results of invoking [`value(forKey:)`](nsarray/value(forkey:).md) using `key` on each of the array’s objects.
### Randomly Shuffling an Array
- [func shuffled() -> [Any]](nsarray/shuffled.md)
  Returns a new array that lists this array’s elements in a random order.
- [func shuffled(using: GKRandomSource) -> [Any]](nsarray/shuffled(using:).md)
  Returns a new array that lists this array’s elements in a random order, using the specified random source.
### Comparing with Another Array
- [class NSOrderedCollectionDifference](nsorderedcollectiondifference.md)
  An object representing the difference between two ordered collections.
- [struct NSOrderedCollectionDifferenceCalculationOptions](nsorderedcollectiondifferencecalculationoptions.md)
  Constants that specify the options to use when creating an ordered collection difference.
### New Methods
- [init?(coder: NSCoder)](nsarray/init(coder:).md)
### Constants
- [struct NSBinarySearchingOptions](nsbinarysearchingoptions.md)
  Options for searches and insertions using [`index(of:inSortedRange:options:usingComparator:)`](nsarray/index(of:insortedrange:options:usingcomparator:).md).
### Initializers
- [convenience init(array: NSArray)](nsarray/init(array:)-9rh7.md)
- [convenience init(contentsOfURL: URL, error: ()) throws](nsarray/init(contentsofurl:error:).md)
- [convenience init(objects: Any...)](nsarray/init(objects:).md)
### Instance Methods
- [func write(to: URL) throws](nsarray/write(to:).md)
### Default Implementations
- [ExpressibleByArrayLiteral Implementations](nsarray/expressiblebyarrayliteral-implementations.md)
- [Sequence Implementations](nsarray/sequence-implementations.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSMutableArray](nsmutablearray.md)
### Conforms To
- [CKRecordValue](../CloudKit/CKRecordValue-c.protocol.md)
- [CKRecordValueProtocol](../CloudKit/CKRecordValueProtocol.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray)*