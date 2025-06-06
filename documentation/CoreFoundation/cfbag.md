# CFBag

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
class CFBag
```

#### Overview

CFBag and its derived mutable type, [`CFMutableBag`](cfmutablebag.md), manage non-sequential collections of values called bags in which there can be duplicate values. CFBag creates static bags and CFMutableBag creates dynamic bags.

Use bags or sets as an alternative to arrays when the order of elements isn’t important and performance in testing whether a value is contained in the collection is a consideration—while arrays are ordered, testing for membership is slower than with bags or sets. Use bags over sets if you want to allow duplicate values in your collections.

You create a static bag object using either the [`CFBagCreate(_:_:_:_:)`](cfbagcreate(_:_:_:_:).md) or [`CFBagCreateCopy(_:_:)`](cfbagcreatecopy(_:_:).md) function. These functions return a bag containing the values you pass in as arguments. (Note that bags can’t contain `NULL` pointers; in most cases, though, you can use the kCFNull constant instead.) Values are not copied but retained using the retain callback provided when the bag was created. Similarly, when a value is removed from a bag, it is released using the release callback.

CFBag provides functions for querying the values of a bag. The [`CFBagGetCount(_:)`](cfbaggetcount(_:).md) returns the number of values in a bag, the [`CFBagContainsValue(_:_:)`](cfbagcontainsvalue(_:_:).md) function checks if a value is in a bag, and [`CFBagGetValues(_:_:)`](cfbaggetvalues(_:_:).md) returns a C array containing all the values in a bag.

The [`CFBagApplyFunction(_:_:_:)`](cfbagapplyfunction(_:_:_:).md) function lets you apply a function to all values in a bag.

## Topics

### Creating a Bag
- [func CFBagCreate(CFAllocator!, UnsafeMutablePointer<UnsafeRawPointer?>!, CFIndex, UnsafePointer<CFBagCallBacks>!) -> CFBag!](cfbagcreate(_:_:_:_:).md)
  Creates an immutable bag containing specified values.
- [func CFBagCreateCopy(CFAllocator!, CFBag!) -> CFBag!](cfbagcreatecopy(_:_:).md)
  Creates an immutable bag with the values of another bag.
### Examining a Bag
- [func CFBagContainsValue(CFBag!, UnsafeRawPointer!) -> Bool](cfbagcontainsvalue(_:_:).md)
  Reports whether or not a value is in a bag.
- [func CFBagGetCount(CFBag!) -> CFIndex](cfbaggetcount(_:).md)
  Returns the number of values currently in a bag.
- [func CFBagGetCountOfValue(CFBag!, UnsafeRawPointer!) -> CFIndex](cfbaggetcountofvalue(_:_:).md)
  Returns the number of times a value occurs in a bag.
- [func CFBagGetValue(CFBag!, UnsafeRawPointer!) -> UnsafeRawPointer!](cfbaggetvalue(_:_:).md)
  Returns a requested value from a bag.
- [func CFBagGetValueIfPresent(CFBag!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](cfbaggetvalueifpresent(_:_:_:).md)
  Reports whether or not a value is in a bag, and returns that value indirectly if it exists.
- [func CFBagGetValues(CFBag!, UnsafeMutablePointer<UnsafeRawPointer?>!)](cfbaggetvalues(_:_:).md)
  Fills a buffer with values from a bag.
### Applying a Function to the Contents of a Bag
- [func CFBagApplyFunction(CFBag!, ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void)!, UnsafeMutableRawPointer!)](cfbagapplyfunction(_:_:_:).md)
  Calls a function once for each value in a bag.
### Getting the CFBag Type ID
- [func CFBagGetTypeID() -> CFTypeID](cfbaggettypeid().md)
  Returns the type identifier for the CFBag opaque type.
### Callbacks
- [typealias CFBagApplierFunction](cfbagapplierfunction.md)
  Prototype of a callback function that may be applied to every value in a bag.
- [typealias CFBagCopyDescriptionCallBack](cfbagcopydescriptioncallback.md)
  Prototype of a callback function used to get a description of a value in a bag.
- [typealias CFBagEqualCallBack](cfbagequalcallback.md)
  Prototype of a callback function used to determine if two values in a bag are equal.
- [typealias CFBagHashCallBack](cfbaghashcallback.md)
  Prototype of a callback function invoked to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.
- [typealias CFBagReleaseCallBack](cfbagreleasecallback.md)
  Prototype of a callback function used to release a value before it’s removed from a bag.
- [typealias CFBagRetainCallBack](cfbagretaincallback.md)
  Prototype of a callback function used to retain a value being added to a bag.
### Data Types
- [struct CFBagCallBacks](cfbagcallbacks.md)
  This structure contains the callbacks used to retain, release, describe, and compare the values of a CFBag object.
### Constants
- [Predefined Callback Structures](cfbag-predefined-callback-structures.md)
  CFBag provides some predefined callbacks for your convenience.

## Relationships

### Inherited By
- [CFMutableBag](cfmutablebag.md)
### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Collections Programming Topics for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/CFCollections.html#//apple_ref/doc/uid/10000124i)
- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbag)*