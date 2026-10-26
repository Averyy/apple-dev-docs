# NSArray

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSArray : NSObject
```

## Mentions

- [Implementing Handoff in Your App](./implementing-handoff-in-your-app.md)

#### Overview

You can use this type in Swift instead of an [`Array`](../Swift/array.md) constant in cases that require reference semantics.

`NSArray` and its subclass [`NSMutableArray`](./nsmutablearray.md) manage ordered collections of objects called **arrays**. `NSArray` creates static arrays, and `NSMutableArray` creates dynamic arrays. You can use arrays when you need an ordered collection of objects.

`NSArray` is “toll-free bridged” with its Core Foundation counterpart, [`CFArray`](../CoreFoundation/cfarray.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

##### Creating NSArray Objects Using Array Literals

In addition to the provided initializers, such as [`initWithObjects:`](./nsarray/initwithobjects_.md), you can create an `NSArray` object using an *array literal*.

**Swift**:

```swift
let array: NSArray = [someObject, "Hello, World!", 42]
```

**Objective-C**:

```objc
NSArray *array = @[someObject, @"Hello, World!", @42];
```

In Objective-C, the compiler generates code that makes an underlying call to the [`init(objects:count:)`](./nsarray/init%28objects,count%29-7dct1.md) method.

```objc
id objects[] = { someObject, @"Hello, World!", @42 };
NSUInteger count = sizeof(objects) / sizeof(id);
NSArray *array = [NSArray arrayWithObjects:objects
                                     count:count];
