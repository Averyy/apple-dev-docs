# CFMutableAttributedString

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
class CFMutableAttributedString
```

#### Overview

Instances of CFMutableAttributedString manage mutable character strings and associated sets of attributes (for example, font and kerning information) that apply to individual characters or ranges of characters in the string. CFAttributedString as defined in CoreFoundation provides the basic container functionality, while higher levels provide definitions for standard attributes, their values, and additional behaviors involving these. CFMutableAttributedString represents a mutable string—use CFAttributedString to create and manage an attributed string that cannot be changed after it has been created.

CFMutableAttributedString is not a “subclass” of CFMutableString; that is, it does not respond to CFMutableString (or CFString) function calls. CFAttributedString conceptually contains a CFMutableString to which it applies attributes. This protects you from ambiguities caused by the semantic differences between simple and attributed string. Functions defined for CFAttributedString can be applied to a CFMutableAttributedString object.

Attributes are identified by key/value pairs stored in CFDictionary objects. Keys must be CFString objects, while the corresponding values are CFType objects of an appropriate type. See the attribute constants in NSAttributedString Application Kit Additions Reference for standard attribute names in macOS and NSAttributedString UIKit Additions Reference on iOS.

> ❗ **Important**:  Attribute dictionaries set for an attributed string must always be created with kCFCopyStringDictionaryKeyCallbacks for their dictionary key callbacks and kCFTypeDictionaryValueCallBacks for their value callbacks; otherwise it’s an error.

 Attribute dictionaries set for an attributed string must always be created with kCFCopyStringDictionaryKeyCallbacks for their dictionary key callbacks and kCFTypeDictionaryValueCallBacks for their value callbacks; otherwise it’s an error.

When you modify the contents of a mutable attributed string, it may have to do a lot of work to ensure it is internally consistent, and to coalesce runs of identical attributes. You can call [`CFAttributedStringBeginEditing(_:)`](cfattributedstringbeginediting(_:).md) and [`CFAttributedStringEndEditing(_:)`](cfattributedstringendediting(_:).md) around a set of related mutation calls that don’t require the string to be in consistent state in between, and thereby reduce the amount of work necessary. These calls can be nested.

CFMutableAttributedString is “toll-free bridged” with its Foundation counterpart, NSMutableAttributedString. This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSMutableAttributedString *` parameter, you can pass in an object of type `CFMutableAttributedStringRef`, and in a function where you see a `CFMutableAttributedStringRef` parameter, you can pass in an `NSMutableAttributedString` instance. See [`Toll-Free Bridged Types`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

There is not always a 1:1 mapping between `NSMutableAttributedString`‘s methods and CFMutableAttributedString’s functions. For example, to perform an operation equivalent to `NSMutableAttributedString`’s [`append(_:)`](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1417879-append) method on a CFMutableAttributedString object, you can use [`CFAttributedStringReplaceAttributedString(_:_:_:)`](cfattributedstringreplaceattributedstring(_:_:_:).md) and specify `CFRangeMake(CFAttributedStringGetLength(attrStr), 0)` as the range. Alternatively you can cast the CFMutableAttributedString object to an `NSMutableAttributedString` object and send the `appendAttributedString:` message.

## Topics

### Creating a CFMutableAttributedString
- [func CFAttributedStringCreateMutable(CFAllocator!, CFIndex) -> CFMutableAttributedString!](cfattributedstringcreatemutable(_:_:).md)
  Creates a mutable attributed string.
- [func CFAttributedStringCreateMutableCopy(CFAllocator!, CFIndex, CFAttributedString!) -> CFMutableAttributedString!](cfattributedstringcreatemutablecopy(_:_:_:).md)
  Creates a mutable copy of an attributed string.
### Modifying a CFMutableAttributedString
- [func CFAttributedStringBeginEditing(CFMutableAttributedString!)](cfattributedstringbeginediting(_:).md)
  Defers internal consistency-checking and coalescing for a mutable attributed string.
- [func CFAttributedStringEndEditing(CFMutableAttributedString!)](cfattributedstringendediting(_:).md)
  Re-enables internal consistency-checking and coalescing for a mutable attributed string.
- [func CFAttributedStringGetMutableString(CFMutableAttributedString!) -> CFMutableString!](cfattributedstringgetmutablestring(_:).md)
  Gets as a mutable string the string for an attributed string.
- [func CFAttributedStringRemoveAttribute(CFMutableAttributedString!, CFRange, CFString!)](cfattributedstringremoveattribute(_:_:_:).md)
  Removes the value of a single attribute over a specified range.
- [func CFAttributedStringReplaceString(CFMutableAttributedString!, CFRange, CFString!)](cfattributedstringreplacestring(_:_:_:).md)
  Modifies the string of an attributed string.
- [func CFAttributedStringReplaceAttributedString(CFMutableAttributedString!, CFRange, CFAttributedString!)](cfattributedstringreplaceattributedstring(_:_:_:).md)
  Replaces the attributed substring over a range with another attributed string.
- [func CFAttributedStringSetAttribute(CFMutableAttributedString!, CFRange, CFString!, CFTypeRef!)](cfattributedstringsetattribute(_:_:_:_:).md)
  Sets the value of a single attribute over the specified range.
- [func CFAttributedStringSetAttributes(CFMutableAttributedString!, CFRange, CFDictionary!, Bool)](cfattributedstringsetattributes(_:_:_:_:).md)
  Sets the value of attributes of a mutable attributed string over a specified range.

## Relationships

### Inherits From
- [CFAttributedString](cfattributedstring.md)
### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Property List Programming Topics for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
- [String Programming Guide for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/introCFStrings.html#//apple_ref/doc/uid/10000131i)
- [Data Formatting Guide for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDataFormatting/Articles/CFDataFormatting.html#//apple_ref/doc/uid/10000176i)
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmutableattributedstring)*