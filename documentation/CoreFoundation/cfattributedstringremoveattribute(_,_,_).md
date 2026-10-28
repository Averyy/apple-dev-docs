# CFAttributedStringRemoveAttribute(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Removes the value of a single attribute over a specified range.

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
func CFAttributedStringRemoveAttribute(_ aStr: CFMutableAttributedString!, _ range: CFRange, _ attrName: CFString!)
```

```c
extern void CFAttributedStringRemoveAttribute(CFMutableAttributedStringRef aStr, CFRange range, CFStringRef attrName);
```

## Discussion

It is *not* an error of the specified attribute does not exist over the given range.

## Parameters

- `aStr`: The mutable attributed string to modify.
- `range`: The range of `aStr` from which to remove the specified attribute. `range` must not exceed the bounds of `aStr`.
- `attrName`: The name of the attribute to remove.

## See Also

### Modifying a CFMutableAttributedString
- [func CFAttributedStringBeginEditing(CFMutableAttributedString!)](./cfattributedstringbeginediting%28_%29.md)
  Defers internal consistency-checking and coalescing for a mutable attributed string.
- [func CFAttributedStringEndEditing(CFMutableAttributedString!)](./cfattributedstringendediting%28_%29.md)
  Re-enables internal consistency-checking and coalescing for a mutable attributed string.
- [func CFAttributedStringGetMutableString(CFMutableAttributedString!) -> CFMutableString!](./cfattributedstringgetmutablestring%28_%29.md)
  Gets as a mutable string the string for an attributed string.
- [func CFAttributedStringReplaceString(CFMutableAttributedString!, CFRange, CFString!)](./cfattributedstringreplacestring%28_,_,_%29.md)
  Modifies the string of an attributed string.
- [func CFAttributedStringReplaceAttributedString(CFMutableAttributedString!, CFRange, CFAttributedString!)](./cfattributedstringreplaceattributedstring%28_,_,_%29.md)
  Replaces the attributed substring over a range with another attributed string.
- [func CFAttributedStringSetAttribute(CFMutableAttributedString!, CFRange, CFString!, CFTypeRef!)](./cfattributedstringsetattribute%28_,_,_,_%29.md)
  Sets the value of a single attribute over the specified range.
- [func CFAttributedStringSetAttributes(CFMutableAttributedString!, CFRange, CFDictionary!, Bool)](./cfattributedstringsetattributes%28_,_,_,_%29.md)
  Sets the value of attributes of a mutable attributed string over a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringremoveattribute(_:_:_:))*