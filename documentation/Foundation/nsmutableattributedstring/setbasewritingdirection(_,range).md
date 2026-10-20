# setBaseWritingDirection(_:range:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the base writing direction for the characters to the specified direction.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func setBaseWritingDirection(_ writingDirection: NSWritingDirection, range: NSRange)
```

```objc
- (void) setBaseWritingDirection:(NSWritingDirection) writingDirection range:(NSRange) range;
```

## Parameters

- `writingDirection`: The writing direction to use.
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
- [func applyFontTraits(NSFontTraitMask, range: NSRange)](./applyfonttraits%28_,range%29.md)
  Applies the specified font-related attributes to characters in the string.
- [func setAlignment(NSTextAlignment, range: NSRange)](./setalignment%28_,range%29.md)
  Sets the alignment characteristic of the paragraph style attribute for the specified range of text.
- [func subscriptRange(NSRange)](./subscriptrange%28_%29.md)
  Decrements the value of the superscript attribute for characters in the specified range by one.
- [func superscriptRange(NSRange)](./superscriptrange%28_%29.md)
  Increments the value of the superscript attribute for characters in the specified range by one.
- [func unscriptRange(NSRange)](./unscriptrange%28_%29.md)
  Removes the superscript attribute from the characters in the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/setbasewritingdirection(_:range:))*