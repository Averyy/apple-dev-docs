# CFMutableCharacterSet

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
class CFMutableCharacterSet
```

#### Overview

CFMutableCharacterSet manages dynamic character sets. The basic interface for managing character sets is provided by [`CFCharacterSet`](cfcharacterset.md). CFMutableCharacterSet adds functions to modify the contents of a character set.

You create a mutable character set object using either the [`CFCharacterSetCreateMutable(_:)`](cfcharactersetcreatemutable(_:).md) or [`CFCharacterSetCreateMutableCopy(_:_:)`](cfcharactersetcreatemutablecopy(_:_:).md) function.

CFMutableCharacterSet is “toll-free bridged” with its Cocoa Foundation counterpart, [`NSMutableCharacterSet`](https://developer.apple.com/documentation/Foundation/NSMutableCharacterSet). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSMutableCharacterSet *` parameter, you can pass in a `CFMutableCharacterSetRef`, and in a function where you see a `CFMutableCharacterSetRef` parameter, you can pass in an NSMutableCharacterSet instance. This capability also applies to concrete subclasses of NSMutableCharacterSet. See [`Toll-Free Bridged Types`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

### Creating a Mutable Character Set
- [func CFCharacterSetCreateMutable(CFAllocator!) -> CFMutableCharacterSet!](cfcharactersetcreatemutable(_:).md)
  Creates a new empty mutable character set.
- [func CFCharacterSetCreateMutableCopy(CFAllocator!, CFCharacterSet!) -> CFMutableCharacterSet!](cfcharactersetcreatemutablecopy(_:_:).md)
  Creates a new mutable character set with the values from another character set.
### Adding Characters
- [func CFCharacterSetAddCharactersInRange(CFMutableCharacterSet!, CFRange)](cfcharactersetaddcharactersinrange(_:_:).md)
  Adds a given range to a character set.
- [func CFCharacterSetAddCharactersInString(CFMutableCharacterSet!, CFString!)](cfcharactersetaddcharactersinstring(_:_:).md)
  Adds the characters in a given string to a character set.
### Removing Characters
- [func CFCharacterSetRemoveCharactersInRange(CFMutableCharacterSet!, CFRange)](cfcharactersetremovecharactersinrange(_:_:).md)
  Removes a given range of Unicode characters from a character set.
- [func CFCharacterSetRemoveCharactersInString(CFMutableCharacterSet!, CFString!)](cfcharactersetremovecharactersinstring(_:_:).md)
  Removes the characters in a given string from a character set.
### Logical Operations
- [func CFCharacterSetIntersect(CFMutableCharacterSet!, CFCharacterSet!)](cfcharactersetintersect(_:_:).md)
  Forms an intersection of two character sets.
- [func CFCharacterSetInvert(CFMutableCharacterSet!)](cfcharactersetinvert(_:).md)
  Inverts the content of a given character set.
- [func CFCharacterSetUnion(CFMutableCharacterSet!, CFCharacterSet!)](cfcharactersetunion(_:_:).md)
  Forms the union of two character sets.

## Relationships

### Inherits From
- [CFCharacterSet](cfcharacterset.md)
### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [String Programming Guide for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/introCFStrings.html#//apple_ref/doc/uid/10000131i)
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmutablecharacterset)*