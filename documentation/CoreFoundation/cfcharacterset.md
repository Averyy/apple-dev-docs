# CFCharacterSet

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
class CFCharacterSet
```

#### Overview

A CFCharacterSet object represents a set of Unicode compliant characters. CFString uses CFCharacterSet objects to group characters together for searching operations, so that they can find any of a particular set of characters during a search. The two opaque types, CFCharacterSet and [`CFMutableCharacterSet`](cfmutablecharacterset.md), define the interface for static and dynamic character sets, respectively. The objects you create using these opaque types are referred to as character set objects (and when no confusion will result, merely as character sets).

CFCharacterSet’s principal function, [`CFCharacterSetIsCharacterMember(_:_:)`](cfcharactersetischaractermember(_:_:).md), provides the basis for all other functions in its interface. You create a character set using one of the `CFCharacterSetCreate...` functions. You may also use any one of the predefined character sets using the [`CFCharacterSetGetPredefined(_:)`](cfcharactersetgetpredefined(_:).md) function.

CFCharacterSet is “toll-free bridged” with its Cocoa Foundation counterpart, [`NSCharacterSet`](https://developer.apple.com/documentation/Foundation/NSCharacterSet). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSCharacterSet *` parameter, you can pass in a `CFCharacterSetRef`, and in a function where you see a `CFCharacterSetRef` parameter, you can pass in an NSCharacterSet instance. This capability also applies to concrete subclasses of NSCharacterSet. See [`Toll-Free Bridged Types`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

### Creating Character Sets
- [func CFCharacterSetCreateCopy(CFAllocator!, CFCharacterSet!) -> CFCharacterSet!](cfcharactersetcreatecopy(_:_:).md)
  Creates a new character set with the values from a given character set.
- [func CFCharacterSetCreateInvertedSet(CFAllocator!, CFCharacterSet!) -> CFCharacterSet!](cfcharactersetcreateinvertedset(_:_:).md)
  Creates a new immutable character set that is the invert of the specified character set.
- [func CFCharacterSetCreateWithCharactersInRange(CFAllocator!, CFRange) -> CFCharacterSet!](cfcharactersetcreatewithcharactersinrange(_:_:).md)
  Creates a new character set with the values from the given range of Unicode characters.
- [func CFCharacterSetCreateWithCharactersInString(CFAllocator!, CFString!) -> CFCharacterSet!](cfcharactersetcreatewithcharactersinstring(_:_:).md)
  Creates a new character set with the values in the given string.
- [func CFCharacterSetCreateWithBitmapRepresentation(CFAllocator!, CFData!) -> CFCharacterSet!](cfcharactersetcreatewithbitmaprepresentation(_:_:).md)
  Creates a new immutable character set with the bitmap representation specified by given data.
### Getting Predefined Character Sets
- [func CFCharacterSetGetPredefined(CFCharacterSetPredefinedSet) -> CFCharacterSet!](cfcharactersetgetpredefined(_:).md)
  Returns a predefined character set.
### Querying Character Sets
- [func CFCharacterSetCreateBitmapRepresentation(CFAllocator!, CFCharacterSet!) -> CFData!](cfcharactersetcreatebitmaprepresentation(_:_:).md)
  Creates a new immutable data with the bitmap representation from the given character set.
- [func CFCharacterSetHasMemberInPlane(CFCharacterSet!, CFIndex) -> Bool](cfcharactersethasmemberinplane(_:_:).md)
  Reports whether or not a character set contains at least one member character in the specified plane.
- [func CFCharacterSetIsCharacterMember(CFCharacterSet!, UniChar) -> Bool](cfcharactersetischaractermember(_:_:).md)
  Reports whether or not a given Unicode character is in a character set.
- [func CFCharacterSetIsLongCharacterMember(CFCharacterSet!, UTF32Char) -> Bool](cfcharactersetislongcharactermember(_:_:).md)
  Reports whether or not a given UTF-32 character is in a character set.
- [func CFCharacterSetIsSupersetOfSet(CFCharacterSet!, CFCharacterSet!) -> Bool](cfcharactersetissupersetofset(_:_:).md)
  Reports whether or not a character set is a superset of another set.
### Getting the Character Set Type Identifier
- [func CFCharacterSetGetTypeID() -> CFTypeID](cfcharactersetgettypeid().md)
  Returns the type identifier of the CFCharacterSet opaque type.
### Data Types
- [enum CFCharacterSetPredefinedSet](cfcharactersetpredefinedset.md)
  Defines a predefined character set.
### Constants
- [Predefined CFCharacterSet Selector Values](predefined_cfcharacterset_selector_values.md)
  Identifiers for the available predefined CFCharacterSet objects.

## Relationships

### Inherited By
- [CFMutableCharacterSet](cfmutablecharacterset.md)
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
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)
- [class CFFileDescriptor](cffiledescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcharacterset)*