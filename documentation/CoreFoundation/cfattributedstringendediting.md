# CFAttributedStringEndEditing(_:)

**Framework**: Core Foundation  
**Kind**: func

Re-enables internal consistency-checking and coalescing for a mutable attributed string.

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
func CFAttributedStringEndEditing(_ aStr: CFMutableAttributedString!)
```

## Parameters

- `aStr`: A mutable attributed string, following a call to  .

## See Also

- [func CFAttributedStringBeginEditing(CFMutableAttributedString!)](cfattributedstringbeginediting(_:).md)
  Defers internal consistency-checking and coalescing for a mutable attributed string.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringendediting(_:))*