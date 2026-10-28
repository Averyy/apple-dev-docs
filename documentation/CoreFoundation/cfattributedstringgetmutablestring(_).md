# CFAttributedStringGetMutableString(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Gets as a mutable string the string for an attributed string.

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
func CFAttributedStringGetMutableString(_ aStr: CFMutableAttributedString!) -> CFMutableString!
```

```c
extern CFMutableStringRefCFAttributedStringGetMutableString(CFMutableAttributedStringRef aStr);
```

## Return Value

The string for the specified attributed string as a mutable string.

## Discussion

This function allows you to edit the character contents of the attributed string as if it were a CFMutableString. Attributes corresponding to the edited range are appropriately modified. If, as a result of the edit, new characters are introduced into the string, they inherit the attributes of the first replaced character from range. If no existing characters are replaced by the edit, the new characters inherit the attributes of the character preceding range if it has any, otherwise of the character following range. If the initial string is empty, the attributes for the new characters are also empty.

## Parameters

- `aStr`: The mutable attributed string from which to retrieve the string.

## See Also

### Modifying a CFMutableAttributedString
- [func CFAttributedStringBeginEditing(CFMutableAttributedString!)](./cfattributedstringbeginediting%28_%29.md)
  Defers internal consistency-checking and coalescing for a mutable attributed string.
- [func CFAttributedStringEndEditing(CFMutableAttributedString!)](./cfattributedstringendediting%28_%29.md)
  Re-enables internal consistency-checking and coalescing for a mutable attributed string.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringgetmutablestring(_:))*