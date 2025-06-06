# addAttributes(_:range:)

**Framework**: Foundation  
**Kind**: method

Adds the given collection of attributes to the characters in the specified range.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addAttributes(_ attrs: [NSAttributedString.Key : Any] = [:], range: NSRange)
```

#### Discussion

You may assign any name/value pair you wish to a range of characters. Raises an [`invalidArgumentException`](nsexceptionname/invalidargumentexception.md) if `attrs` is `nil` and an [`rangeException`](nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## Parameters

- `attrs`: A dictionary containing the attributes to add. Attribute keys can be supplied by another framework or can be custom ones you define. For information about the system-supplied attribute keys, see the Constants section in  .
- `range`: The range of characters to which the specified attributes apply.

## See Also

- [func setAttributes([NSAttributedString.Key : Any]?, range: NSRange)](nsmutableattributedstring/setattributes(_:range:).md)
  Sets the attributes for the characters in the specified range to the specified attributes.
- [func addAttribute(NSAttributedString.Key, value: Any, range: NSRange)](nsmutableattributedstring/addattribute(_:value:range:).md)
  Adds an attribute with the given name and value to the characters in the specified range.
- [func removeAttribute(NSAttributedString.Key, range: NSRange)](nsmutableattributedstring/removeattribute(_:range:).md)
  Removes the named attribute from the characters in the specified range.
- [func applyFontTraits(NSFontTraitMask, range: NSRange)](nsmutableattributedstring/applyfonttraits(_:range:).md)
  Applies the specified font-related attributes to characters in the string.
- [func setAlignment(NSTextAlignment, range: NSRange)](nsmutableattributedstring/setalignment(_:range:).md)
  Sets the alignment characteristic of the paragraph style attribute for the specified range of text.
- [func setBaseWritingDirection(NSWritingDirection, range: NSRange)](nsmutableattributedstring/setbasewritingdirection(_:range:).md)
  Sets the base writing direction for the characters to the specified direction.
- [func subscriptRange(NSRange)](nsmutableattributedstring/subscriptrange(_:).md)
  Decrements the value of the superscript attribute for characters in the specified range by one.
- [func superscriptRange(NSRange)](nsmutableattributedstring/superscriptrange(_:).md)
  Increments the value of the superscript attribute for characters in the specified range by one.
- [func unscriptRange(NSRange)](nsmutableattributedstring/unscriptrange(_:).md)
  Removes the superscript attribute from the characters in the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/addattributes(_:range:))*