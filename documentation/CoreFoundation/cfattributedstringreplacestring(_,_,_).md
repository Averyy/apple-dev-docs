# CFAttributedStringReplaceString(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Modifies the string of an attributed string.

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
func CFAttributedStringReplaceString(_ aStr: CFMutableAttributedString!, _ range: CFRange, _ replacement: CFString!)
```

```c
extern void CFAttributedStringReplaceString(CFMutableAttributedStringRef aStr, CFRange range, CFStringRef replacement);
```

## Parameters

- `aStr`: The mutable attributed string to modify.
- `range`: The range of `aStr` to be modified. `range` must not specify characters outside the bounds of `aStr`.
- `replacement`: The string to replace the existing string in `range`.

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
- [func CFAttributedStringReplaceAttributedString(CFMutableAttributedString!, CFRange, CFAttributedString!)](./cfattributedstringreplaceattributedstring%28_,_,_%29.md)
  Replaces the attributed substring over a range with another attributed string.
- [func CFAttributedStringSetAttribute(CFMutableAttributedString!, CFRange, CFString!, CFTypeRef!)](./cfattributedstringsetattribute%28_,_,_,_%29.md)
  Sets the value of a single attribute over the specified range.
- [func CFAttributedStringSetAttributes(CFMutableAttributedString!, CFRange, CFDictionary!, Bool)](./cfattributedstringsetattributes%28_,_,_,_%29.md)
  Sets the value of attributes of a mutable attributed string over a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringreplacestring(_:_:_:))*