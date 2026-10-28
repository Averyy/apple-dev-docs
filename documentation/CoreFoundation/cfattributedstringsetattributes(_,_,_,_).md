# CFAttributedStringSetAttributes(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Sets the value of attributes of a mutable attributed string over a specified range.

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
func CFAttributedStringSetAttributes(_ aStr: CFMutableAttributedString!, _ range: CFRange, _ replacement: CFDictionary!, _ clearOtherAttributes: Bool)
```

```c
extern void CFAttributedStringSetAttributes(CFMutableAttributedStringRef aStr, CFRange range, CFDictionaryRef replacement, Boolean clearOtherAttributes);
```

## Discussion

Note that after this call, if it is mutable, changes to `replacement` will not affect the contents of the attributed string.

## Parameters

- `aStr`: The mutable attributed string to modify.
- `range`: The range of aStr over to which the new attributes apply. `range` must not exceed the bounds of `aStr`.
- `replacement`: A dictionary that contains key-value pairs that specify the new attributes to apply to `range`. The keys must be CFString objects, and the corresponding values must be CFType objects.
- `clearOtherAttributes`: If `false`, existing attributes (that aren’t being replaced) are left alone; otherwise they are cleared.

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
- [func CFAttributedStringSetAttribute(CFMutableAttributedString!, CFRange, CFString!, CFTypeRef!)](./cfattributedstringsetattribute%28_,_,_,_%29.md)
  Sets the value of a single attribute over the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringsetattributes(_:_:_:_:))*