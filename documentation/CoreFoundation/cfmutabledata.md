# CFMutableData

**Framework**: Core Foundation  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class CFMutableData
```

```c
typedef struct __CFData * CFMutableDataRef;
```

## Overview

CFMutableData manages dynamic binary data. The basic interface for managing binary data is provided by [`CFData`](./cfdata.md). CFMutableData adds functions to modify the contents of a binary data object.

You create a mutable data object using either the [`CFDataCreateMutable(_:_:)`](./cfdatacreatemutable%28_,_%29.md) or [`CFDataCreateMutableCopy(_:_:_:)`](./cfdatacreatemutablecopy%28_,_,_%29.md) function.

Bytes are added to a data object with the [`CFDataAppendBytes(_:_:_:)`](./cfdataappendbytes%28_,_,_%29.md) function. Bytes are removed from a data object with the [`CFDataDeleteBytes(_:_:)`](./cfdatadeletebytes%28_,_%29.md) function.

> ❗ **Important**:  Many of the CFMutableData functions take a [`CFIndex`](./cfindex.md) `length` or `capacity` argument. You must not pass a negative number for such values—this may introduce a security risk.

CFMutableData is “toll-free bridged” with its Cocoa Foundation counterpart, [`NSMutableData`](../Foundation/nsmutabledata.md). What this means is that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. In other words, in a method where you see an `NSMutableData *` parameter, you can pass in a `CFMutableDataRef`, and in a function where you see a `CFMutableDataRef` parameter, you can pass in an `NSMutableData` instance. This also applies to concrete subclasses of `NSMutableData`. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

### Creating a Mutable Data Object
- [func CFDataCreateMutable(CFAllocator!, CFIndex) -> CFMutableData!](./cfdatacreatemutable%28_,_%29.md)
  Creates an empty CFMutableData object.
- [func CFDataCreateMutableCopy(CFAllocator!, CFIndex, CFData!) -> CFMutableData!](./cfdatacreatemutablecopy%28_,_,_%29.md)
  Creates a CFMutableData object by copying another CFData object.
### Accessing Data
- [func CFDataGetMutableBytePtr(CFMutableData!) -> UnsafeMutablePointer<UInt8>!](./cfdatagetmutablebyteptr%28_%29.md)
  Returns a pointer to a mutable byte buffer of a CFMutableData object.
### Modifying a Mutable Data Object
- [func CFDataAppendBytes(CFMutableData!, UnsafePointer<UInt8>!, CFIndex)](./cfdataappendbytes%28_,_,_%29.md)
  Appends the bytes from a byte buffer to the contents of a CFData object.
- [func CFDataDeleteBytes(CFMutableData!, CFRange)](./cfdatadeletebytes%28_,_%29.md)
  Deletes the bytes in a CFMutableData object within a specified range.
- [func CFDataReplaceBytes(CFMutableData!, CFRange, UnsafePointer<UInt8>!, CFIndex)](./cfdatareplacebytes%28_,_,_,_%29.md)
  Replaces those bytes in a CFMutableData object that fall within a specified range with other bytes.
- [func CFDataIncreaseLength(CFMutableData!, CFIndex)](./cfdataincreaselength%28_,_%29.md)
  Increases the length of a CFMutableData object’s internal byte buffer, zero-filling the extension to the buffer.
- [func CFDataSetLength(CFMutableData!, CFIndex)](./cfdatasetlength%28_,_%29.md)
  Resets the length of a CFMutableData object’s internal byte buffer.

## Relationships

### Inherits From
- [CFData](./cfdata.md)
### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Related Documentation
- [Property List Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
- [Binary Data Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBinaryData/CFBinaryData.html#//apple_ref/doc/uid/10000144i)
### Opaque Types
- [class CFAllocator](./cfallocator.md)
- [class CFArray](./cfarray.md)
- [class CFAttributedString](./cfattributedstring.md)
- [class CFBag](./cfbag.md)
- [class CFBinaryHeap](./cfbinaryheap.md)
- [class CFBitVector](./cfbitvector.md)
- [class CFBoolean](./cfboolean.md)
- [class CFBundle](./cfbundle.md)
- [class CFCalendar](./cfcalendar.md)
- [class CFCharacterSet](./cfcharacterset.md)
- [class CFData](./cfdata.md)
- [class CFDate](./cfdate.md)
- [class CFDateFormatter](./cfdateformatter.md)
- [class CFDictionary](./cfdictionary.md)
- [class CFError](./cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmutabledata)*