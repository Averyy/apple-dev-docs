# CFAttributedStringBeginEditing(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Defers internal consistency-checking and coalescing for a mutable attributed string.

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
func CFAttributedStringBeginEditing(_ aStr: CFMutableAttributedString!)
```

```c
extern void CFAttributedStringBeginEditing(CFMutableAttributedStringRef aStr);
```

#### Discussion

Defers internal consistency-checking and coalescing for a mutable attributed string. You must balance a call to this function with a corresponding [`CFAttributedStringEndEditing(_:)`](./cfattributedstringendediting%28_%29.md).

## Parameters

- `aStr`: A mutable attributed string that is to be edited.

## See Also

### Modifying a CFMutableAttributedString
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
- [func CFAttributedStringSetAttribute(CFMutableAttributedString!, CFRange, CFString!, CFTypeRef!)](./cfattributedstringsetattribute%28_,_,_,_%29.md)
  Sets the value of a single attribute over the specified range.
- [func CFAttributedStringSetAttributes(CFMutableAttributedString!, CFRange, CFDictionary!, Bool)](./cfattributedstringsetattributes%28_,_,_,_%29.md)
  Sets the value of attributes of a mutable attributed string over a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringbeginediting(_:))*