# setAlignment(_:range:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the alignment characteristic of the paragraph style attribute for the specified range of text.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func setAlignment(_ alignment: NSTextAlignment, range: NSRange)
```

```objc
- (void) setAlignment:(NSTextAlignment) alignment range:(NSRange) range;
```

#### Discussion

When attribute fixing takes place, this change will affect only paragraphs whose first character was included in `range`. Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## Parameters

- `alignment`: The alignment to use.
- `range`: The range of characters.

## See Also

### Related Documentation
- [func fixParagraphStyleAttribute(in: NSRange)](./fixparagraphstyleattribute%28in%29.md)
  Fixes the paragraph style attributes in the specified range and assigns a paragraph style to all characters in the paragraph.
### Changing Attributes
- [func setAttributes([NSAttributedString.Key : Any]?, range: NSRange)](./setattributes%28_,range%29.md)
  Sets the attributes for the characters in the specified range to the specified attributes.
- [func addAttribute(NSAttributedString.Key, value: Any, range: NSRange)](./addattribute%28_,value,range%29.md)
  Adds an attribute with the given name and value to the characters in the specified range.
- [func addAttributes([NSAttributedString.Key : Any], range: NSRange)](./addattributes%28_,range%29.md)
  Adds the given collection of attributes to the characters in the specified range.
- [func removeAttribute(NSAttributedString.Key, range: NSRange)](./removeattribute%28_,range%29.md)
  Removes the named attribute from the characters in the specified range.
- [func applyFontTraits(NSFontTraitMask, range: NSRange)](./applyfonttraits%28_,range%29.md)
  Applies the specified font-related attributes to characters in the string.
- [func setBaseWritingDirection(NSWritingDirection, range: NSRange)](./setbasewritingdirection%28_,range%29.md)
  Sets the base writing direction for the characters to the specified direction.
- [func subscriptRange(NSRange)](./subscriptrange%28_%29.md)
  Decrements the value of the superscript attribute for characters in the specified range by one.
- [func superscriptRange(NSRange)](./superscriptrange%28_%29.md)
  Increments the value of the superscript attribute for characters in the specified range by one.
- [func unscriptRange(NSRange)](./unscriptrange%28_%29.md)
  Removes the superscript attribute from the characters in the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/setalignment(_:range:))*