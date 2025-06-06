# CFAttributedStringSetAttribute(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sets the value of a single attribute over the specified range.

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
func CFAttributedStringSetAttribute(_ aStr: CFMutableAttributedString!, _ range: CFRange, _ attrName: CFString!, _ value: CFTypeRef!)
```

## Parameters

- `aStr`: The mutable attributed string to modify.
- `range`: The range of   over to which the new attributes apply.   must not exceed the bounds of  .
- `attrName`: The name of the attribute whose value to set.
- `value`: The value of the attribute   to apply over  . This value may not be  . If you want to remove an attribute, use  .

## See Also

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
- [func CFAttributedStringSetAttributes(CFMutableAttributedString!, CFRange, CFDictionary!, Bool)](cfattributedstringsetattributes(_:_:_:_:).md)
  Sets the value of attributes of a mutable attributed string over a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringsetattribute(_:_:_:_:))*