```

You should not terminate the list of objects with `nil` when using this literal syntax, and in fact `nil` is an invalid value. For more information about object literals in Objective-C, see [Working with Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/WorkingwithObjects/WorkingwithObjects.html#//apple_ref/doc/uid/TP40011210-CH4) in [Programming with Objective-C](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011210).

In Swift, the `NSArray` class conforms to the `ArrayLiteralConvertible` protocol, which allows it to be initialized with array literals. For more information about object literals in Swift, see [Literal Expression](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/Expressions.html#//apple_ref/doc/uid/TP40014097-CH32-ID390) in [The Swift Programming Language (Swift 4.1)](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/index.html#//apple_ref/doc/uid/TP40014097).

##### Accessing Values Using Subscripting

In addition to the provided instance methods, such as [`object(at:)`](./nsarray/object%28at%29.md), you can access `NSArray` values by their indexes using *subscripting*.

**Swift**:

```swift
let value = array[3]
```

**Objective-C**:

```objc
id value = array[3];
```

##### Subclassing Notes

There is typically little reason to subclass `NSArray`. The class does well what it is designed to do—maintain an ordered collection of objects. But there are situations where a custom `NSArray` object might come in handy. Here are a few possibilities:

- Changing how `NSArray` stores the elements of its collection. You might do this for performance reasons or for better compatibility with legacy code.
- Acquiring more information about what is happening to the collection (for example, statistics gathering).

###### Methods to Override

Any subclass of `NSArray`    *must* override the primitive instance methods [`count`](./nsarray/count.md) and [`object(at:)`](./nsarray/object%28at%29.md). These methods must operate on the backing store that you provide for the elements of the collection. For this backing store you can use a static array, a standard `NSArray` object, or some other data type or mechanism. You may also choose to override, partially or fully, any other `NSArray` method for which you want to provide an alternative implementation.

You might want to implement an initializer for your subclass that is suited to the backing store that the subclass is managing. If you do, your initializer must invoke one of the designated initializers of the `NSArray` class, either [`init()`](./nsarray/init%28%29.md) or [`init(objects:count:)`](./nsarray/init%28objects,count%29-5odxv.md). The `NSArray` class adopts the [`NSCopying`](./nscopying.md), [`NSMutableCopying`](./nsmutablecopying.md), and [`NSCoding`](./nscoding.md) protocols; custom subclasses of `NSArray` should override the methods in these protocols as necessary.

Remember that `NSArray` is the public interface for a class cluster and what this entails for your subclass. You must provide the storage for your subclass and implement the primitive methods that directly act on that storage.

###### Alternatives to Subclassing

Before making a custom subclass of `NSArray`, investigate [`NSPointerArray`](./nspointerarray.md) and the corresponding Core Foundation type, [`CFArray`](../CoreFoundation/cfarray.md). Because `NSArray` and `CFArray` are “toll-free bridged,” you can substitute a `CFArray` object for a `NSArray` object in your code (with appropriate casting). Although they are corresponding types, `CFArray` and `NSArray` do not have identical interfaces or implementations, and you can sometimes do things with `CFArray` that you cannot easily do with `NSArray`. For example, `CFArray` provides a set of callbacks, some of which are for implementing custom retain-release behavior. If you specify `NULL` implementations for these callbacks, you can easily get a non-retaining array.

If the behavior you want to add supplements that of the existing class, you could write a category on `NSArray`. Keep in mind, however, that this category will be in effect for all instances of `NSArray` that you use, and this might have unintended consequences. Alternatively, you could use composition to achieve the desired behavior.

## Topics

### Creating an Array
- [convenience init(object: Any)](./nsarray/init%28object%29.md)
  Creates and returns an array containing a given object.
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](./nsarray/init%28objects,count%29-7dct1.md)
  Creates and returns an array that includes a given number of objects from a given C array.
- [+ array](./nsarray/array.md)
  Creates and returns an empty array.
- [+ arrayWithArray:](./nsarray/arraywitharray_.md)
  Creates and returns an array containing the objects in another given array.
- [+ arrayWithContentsOfFile:](./nsarray/arraywithcontentsoffile_.md)
  Creates and returns an array containing the contents of the file specified by a given path.
- [+ arrayWithObjects:](./nsarray/arraywithobjects_.md)
  Creates and returns an array containing the objects in the argument list.
### Initializing an Array
- [init()](./nsarray/init%28%29.md)
  Initializes a newly allocated array.
- [convenience init(array: [Any])](./nsarray/init%28array%29-o72h.md)
  Initializes a newly allocated array by placing in it the objects contained in a given array.
- [convenience init(array: [Any], copyItems: Bool)](./nsarray/init%28array,copyitems%29.md)
  Initializes a newly allocated array using `anArray` as the source of data objects for the array.
- [convenience init?(contentsOfFile: String)](./nsarray/init%28contentsoffile%29.md)
  Initializes a newly allocated array with the contents of the file specified by a given path.
- [init(objects: UnsafePointer<AnyObject>?, count: Int)](./nsarray/init%28objects,count%29-5odxv.md)
  Initializes a newly allocated array to include a given number of objects from a given C array.
- [- initWithObjects:](./nsarray/initwithobjects_.md)
  Initializes a newly allocated array by placing in it the objects in the argument list.
### Querying an Array
- [func contains(Any) -> Bool](./nsarray/contains%28_%29.md)
  Returns a Boolean value that indicates whether a given object is present in the array.
- [var count: Int](./nsarray/count.md)
  The number of objects in the array.
- [var firstObject: Any?](./nsarray/firstobject.md)
  The first object in the array.
- [var lastObject: Any?](./nsarray/lastobject.md)
  The last object in the array.
- [func object(at: Int) -> Any](./nsarray/object%28at%29.md)
  Returns the object located at the specified index.
- [subscript(Int) -> Any](./nsarray/subscript%28_%29.md)
  Returns the object at the specified index.
- [func objects(at: IndexSet) -> [Any]](./nsarray/objects%28at%29.md)
  Returns an array containing the objects in the array at the indexes specified by a given index set.
- [func objectEnumerator() -> NSEnumerator](./nsarray/objectenumerator%28%29.md)
  Returns an enumerator object that lets you access each object in the array.
- [func reverseObjectEnumerator() -> NSEnumerator](./nsarray/reverseobjectenumerator%28%29.md)
  Returns an enumerator object that lets you access each object in the array, in reverse order.
- [- getObjects:](./nsarray/getobjects_.md)
  Copies all the objects contained in the array to `aBuffer`.
- [- getObjects:range:](./nsarray/getobjects_range_.md)
  Copies references to objects contained in the array that fall within the specified range to `aBuffer`.
### Finding Objects in an Array
- [func index(of: Any) -> Int](./nsarray/index%28of%29.md)
  Returns the lowest index whose corresponding array value is equal to a given object.
- [func index(of: Any, in: NSRange) -> Int](./nsarray/index%28of,in%29.md)
  Returns the lowest index within a specified range whose corresponding array value is equal to a given object .
- [func indexOfObjectIdentical(to: Any) -> Int](./nsarray/indexofobjectidentical%28to%29.md)
  Returns the lowest index whose corresponding array value is identical to a given object.
- [func indexOfObjectIdentical(to: Any, in: NSRange) -> Int](./nsarray/indexofobjectidentical%28to,in%29.md)
  Returns the lowest index within a specified range whose corresponding array value is equal to a given object .
- [func indexOfObject(passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](./nsarray/indexofobject%28passingtest%29.md)
  Returns the index of the first object in the array that passes a test in a given block.
- [func indexOfObject(options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](./nsarray/indexofobject%28options,passingtest%29.md)
  Returns the index of an object in the array that passes a test in a given block for a given set of enumeration options.
- [func indexOfObject(at: IndexSet, options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> Int](./nsarray/indexofobject%28at,options,passingtest%29.md)
  Returns the index, from a given set of indexes, of the first object in the array that passes a test in a given block for a given set of enumeration options.
- [func indexesOfObjects(passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](./nsarray/indexesofobjects%28passingtest%29.md)
  Returns the indexes of objects in the array that pass a test in a given block.
- [func indexesOfObjects(options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](./nsarray/indexesofobjects%28options,passingtest%29.md)
  Returns the indexes of objects in the array that pass a test in a given block for a given set of enumeration options.
- [func indexesOfObjects(at: IndexSet, options: NSEnumerationOptions, passingTest: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Bool) -> IndexSet](./nsarray/indexesofobjects%28at,options,passingtest%29.md)
  Returns the indexes, from a given set of indexes, of objects in the array that pass a test in a given block for a given set of enumeration options.
- [func index(of: Any, inSortedRange: NSRange, options: NSBinarySearchingOptions, usingComparator: (Any, Any) -> ComparisonResult) -> Int](./nsarray/index%28of,insortedrange,options,usingcomparator%29.md)
  Returns the index, within a specified range, of an object compared with elements in the array using a given `NSComparator` block.
### Sending Messages to Elements
- [func enumerateObjects((Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./nsarray/enumerateobjects%28_%29.md)
  Executes a given closure or block using each object in the array, starting with the first object and continuing through the array to the last object.
- [func enumerateObjects(options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./nsarray/enumerateobjects%28options,using%29.md)
  Executes a given closure or block using each object in the array with the specified options.
- [func enumerateObjects(at: IndexSet, options: NSEnumerationOptions, using: (Any, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./nsarray/enumerateobjects%28at,options,using%29.md)
  Executes a given block using the objects in the array at the specified indexes.
- [- makeObjectsPerformSelector:](./nsarray/makeobjectsperformselector_.md)
  Sends to each object in the array the message identified by a given selector, starting with the first object and continuing through the array to the last object.
- [- makeObjectsPerformSelector:withObject:](./nsarray/makeobjectsperformselector_withobject_.md)
  Sends the `aSelector` message to each object in the array, starting with the first object and continuing through the array to the last object.
### Comparing Arrays
- [func firstObjectCommon(with: [Any]) -> Any?](./nsarray/firstobjectcommon%28with%29.md)
  Returns the first object contained in the receiving array that’s equal to an object in another given array.
- [func isEqual(to: [Any]) -> Bool](./nsarray/isequal%28to%29.md)
  Compares the receiving array to another array.
### Deriving New Arrays
- [func adding(Any) -> [Any]](./nsarray/adding%28_%29.md)
  Returns a new array that is a copy of the receiving array with a given object added to the end.
- [func addingObjects(from: [Any]) -> [Any]](./nsarray/addingobjects%28from%29.md)
  Returns a new array that is a copy of the receiving array with the objects contained in another array added to the end.
- [func filtered(using: NSPredicate) -> [Any]](./nsarray/filtered%28using%29.md)
  Evaluates a given predicate against each object in the receiving array and returns a new array containing the objects for which the predicate returns true.
- [func subarray(with: NSRange) -> [Any]](./nsarray/subarray%28with%29.md)
  Returns a new array containing the receiving array’s elements that fall within the limits specified by a given range.
### Sorting
- [var sortedArrayHint: Data](./nsarray/sortedarrayhint.md)
  Analyzes the array and returns a “hint” that speeds the sorting of the array when the hint is supplied to [`sortedArray(_:context:hint:)`](./nsarray/sortedarray%28_,context,hint%29.md).
- [func sortedArray((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?) -> [Any]](./nsarray/sortedarray%28_,context%29.md)
  Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [func sortedArray((Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?, hint: Data?) -> [Any]](./nsarray/sortedarray%28_,context,hint%29.md)
  Returns a new array that lists the receiving array’s elements in ascending order as defined by the comparison function `comparator`.
- [func sortedArray(using: [NSSortDescriptor]) -> [Any]](./nsarray/sortedarray%28using%29-82wi1.md)
  Returns a copy of the receiving array sorted as specified by a given array of sort descriptors.
- [func sortedArray(using: Selector) -> [Any]](./nsarray/sortedarray%28using%29-9nhh9.md)
  Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given selector.
- [func sortedArray(comparator: (Any, Any) -> ComparisonResult) -> [Any]](./nsarray/sortedarray%28comparator%29.md)
  Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [func sortedArray(options: NSSortOptions, usingComparator: (Any, Any) -> ComparisonResult) -> [Any]](./nsarray/sortedarray%28options,usingcomparator%29.md)
  Returns an array that lists the receiving array’s elements in ascending order, as determined by the comparison method specified by a given `NSComparator` block.
- [typealias Comparator](./comparator.md)
  Defines the signature for a block object used for comparison operations.
### Working with String Elements
- [func componentsJoined(by: String) -> String](./nsarray/componentsjoined%28by%29.md)
  Constructs and returns an `NSString` object that is the result of interposing a given separator between the elements of the array.
### Creating a Description
- [var description: String](./nsarray/description.md)
  A string that represents the contents of the array, formatted as a property list.
- [func description(withLocale: Any?) -> String](./nsarray/description%28withlocale%29.md)
  Returns a string that represents the contents of the array, formatted as a property list.
- [func description(withLocale: Any?, indent: Int) -> String](./nsarray/description%28withlocale,indent%29.md)
  Returns a string that represents the contents of the array, formatted as a property list.
### Storing Arrays
- [func write(toFile: String, atomically: Bool) -> Bool](./nsarray/write%28tofile,atomically%29.md)
  Writes the contents of the array to a file at a given path.
- [func write(to: URL, atomically: Bool) -> Bool](./nsarray/write%28to,atomically%29.md)
  Writes the contents of the array to the location specified by a given URL.
### Collecting Paths
- [func pathsMatchingExtensions([String]) -> [String]](./nsarray/pathsmatchingextensions%28_%29.md)
  Returns an array containing all the pathname elements in the receiving array that have filename extensions from a given array.
### Key-Value Observing
- [func addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](./nsarray/addobserver%28_,forkeypath,options,context%29.md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String)](./nsarray/removeobserver%28_,forkeypath%29.md)
  Raises an exception.
- [func removeObserver(NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](./nsarray/removeobserver%28_,forkeypath,context%29.md)
  Raises an exception.
- [func removeObserver(NSObject, fromObjectsAt: IndexSet, forKeyPath: String, context: UnsafeMutableRawPointer?)](./nsarray/removeobserver%28_,fromobjectsat,forkeypath,context%29.md)
  Raises an exception.
- [func addObserver(NSObject, toObjectsAt: IndexSet, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](./nsarray/addobserver%28_,toobjectsat,forkeypath,options,context%29.md)
  Registers an observer to receive key value observer notifications for the specified key-path relative to the objects at the indexes.
- [func removeObserver(NSObject, fromObjectsAt: IndexSet, forKeyPath: String)](./nsarray/removeobserver%28_,fromobjectsat,forkeypath%29.md)
  Removes `anObserver` from all key value observer notifications associated with the specified `keyPath` relative to the array’s objects at `indexes`.
### Key-Value Coding
- [func setValue(Any?, forKey: String)](./nsarray/setvalue%28_,forkey%29.md)
  Invokes [`setValue(_:forKey:)`](./nsarray/setvalue%28_,forkey%29.md) on each of the array’s items using the specified `value` and `key`.
- [func value(forKey: String) -> Any](./nsarray/value%28forkey%29.md)
  Returns an array containing the results of invoking [`value(forKey:)`](./nsarray/value%28forkey%29.md) using `key` on each of the array’s objects.
### Randomly Shuffling an Array
- [func shuffled() -> [Any]](./nsarray/shuffled%28%29.md)
  Returns a new array that lists this array’s elements in a random order.
- [func shuffled(using: GKRandomSource) -> [Any]](./nsarray/shuffled%28using%29.md)
  Returns a new array that lists this array’s elements in a random order, using the specified random source.
### Comparing with Another Array
- [class NSOrderedCollectionDifference](./nsorderedcollectiondifference.md)
  An object representing the difference between two ordered collections.
- [struct NSOrderedCollectionDifferenceCalculationOptions](./nsorderedcollectiondifferencecalculationoptions.md)
  Constants that specify the options to use when creating an ordered collection difference.
- [- differenceFromArray:](./nsarray/differencefromarray_.md)
  Compares two arrays to create a difference object that represents the changes between them.
- [- differenceFromArray:withOptions:](./nsarray/differencefromarray_withoptions_.md)
  Compares two arrays, with options, to create a difference object that represents the changes between them.
- [- differenceFromArray:withOptions:usingEquivalenceTest:](./nsarray/differencefromarray_withoptions_usingequivalencetest_.md)
  Compares two arrays, using the provided block and with options, to create a difference object that represents the changes between them.
### New Methods
- [init?(coder: NSCoder)](./nsarray/init%28coder%29.md)
### Constants
- [struct NSBinarySearchingOptions](./nsbinarysearchingoptions.md)
  Options for searches and insertions using [`index(of:inSortedRange:options:usingComparator:)`](./nsarray/index%28of,insortedrange,options,usingcomparator%29.md).
### Initializers
- [convenience init(array: NSArray)](./nsarray/init%28array%29-9rh7.md)
  Initializes a newly allocated array by placing in it the objects contained in a given array.
- [convenience init?(contentsOf: URL)](./nsarray/init%28contentsof%29.md)
  Initializes a newly allocated array with the contents of the location specified by a given URL.
- [convenience init(contentsOf: URL, error: ()) throws](./nsarray/init%28contentsof,error%29.md)
- [convenience init(objects: Any...)](./nsarray/init%28objects%29.md)
### Instance Methods
- [func write(to: URL) throws](./nsarray/write%28to%29.md)
- [- arrayByApplyingDifference:](./nsarray/arraybyapplyingdifference_.md)
  Creates a new array by applying a difference object to an existing array.
### Default Implementations
- [ExpressibleByArrayLiteral Implementations](./nsarray/expressiblebyarrayliteral-implementations.md)
- [NSArray Implementations](./nsarray/nsarray-implementations.md)
- [Sequence Implementations](./nsarray/sequence-implementations.md)
### Type Methods
- [+ arrayWithContentsOfURL:](./nsarray/arraywithcontentsofurl_.md)
  Creates and returns an array containing the contents specified by a given URL.
- [+ arrayWithContentsOfURL:error:](./nsarray/arraywithcontentsofurl_error_.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NSMutableArray](./nsmutablearray.md)
### Conforms To
- [CKRecordValue](../CloudKit/ckrecordvalue-c.protocol.md)
- [CKRecordValueProtocol](../CloudKit/ckrecordvalueprotocol.md)
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
- [NSMutableArray](./nsmutablearray.md)
  A dynamic ordered collection of objects.
- [NSDictionary](./nsdictionary.md)
  A static collection of objects associated with unique keys.
- [NSMutableDictionary](./nsmutabledictionary.md)
  A dynamic collection of objects associated with unique keys.
- [NSSet](./nsset.md)
  A static, unordered collection of unique objects.
- [NSMutableSet](./nsmutableset.md)
  A dynamic unordered collection of unique objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray)*