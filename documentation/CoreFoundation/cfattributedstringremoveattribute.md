# CFAttributedStringRemoveAttribute(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Removes the value of a single attribute over a specified range.

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
func CFAttributedStringRemoveAttribute(_ aStr: CFMutableAttributedString!, _ range: CFRange, _ attrName: CFString!)
```

#### Discussion

It is  an error of the specified attribute does not exist over the given range.

## Parameters

- `aStr`: The mutable attributed string to modify.
- `range`: The range of   from which to remove the specified attribute.   must not exceed the bounds of  .
- `attrName`: The name of the attribute to remove.

## See Also

- [func CFAttributedStringBeginEditing(CFMutableAttributedString!)](cfattributedstringbeginediting(_:).md)
  Defers internal consistency-checking and coalescing for a mutable attributed string.
- [func CFAttributedStringEndEditing(CFMutableAttributedString!)](cfattributedstringendediting(_:).md)
  Re-enables internal consistency-checking and coalescing for a mutable attributed string.
- [func CFAttributedStringGetMutableString(CFMutableAttributedString!) -> CFMutableString!](cfattributedstringgetmutablestring(_:).md)
  Gets as a mutable string the string for an attributed string.
- [func CFAttributedStringReplaceString(CFMutableAttributedString!, CFRange, CFString!)](cfattributedstringreplacestring(_:_:_:).md)
  Modifies the string of an attributed string.
- [func CFAttributedStringReplaceAttributedString(CFMutableAttributedString!, CFRange, CFAttributedString!)](cfattributedstringreplaceattributedstring(_:_:_:).md)
  Replaces the attributed substring over a range with another attributed string.
- [func CFAttributedStringSetAttribute(CFMutableAttributedString!, CFRange, CFString!, CFTypeRef!)](cfattributedstringsetattribute(_:_:_:_:).md)
  Sets the value of a single attribute over the specified range.
- [func CFAttributedStringSetAttributes(CFMutableAttributedString!, CFRange, CFDictionary!, Bool)](cfattributedstringsetattributes(_:_:_:_:).md)
  Sets the value of attributes of a mutable attributed string over a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringremoveattribute(_:_:_:))*