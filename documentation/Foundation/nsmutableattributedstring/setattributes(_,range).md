# setAttributes(_:range:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the attributes for the characters in the specified range to the specified attributes.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setAttributes(_ attrs: [NSAttributedString.Key : Any]?, range: NSRange)
```

```objc
- (void) setAttributes:(NSDictionary<NSString *,id> *) attrs range:(NSRange) range;
```

#### Discussion

These new attributes replace any attributes previously associated with the characters in `range`. Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

To set attributes for a zero-length `NSMutableAttributedString` displayed in a text view, use the `NSTextView` method [`typingAttributes`](../../AppKit/nstextview/typingattributes.md).

## Parameters

- `attrs`: A dictionary containing the attributes to set. Attribute keys can be supplied by another framework or can be custom ones you define. For information about the system-supplied attribute keys, see the Constants section in [`NSAttributedString`](../nsattributedstring.md).
- `range`: The range of characters whose attributes are set.

## See Also

### Changing Attributes
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
- [func setBaseWritingDirection(NSWritingDirection, range: NSRange)](./setbasewritingdirection%28_,range%29.md)
  Sets the base writing direction for the characters to the specified direction.
- [func subscriptRange(NSRange)](./subscriptrange%28_%29.md)
  Decrements the value of the superscript attribute for characters in the specified range by one.
- [func superscriptRange(NSRange)](./superscriptrange%28_%29.md)
  Increments the value of the superscript attribute for characters in the specified range by one.
- [func unscriptRange(NSRange)](./unscriptrange%28_%29.md)
  Removes the superscript attribute from the characters in the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/setattributes(_:range:))*