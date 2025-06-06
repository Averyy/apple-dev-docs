# setBaseWritingDirection(_:range:)

**Framework**: Foundation  
**Kind**: method

Sets the base writing direction for the characters to the specified direction.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func setBaseWritingDirection(_ writingDirection: NSWritingDirection, range: NSRange)
```

## Parameters

- `writingDirection`: The writing direction to use.
- `range`: The range of characters.

## See Also

- [func setAttributes([NSAttributedString.Key : Any]?, range: NSRange)](nsmutableattributedstring/setattributes(_:range:).md)
  Sets the attributes for the characters in the specified range to the specified attributes.
- [func addAttribute(NSAttributedString.Key, value: Any, range: NSRange)](nsmutableattributedstring/addattribute(_:value:range:).md)
  Adds an attribute with the given name and value to the characters in the specified range.
- [func addAttributes([NSAttributedString.Key : Any], range: NSRange)](nsmutableattributedstring/addattributes(_:range:).md)
  Adds the given collection of attributes to the characters in the specified range.
- [func removeAttribute(NSAttributedString.Key, range: NSRange)](nsmutableattributedstring/removeattribute(_:range:).md)
  Removes the named attribute from the characters in the specified range.
- [func applyFontTraits(NSFontTraitMask, range: NSRange)](nsmutableattributedstring/applyfonttraits(_:range:).md)
  Applies the specified font-related attributes to characters in the string.
- [func setAlignment(NSTextAlignment, range: NSRange)](nsmutableattributedstring/setalignment(_:range:).md)
  Sets the alignment characteristic of the paragraph style attribute for the specified range of text.
- [func subscriptRange(NSRange)](nsmutableattributedstring/subscriptrange(_:).md)
  Decrements the value of the superscript attribute for characters in the specified range by one.
- [func superscriptRange(NSRange)](nsmutableattributedstring/superscriptrange(_:).md)
  Increments the value of the superscript attribute for characters in the specified range by one.
- [func unscriptRange(NSRange)](nsmutableattributedstring/unscriptrange(_:).md)
  Removes the superscript attribute from the characters in the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/setbasewritingdirection(_:range:))*