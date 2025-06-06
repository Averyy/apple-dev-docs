# CFArray

**Framework**: Core Foundation  
**Kind**: class

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CFArray
```

#### Overview

CFArray and its derived mutable type, [`CFMutableArray`](cfmutablearray.md), manage ordered collections of values called arrays. CFArray creates static arrays and CFMutableArray creates dynamic arrays.

You create a static array object using either the [`CFArrayCreate(_:_:_:_:)`](cfarraycreate(_:_:_:_:).md) or [`CFArrayCreateCopy(_:_:)`](cfarraycreatecopy(_:_:).md) function. These functions return an array containing the values you pass in as arguments. (Note that arrays can’t contain `NULL` pointers; in most cases, though, you can use the [`kCFNull`](kcfnull.md) constant instead.) Values are not copied but retained using the retain callback provided when an array was created. Similarly, when a value is removed from an array, it is released using the release callback.

CFArray’s two primitive functions [`CFArrayGetCount(_:)`](cfarraygetcount(_:).md) and [`CFArrayGetValueAtIndex(_:_:)`](cfarraygetvalueatindex(_:_:).md) provide the basis for all other functions in its interface. The [`CFArrayGetCount(_:)`](cfarraygetcount(_:).md) function returns the number of elements in an array; [`CFArrayGetValueAtIndex(_:_:)`](cfarraygetvalueatindex(_:_:).md) gives you access to an array’s elements by index, with index values starting at 0.

A number of CFArray functions allow you to operate over a range of values in an array, for example [`CFArrayApplyFunction(_:_:_:_:)`](cfarrayapplyfunction(_:_:_:_:).md) lets you apply a function to values in an array, and [`CFArrayBSearchValues(_:_:_:_:_:)`](cfarraybsearchvalues(_:_:_:_:_:).md) searches an array for the value that matches its parameter. Recall that a range is defined as `{start, length}`, therefore to operate over the entire array the range you supply should be `{0, N}` (where `N` is the count of the array).

CFArray is “toll-free bridged” with its Cocoa Foundation counterpart, [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSArray *` parameter, you can pass in a `CFArrayRef`, and in a function where you see a `CFArrayRef` parameter, you can pass in an NSArray instance. This also applies to concrete subclasses of NSArray. See [`Toll-Free Bridged Types`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

### Creating an Array
- [func CFArrayCreate(CFAllocator!, UnsafeMutablePointer<UnsafeRawPointer?>!, CFIndex, UnsafePointer<CFArrayCallBacks>!) -> CFArray!](cfarraycreate(_:_:_:_:).md)
  Creates a new immutable array with the given values.
- [func CFArrayCreateCopy(CFAllocator!, CFArray!) -> CFArray!](cfarraycreatecopy(_:_:).md)
  Creates a new immutable array with the values from another array.
### Examining an Array
- [func CFArrayBSearchValues(CFArray!, CFRange, UnsafeRawPointer!, CFComparatorFunction!, UnsafeMutableRawPointer!) -> CFIndex](cfarraybsearchvalues(_:_:_:_:_:).md)
  Searches an array for a value using a binary search algorithm.
- [func CFArrayContainsValue(CFArray!, CFRange, UnsafeRawPointer!) -> Bool](cfarraycontainsvalue(_:_:_:).md)
  Reports whether or not a value is in an array.
- [func CFArrayGetCount(CFArray!) -> CFIndex](cfarraygetcount(_:).md)
  Returns the number of values currently in an array.
- [func CFArrayGetCountOfValue(CFArray!, CFRange, UnsafeRawPointer!) -> CFIndex](cfarraygetcountofvalue(_:_:_:).md)
  Counts the number of times a given value occurs in an array.
- [func CFArrayGetFirstIndexOfValue(CFArray!, CFRange, UnsafeRawPointer!) -> CFIndex](cfarraygetfirstindexofvalue(_:_:_:).md)
  Searches an array forward for a value.
- [func CFArrayGetLastIndexOfValue(CFArray!, CFRange, UnsafeRawPointer!) -> CFIndex](cfarraygetlastindexofvalue(_:_:_:).md)
  Searches an array backward for a value.
- [func CFArrayGetValues(CFArray!, CFRange, UnsafeMutablePointer<UnsafeRawPointer?>!)](cfarraygetvalues(_:_:_:).md)
  Fills a buffer with values from an array.
- [func CFArrayGetValueAtIndex(CFArray!, CFIndex) -> UnsafeRawPointer!](cfarraygetvalueatindex(_:_:).md)
  Retrieves a value at a given index.
### Applying a Function to Elements
- [func CFArrayApplyFunction(CFArray!, CFRange, ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void)!, UnsafeMutableRawPointer!)](cfarrayapplyfunction(_:_:_:_:).md)
  Calls a function once for each element in range in an array.
### Getting the CFArray Type ID
- [func CFArrayGetTypeID() -> CFTypeID](cfarraygettypeid().md)
  Returns the type identifier for the CFArray opaque type.
### Callbacks
- [typealias CFArrayApplierFunction](cfarrayapplierfunction.md)
  Prototype of a callback function that may be applied to every value in an array.
- [typealias CFArrayCopyDescriptionCallBack](cfarraycopydescriptioncallback.md)
  Prototype of a callback function used to get a description of a value in an array.
- [typealias CFArrayEqualCallBack](cfarrayequalcallback.md)
  Prototype of a callback function used to determine if two values in an array are equal.
- [typealias CFArrayReleaseCallBack](cfarrayreleasecallback.md)
  Prototype of a callback function used to release a value before it’s removed from an array.
- [typealias CFArrayRetainCallBack](cfarrayretaincallback.md)
  Prototype of a callback function used to retain a value being added to an array.
### Data Types
- [struct CFArrayCallBacks](cfarraycallbacks.md)
  Structure containing the callbacks of a CFArray.
### Constants
- [Predefined Callback Structures](predefined-callback-structures.md)
  CFArray provides a predefined callback structure appropriate for use when the values in a CFArray are all CFType-derived objects.

## Relationships

### Inherited By
- [CFMutableArray](cfmutablearray.md)
### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Property List Programming Topics for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
- [Collections Programming Topics for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/CFCollections.html#//apple_ref/doc/uid/10000124i)
- [class CFAllocator](cfallocator.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)
- [class CFFileDescriptor](cffiledescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarray)*