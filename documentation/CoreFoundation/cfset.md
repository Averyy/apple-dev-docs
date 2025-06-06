# CFSet

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
class CFSet
```

#### Overview

CFSet and its derived mutable type, [`CFMutableSet`](cfmutableset.md), provide support for the mathematical concept of a set. A set, both in its mathematical sense and in the implementation of CFSet, is an unordered collection of distinct elements. CFSet creates static sets and CFMutableSet creates dynamic sets.

Use bags or sets as an alternative to arrays when the order of elements isn’t important and performance in testing whether a value is contained in the collection is a consideration—while arrays are ordered, testing for membership is slower than with bags or sets. Use bags over sets if you want to allow duplicate values in your collections.

You create a static set object using either the [`CFSetCreate(_:_:_:_:)`](cfsetcreate(_:_:_:_:).md) or [`CFSetCreateCopy(_:_:)`](cfsetcreatecopy(_:_:).md) function. These functions return a set containing the values you pass in as arguments. (Note that sets can’t contain `NULL` pointers; in most cases, though, you can use the [`kCFNull`](kcfnull.md) constant instead.) Values are not copied but retained using the retain callback provided when the set was created. Similarly, when a value is removed from a set, it is released using the release callback.

CFSet provides functions for querying the values of a set. The [`CFSetGetCount(_:)`](cfsetgetcount(_:).md) returns the number of values in a set, the [`CFSetContainsValue(_:_:)`](cfsetcontainsvalue(_:_:).md) function checks if a value is in a set, and [`CFSetGetValues(_:_:)`](cfsetgetvalues(_:_:).md) returns a C array containing all the values in a set.

CFSet is “toll-free bridged” with its Cocoa Foundation counterpart, [`NSSet`](https://developer.apple.com/documentation/Foundation/NSSet). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSSet *` parameter, you can pass in a `CFSetRef`, and in a function where you see a `CFSetRef` parameter, you can pass in an NSSet instance. This also applies to concrete subclasses of NSSet. See [`Toll-Free Bridged Types`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

### Creating Sets
- [func CFSetCreate(CFAllocator!, UnsafeMutablePointer<UnsafeRawPointer?>!, CFIndex, UnsafePointer<CFSetCallBacks>!) -> CFSet!](cfsetcreate(_:_:_:_:).md)
  Creates an immutable CFSet object containing supplied values.
- [func CFSetCreateCopy(CFAllocator!, CFSet!) -> CFSet!](cfsetcreatecopy(_:_:).md)
  Creates an immutable set containing the values of an existing set.
### Examining a Set
- [func CFSetContainsValue(CFSet!, UnsafeRawPointer!) -> Bool](cfsetcontainsvalue(_:_:).md)
  Returns a Boolean that indicates whether a set contains a given value.
- [func CFSetGetCount(CFSet!) -> CFIndex](cfsetgetcount(_:).md)
  Returns the number of values currently in a set.
- [func CFSetGetCountOfValue(CFSet!, UnsafeRawPointer!) -> CFIndex](cfsetgetcountofvalue(_:_:).md)
  Returns the number of values in a set that match a given value.
- [func CFSetGetValue(CFSet!, UnsafeRawPointer!) -> UnsafeRawPointer!](cfsetgetvalue(_:_:).md)
  Obtains a specified value from a set.
- [func CFSetGetValueIfPresent(CFSet!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](cfsetgetvalueifpresent(_:_:_:).md)
  Reports whether or not a value is in a set, and if it exists returns the value indirectly.
- [func CFSetGetValues(CFSet!, UnsafeMutablePointer<UnsafeRawPointer?>!)](cfsetgetvalues(_:_:).md)
  Obtains all values in a set.
### Applying a Function to Set Members
- [func CFSetApplyFunction(CFSet!, ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void)!, UnsafeMutableRawPointer!)](cfsetapplyfunction(_:_:_:).md)
  Calls a function once for each value in a set.
### Getting the CFSet Type ID
- [func CFSetGetTypeID() -> CFTypeID](cfsetgettypeid().md)
  Returns the type identifier for the CFSet type.
### Callbacks
- [typealias CFSetApplierFunction](cfsetapplierfunction.md)
  Prototype of a callback function that may be applied to every value in a set.
- [typealias CFSetCopyDescriptionCallBack](cfsetcopydescriptioncallback.md)
  Prototype of a callback function used to get a description of a value in a set.
- [typealias CFSetEqualCallBack](cfsetequalcallback.md)
  Prototype of a callback function used to determine if two values in a set are equal.
- [typealias CFSetHashCallBack](cfsethashcallback.md)
  Prototype of a callback function called to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.
- [typealias CFSetReleaseCallBack](cfsetreleasecallback.md)
  Prototype of a callback function used to release a value before it’s removed from a set.
- [typealias CFSetRetainCallBack](cfsetretaincallback.md)
  Prototype of a callback function used to retain a value being added to a set.
### Data Types
- [struct CFSetCallBacks](cfsetcallbacks.md)
  This structure contains the callbacks used to retain, release, describe, and compare the values of a CFSet object.
### Constants
- [Predefined Callback Structures](cfset-predefined-callback-structures.md)
  CFSet provides some predefined callbacks for your convenience.

## Relationships

### Inherited By
- [CFMutableSet](cfmutableset.md)
### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Collections Programming Topics for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/CFCollections.html#//apple_ref/doc/uid/10000124i)
- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfset)*