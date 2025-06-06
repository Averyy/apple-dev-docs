# CFMutableSet

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
class CFMutableSet
```

#### Overview

CFMutableSet manages dynamic sets. The basic interface for managing sets is provided by [`CFSet`](cfset.md). CFMutableSet adds functions to modify the contents of a set.

You create a mutable set object using either the [`CFSetCreateMutable(_:_:_:)`](cfsetcreatemutable(_:_:_:).md) or [`CFSetCreateMutableCopy(_:_:_:)`](cfsetcreatemutablecopy(_:_:_:).md) function.

CFMutableSet provides several functions for adding and removing values from a set. The [`CFSetAddValue(_:_:)`](cfsetaddvalue(_:_:).md) function adds a value to a set and [`CFSetRemoveValue(_:_:)`](cfsetremovevalue(_:_:).md) removes a value from a set.

CFMutableSet is “toll-free bridged” with its Cocoa Foundation counterpart, [`NSMutableSet`](https://developer.apple.com/documentation/Foundation/NSMutableSet). What this means is that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. This means that in a method where you see an `NSMutableSet *` parameter, you can pass in a `CFMutableSetRef`, and in a function where you see a `CFMutableSetRef` parameter, you can pass in an NSMutableSet instance. This also applies to concrete subclasses of NSMutableSet. See [`Toll-Free Bridged Types`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

### CFMutableSet Miscellaneous Functions
- [func CFSetAddValue(CFMutableSet!, UnsafeRawPointer!)](cfsetaddvalue(_:_:).md)
  Adds a value to a CFMutableSet object.
- [func CFSetCreateMutable(CFAllocator!, CFIndex, UnsafePointer<CFSetCallBacks>!) -> CFMutableSet!](cfsetcreatemutable(_:_:_:).md)
  Creates an empty CFMutableSet object.
- [func CFSetCreateMutableCopy(CFAllocator!, CFIndex, CFSet!) -> CFMutableSet!](cfsetcreatemutablecopy(_:_:_:).md)
  Creates a new mutable set with the values from another set.
- [func CFSetRemoveAllValues(CFMutableSet!)](cfsetremoveallvalues(_:).md)
  Removes all values from a CFMutableSet object.
- [func CFSetRemoveValue(CFMutableSet!, UnsafeRawPointer!)](cfsetremovevalue(_:_:).md)
  Removes a value from a CFMutableSet object.
- [func CFSetReplaceValue(CFMutableSet!, UnsafeRawPointer!)](cfsetreplacevalue(_:_:).md)
  Replaces a value in a CFMutableSet object.
- [func CFSetSetValue(CFMutableSet!, UnsafeRawPointer!)](cfsetsetvalue(_:_:).md)
  Sets a value in a CFMutableSet object.

## Relationships

### Inherits From
- [CFSet](cfset.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmutableset)*