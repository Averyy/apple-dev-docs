# CFMutableCharacterSet

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
class CFMutableCharacterSet
```

```c
typedef struct __CFCharacterSet * CFMutableCharacterSetRef;
```

## Overview

CFMutableCharacterSet manages dynamic character sets. The basic interface for managing character sets is provided by [`CFCharacterSet`](./cfcharacterset.md). CFMutableCharacterSet adds functions to modify the contents of a character set.

You create a mutable character set object using either the [`CFCharacterSetCreateMutable(_:)`](./cfcharactersetcreatemutable%28_%29.md) or [`CFCharacterSetCreateMutableCopy(_:_:)`](./cfcharactersetcreatemutablecopy%28_,_%29.md) function.

CFMutableCharacterSet is “toll-free bridged” with its Cocoa Foundation counterpart, [`NSMutableCharacterSet`](../Foundation/nsmutablecharacterset.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSMutableCharacterSet *` parameter, you can pass in a `CFMutableCharacterSetRef`, and in a function where you see a `CFMutableCharacterSetRef` parameter, you can pass in an NSMutableCharacterSet instance. This capability also applies to concrete subclasses of NSMutableCharacterSet. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

### Creating a Mutable Character Set
- [func CFCharacterSetCreateMutable(CFAllocator!) -> CFMutableCharacterSet!](./cfcharactersetcreatemutable%28_%29.md)
  Creates a new empty mutable character set.
- [func CFCharacterSetCreateMutableCopy(CFAllocator!, CFCharacterSet!) -> CFMutableCharacterSet!](./cfcharactersetcreatemutablecopy%28_,_%29.md)
  Creates a new mutable character set with the values from another character set.
### Adding Characters
- [func CFCharacterSetAddCharactersInRange(CFMutableCharacterSet!, CFRange)](./cfcharactersetaddcharactersinrange%28_,_%29.md)
  Adds a given range to a character set.
- [func CFCharacterSetAddCharactersInString(CFMutableCharacterSet!, CFString!)](./cfcharactersetaddcharactersinstring%28_,_%29.md)
  Adds the characters in a given string to a character set.
### Removing Characters
- [func CFCharacterSetRemoveCharactersInRange(CFMutableCharacterSet!, CFRange)](./cfcharactersetremovecharactersinrange%28_,_%29.md)
  Removes a given range of Unicode characters from a character set.
- [func CFCharacterSetRemoveCharactersInString(CFMutableCharacterSet!, CFString!)](./cfcharactersetremovecharactersinstring%28_,_%29.md)
  Removes the characters in a given string from a character set.
### Logical Operations
- [func CFCharacterSetIntersect(CFMutableCharacterSet!, CFCharacterSet!)](./cfcharactersetintersect%28_,_%29.md)
  Forms an intersection of two character sets.
- [func CFCharacterSetInvert(CFMutableCharacterSet!)](./cfcharactersetinvert%28_%29.md)
  Inverts the content of a given character set.
- [func CFCharacterSetUnion(CFMutableCharacterSet!, CFCharacterSet!)](./cfcharactersetunion%28_,_%29.md)
  Forms the union of two character sets.

## Relationships

### Inherits From
- [CFCharacterSet](./cfcharacterset.md)
### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Related Documentation
- [String Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/introCFStrings.html#//apple_ref/doc/uid/10000131i)
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmutablecharacterset)*