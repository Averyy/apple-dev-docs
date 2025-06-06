# CFAttributedString

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
class CFAttributedString
```

#### Overview

Instances of CFAttributedString manage character strings and associated sets of attributes (for example, font and kerning information) that apply to individual characters or ranges of characters in the string. CFAttributedString as defined in Core Foundation provides the basic container functionality, while higher levels provide definitions for standard attributes, their values, and additional behaviors involving these. CFAttributedString represents an immutable string—use [`CFMutableAttributedString`](cfmutableattributedstring.md) to create and manage an attributed string that can be changed after it has been created.

CFAttributedString is not a “subclass” of CFString; that is, it does not respond to CFString function calls. CFAttributedString conceptually contains a CFString to which it applies attributes. This protects you from ambiguities caused by the semantic differences between simple and attributed string.

Attributes are identified by key/value pairs stored in CFDictionary objects. Keys must be CFString objects, while the corresponding values are CFType objects of an appropriate type. See the attribute constants in NSAttributedString Application Kit Additions Reference or NSAttributedString UIKit Additions Reference for standard attribute names.

> ❗ **Important**:  Attribute dictionaries set for an attributed string must always be created with [`kCFCopyStringDictionaryKeyCallBacks`](kcfcopystringdictionarykeycallbacks.md) for their dictionary key callbacks and [`kCFTypeDictionaryValueCallBacks`](kcftypedictionaryvaluecallbacks.md) for their value callbacks; otherwise it’s an error.

 Attribute dictionaries set for an attributed string must always be created with [`kCFCopyStringDictionaryKeyCallBacks`](kcfcopystringdictionarykeycallbacks.md) for their dictionary key callbacks and [`kCFTypeDictionaryValueCallBacks`](kcftypedictionaryvaluecallbacks.md) for their value callbacks; otherwise it’s an error.

CFAttributedString is “toll-free bridged” with its Foundation counterpart, [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSAttributedString *` parameter, you can pass in a `CFAttributedStringRef`, and in a function where you see a `CFAttributedStringRef` parameter, you can pass in an [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) instance. This also applies to concrete subclasses of [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString). See [`Toll-Free Bridged Types`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

### Creating a CFAttributedString
- [func CFAttributedStringCreate(CFAllocator!, CFString!, CFDictionary!) -> CFAttributedString!](cfattributedstringcreate(_:_:_:).md)
  Creates an attributed string with specified string and attributes.
- [func CFAttributedStringCreateCopy(CFAllocator!, CFAttributedString!) -> CFAttributedString!](cfattributedstringcreatecopy(_:_:).md)
  Creates an immutable copy of an attributed string.
- [func CFAttributedStringCreateWithSubstring(CFAllocator!, CFAttributedString!, CFRange) -> CFAttributedString!](cfattributedstringcreatewithsubstring(_:_:_:).md)
  Creates a sub-attributed string from the specified range.
- [func CFAttributedStringGetLength(CFAttributedString!) -> CFIndex](cfattributedstringgetlength(_:).md)
  Returns the length of the attributed string in characters.
- [func CFAttributedStringGetString(CFAttributedString!) -> CFString!](cfattributedstringgetstring(_:).md)
  Returns the string for an attributed string.
### Accessing Attributes
- [func CFAttributedStringGetAttribute(CFAttributedString!, CFIndex, CFString!, UnsafeMutablePointer<CFRange>!) -> CFTypeRef!](cfattributedstringgetattribute(_:_:_:_:).md)
  Returns the value of a given attribute of an attributed string at a specified location.
- [func CFAttributedStringGetAttributes(CFAttributedString!, CFIndex, UnsafeMutablePointer<CFRange>!) -> CFDictionary!](cfattributedstringgetattributes(_:_:_:).md)
  Returns the attributes of an attributed string at a specified location.
- [func CFAttributedStringGetAttributeAndLongestEffectiveRange(CFAttributedString!, CFIndex, CFString!, CFRange, UnsafeMutablePointer<CFRange>!) -> CFTypeRef!](cfattributedstringgetattributeandlongesteffectiverange(_:_:_:_:_:).md)
  Returns the value of a given attribute of an attributed string at a specified location.
- [func CFAttributedStringGetAttributesAndLongestEffectiveRange(CFAttributedString!, CFIndex, CFRange, UnsafeMutablePointer<CFRange>!) -> CFDictionary!](cfattributedstringgetattributesandlongesteffectiverange(_:_:_:_:).md)
  Returns the attributes of an attributed string at a specified location.
### Getting Attributed String Properties
- [func CFAttributedStringGetTypeID() -> CFTypeID](cfattributedstringgettypeid().md)
  Returns the type identifier for the CFAttributedString opaque type.

## Relationships

### Inherited By
- [CFMutableAttributedString](cfmutableattributedstring.md)
### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Property List Programming Topics for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
- [String Programming Guide for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/introCFStrings.html#//apple_ref/doc/uid/10000131i)
- [Data Formatting Guide for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDataFormatting/Articles/CFDataFormatting.html#//apple_ref/doc/uid/10000176i)
- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstring)*