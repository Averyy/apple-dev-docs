# CFData

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
class CFData
```

```c
typedef const struct __CFData * CFDataRef;
```

## Overview

CFData and its derived mutable type, [`CFMutableData`](./cfmutabledata.md), provide support for data objects, object-oriented wrappers for byte buffers. Data objects let simple allocated buffers (that is, data with no embedded pointers) take on the behavior of Core Foundation objects. CFData creates static data objects, and CFMutableData creates dynamic data objects. Data objects are typically used for raw data storage.

You use the [`CFDataCreate(_:_:_:)`](./cfdatacreate%28_,_,_%29.md) and [`CFDataCreateCopy(_:_:)`](./cfdatacreatecopy%28_,_%29.md) functions to create static data objects. These functions make a new copy of the supplied data. To create a data object that uses the supplied buffer instead of making a separate copy, use the [`CFDataCreateWithBytesNoCopy(_:_:_:_:)`](./cfdatacreatewithbytesnocopy%28_,_,_,_%29.md) function. You use the [`CFDataGetBytes(_:_:_:)`](./cfdatagetbytes%28_,_,_%29.md) function to retrieve the bytes and the [`CFDataGetLength(_:)`](./cfdatagetlength%28_%29.md) function to get the length of the bytes.

CFData is “toll-free bridged” with its Cocoa Foundation counterpart, [`NSData`](../Foundation/nsdata.md). What this means is that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. In other words, in a method where you see an `NSData *` parameter, you can pass in a `CFDataRef`, and in a function where you see a `CFDataRef` parameter, you can pass in an `NSData` instance. This also applies to concrete subclasses of `NSData`. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

### Creating a CFData Object
- [func CFDataCreate(CFAllocator!, UnsafePointer<UInt8>!, CFIndex) -> CFData!](./cfdatacreate%28_,_,_%29.md)
  Creates an immutable CFData object using data copied from a specified byte buffer.
- [func CFDataCreateCopy(CFAllocator!, CFData!) -> CFData!](./cfdatacreatecopy%28_,_%29.md)
  Creates an immutable copy of a CFData object.
- [func CFDataCreateWithBytesNoCopy(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, CFAllocator!) -> CFData!](./cfdatacreatewithbytesnocopy%28_,_,_,_%29.md)
  Creates an immutable CFData object from an external (client-owned) byte buffer.
### Examining a CFData Object
- [func CFDataGetBytePtr(CFData!) -> UnsafePointer<UInt8>!](./cfdatagetbyteptr%28_%29.md)
  Returns a read-only pointer to the bytes of a CFData object.
- [func CFDataGetBytes(CFData!, CFRange, UnsafeMutablePointer<UInt8>!)](./cfdatagetbytes%28_,_,_%29.md)
  Copies the byte contents of a CFData object to an external buffer.
- [func CFDataGetLength(CFData!) -> CFIndex](./cfdatagetlength%28_%29.md)
  Returns the number of bytes contained by a CFData object.
- [func CFDataFind(CFData!, CFData!, CFRange, CFDataSearchFlags) -> CFRange](./cfdatafind%28_,_,_,_%29.md)
  Finds and returns the range within a data object of the first occurrence of the given data, within a given range, subject to any given options.
### Getting the CFData Type ID
- [func CFDataGetTypeID() -> CFTypeID](./cfdatagettypeid%28%29.md)
  Returns the type identifier for the CFData opaque type.
### Data Types
- [struct CFDataSearchFlags](./cfdatasearchflags.md)
  A [`CFOptionFlags`](./cfoptionflags.md) type for specifying options for searching.

## Relationships

### Inherited By
- [CFMutableData](./cfmutabledata.md)
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
- [class CFDate](./cfdate.md)
- [class CFDateFormatter](./cfdateformatter.md)
- [class CFDictionary](./cfdictionary.md)
- [class CFError](./cferror.md)
- [class CFFileDescriptor](./cffiledescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdata)*