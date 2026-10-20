# CFAttributedStringSetAttribute(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Sets the value of a single attribute over the specified range.

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
func CFAttributedStringSetAttribute(_ aStr: CFMutableAttributedString!, _ range: CFRange, _ attrName: CFString!, _ value: CFTypeRef!)
```

```c
extern void CFAttributedStringSetAttribute(CFMutableAttributedStringRef aStr, CFRange range, CFStringRef attrName, CFTypeRef value);
```

## Parameters

- `aStr`: The mutable attributed string to modify.
- `range`: The range of `aStr` over to which the new attributes apply. `range` must not exceed the bounds of `aStr`.
- `attrName`: The name of the attribute whose value to set.
- `value`: The value of the attribute `attrName` to apply over `range`. This value may not be `NULL`. If you want to remove an attribute, use [`CFAttributedStringRemoveAttribute(_:_:_:)`](./cfattributedstringremoveattribute%28_,_,_%29.md).

## See Also

### Modifying a CFMutableAttributedString
- [func CFAttributedStringBeginEditing(CFMutableAttributedString!)](./cfattributedstringbeginediting%28_%29.md)
  Defers internal consistency-checking and coalescing for a mutable attributed string.
- [func CFAttributedStringEndEditing(CFMutableAttributedString!)](./cfattributedstringendediting%28_%29.md)
  Re-enables internal consistency-checking and coalescing for a mutable attributed string.
- [func CFAttributedStringGetMutableString(CFMutableAttributedString!) -> CFMutableString!](./cfattributedstringgetmutablestring%28_%29.md)
  Gets as a mutable string the string for an attributed string.
- [func CFAttributedStringRemoveAttribute(CFMutableAttributedString!, CFRange, CFString!)](./cfattributedstringremoveattribute%28_,_,_%29.md)
  Removes the value of a single attribute over a specified range.
- [func CFAttributedStringReplaceString(CFMutableAttributedString!, CFRange, CFString!)](./cfattributedstringreplacestring%28_,_,_%29.md)
  Modifies the string of an attributed string.
- [func CFAttributedStringReplaceAttributedString(CFMutableAttributedString!, CFRange, CFAttributedString!)](./cfattributedstringreplaceattributedstring%28_,_,_%29.md)
  Replaces the attributed substring over a range with another attributed string.
- [func CFAttributedStringSetAttributes(CFMutableAttributedString!, CFRange, CFDictionary!, Bool)](./cfattributedstringsetattributes%28_,_,_,_%29.md)
  Sets the value of attributes of a mutable attributed string over a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringsetattribute(_:_:_:_:))*