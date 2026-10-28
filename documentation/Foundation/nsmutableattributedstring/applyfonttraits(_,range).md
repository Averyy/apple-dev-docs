# applyFontTraits(_:range:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Applies the specified font-related attributes to characters in the string.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func applyFontTraits(_ traitMask: NSFontTraitMask, range: NSRange)
```

```objc
- (void) applyFontTraits:(NSFontTraitMask) traitMask range:(NSRange) range;
```

## Discussion

Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

## Parameters

- `traitMask`: The font attributes to apply. For information about the font traits you can apply, see [`NSFontManager`](../../AppKit/nsfontmanager.md).
- `range`: The range of characters.

## See Also

### Changing Attributes
- [func setAttributes([NSAttributedString.Key : Any]?, range: NSRange)](./setattributes%28_,range%29.md)
  Sets the attributes for the characters in the specified range to the specified attributes.
- [func addAttribute(NSAttributedString.Key, value: Any, range: NSRange)](./addattribute%28_,value,range%29.md)
  Adds an attribute with the given name and value to the characters in the specified range.
- [func addAttributes([NSAttributedString.Key : Any], range: NSRange)](./addattributes%28_,range%29.md)
  Adds the given collection of attributes to the characters in the specified range.
- [func removeAttribute(NSAttributedString.Key, range: NSRange)](./removeattribute%28_,range%29.md)
  Removes the named attribute from the characters in the specified range.
- [func setAlignment(NSTextAlignment, range: NSRange)](./setalignment%28_,range%29.md)
  Sets the alignment characteristic of the paragraph style attribute for the specified range of text.
- [func setBaseWritingDirection(NSWritingDirection, range: NSRange)](./setbasewritingdirection%28_,range%29.md)
  Sets the base writing direction for the characters to the specified direction.
- [func subscriptRange(NSRange)](./subscriptrange%28_%29.md)
  Decrements the value of the superscript attribute for characters in the specified range by one.
- [func superscriptRange(NSRange)](./superscriptrange%28_%29.md)
  Increments the value of the superscript attribute for characters in the specified range by one.
- [func unscriptRange(NSRange)](./unscriptrange%28_%29.md)
  Removes the superscript attribute from the characters in the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/applyfonttraits(_:range:))*