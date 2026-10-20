# CFAttributedString

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
class CFAttributedString
```

```c
typedef const struct __CFAttributedString * CFAttributedStringRef;
```

#### Overview

Instances of CFAttributedString manage character strings and associated sets of attributes (for example, font and kerning information) that apply to individual characters or ranges of characters in the string. CFAttributedString as defined in Core Foundation provides the basic container functionality, while higher levels provide definitions for standard attributes, their values, and additional behaviors involving these. CFAttributedString represents an immutable string—use [`CFMutableAttributedString`](./cfmutableattributedstring.md) to create and manage an attributed string that can be changed after it has been created.

CFAttributedString is not a “subclass” of CFString; that is, it does not respond to CFString function calls. CFAttributedString conceptually contains a CFString to which it applies attributes. This protects you from ambiguities caused by the semantic differences between simple and attributed string.

Attributes are identified by key/value pairs stored in CFDictionary objects. Keys must be CFString objects, while the corresponding values are CFType objects of an appropriate type. See the attribute constants in NSAttributedString Application Kit Additions Reference or NSAttributedString UIKit Additions Reference for standard attribute names.

> ❗ **Important**:  Attribute dictionaries set for an attributed string must always be created with [`kCFCopyStringDictionaryKeyCallBacks`](./kcfcopystringdictionarykeycallbacks.md) for their dictionary key callbacks and [`kCFTypeDictionaryValueCallBacks`](./kcftypedictionaryvaluecallbacks.md) for their value callbacks; otherwise it’s an error.

CFAttributedString is “toll-free bridged” with its Foundation counterpart, [`NSAttributedString`](../Foundation/nsattributedstring.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSAttributedString *` parameter, you can pass in a `CFAttributedStringRef`, and in a function where you see a `CFAttributedStringRef` parameter, you can pass in an [`NSAttributedString`](../Foundation/nsattributedstring.md) instance. This also applies to concrete subclasses of [`NSAttributedString`](../Foundation/nsattributedstring.md). See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

### Creating a CFAttributedString
- [func CFAttributedStringCreate(CFAllocator!, CFString!, CFDictionary!) -> CFAttributedString!](./cfattributedstringcreate%28_,_,_%29.md)
  Creates an attributed string with specified string and attributes.
- [func CFAttributedStringCreateCopy(CFAllocator!, CFAttributedString!) -> CFAttributedString!](./cfattributedstringcreatecopy%28_,_%29.md)
  Creates an immutable copy of an attributed string.
- [func CFAttributedStringCreateWithSubstring(CFAllocator!, CFAttributedString!, CFRange) -> CFAttributedString!](./cfattributedstringcreatewithsubstring%28_,_,_%29.md)
  Creates a sub-attributed string from the specified range.
- [func CFAttributedStringGetLength(CFAttributedString!) -> CFIndex](./cfattributedstringgetlength%28_%29.md)
  Returns the length of the attributed string in characters.
- [func CFAttributedStringGetString(CFAttributedString!) -> CFString!](./cfattributedstringgetstring%28_%29.md)
  Returns the string for an attributed string.
### Accessing Attributes
- [func CFAttributedStringGetAttribute(CFAttributedString!, CFIndex, CFString!, UnsafeMutablePointer<CFRange>!) -> CFTypeRef!](./cfattributedstringgetattribute%28_,_,_,_%29.md)
  Returns the value of a given attribute of an attributed string at a specified location.
- [func CFAttributedStringGetAttributes(CFAttributedString!, CFIndex, UnsafeMutablePointer<CFRange>!) -> CFDictionary!](./cfattributedstringgetattributes%28_,_,_%29.md)
  Returns the attributes of an attributed string at a specified location.
- [func CFAttributedStringGetAttributeAndLongestEffectiveRange(CFAttributedString!, CFIndex, CFString!, CFRange, UnsafeMutablePointer<CFRange>!) -> CFTypeRef!](./cfattributedstringgetattributeandlongesteffectiverange%28_,_,_,_,_%29.md)
  Returns the value of a given attribute of an attributed string at a specified location.
- [func CFAttributedStringGetAttributesAndLongestEffectiveRange(CFAttributedString!, CFIndex, CFRange, UnsafeMutablePointer<CFRange>!) -> CFDictionary!](./cfattributedstringgetattributesandlongesteffectiverange%28_,_,_,_%29.md)
  Returns the attributes of an attributed string at a specified location.
### Getting Attributed String Properties
- [func CFAttributedStringGetTypeID() -> CFTypeID](./cfattributedstringgettypeid%28%29.md)
  Returns the type identifier for the CFAttributedString opaque type.

## Relationships

### Inherited By
- [CFMutableAttributedString](./cfmutableattributedstring.md)
### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Related Documentation
- [Property List Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
- [String Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/introCFStrings.html#//apple_ref/doc/uid/10000131i)
- [Data Formatting Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDataFormatting/Articles/CFDataFormatting.html#//apple_ref/doc/uid/10000176i)
### Opaque Types
- [class CFAllocator](./cfallocator.md)
- [class CFArray](./cfarray.md)
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
- [class CFFileDescriptor](./cffiledescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstring)*