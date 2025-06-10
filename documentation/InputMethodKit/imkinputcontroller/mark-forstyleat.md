# mark(forStyle:at:)

**Framework**: InputMethodKit  
**Kind**: method

Returns a dictionary of text attributes that can mark a range of an attributed string to send to a client.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func mark(forStyle style: Int, at range: NSRange) -> [AnyHashable : Any]!
```

#### Return Value

The dictionary of text attributes.

#### Discussion

This utility function can be called by input methods to mark each range (i.e. clause ) of marked text. T

The default implementation first calls the method [`compositionAttributes(at:)`](imkinputcontroller/compositionattributes(at:).md) to obtain the additional attributes that an input method wants to include, such as font or glyph information. Then, it adds the appropriate underline and underline color information to the attributes dictionary for the style parameter. Finally it adds the style value as the dictionary value. The key for the style value is [`markedClauseSegment`](https://developer.apple.com/documentation/Foundation/NSAttributedString/Key/markedClauseSegment).

## Parameters

- `style`: A style, which should be one of the following values:  ,  , or  . See the   header file for the definition of these values.
- `range`: The range (that is, a clause) to mark.

## See Also

- [func compositionAttributes(at: NSRange) -> NSMutableDictionary!](imkinputcontroller/compositionattributes(at:).md)
  Returns a dictionary of text attributes.
- [func selectionRange() -> NSRange](imkinputcontroller/selectionrange.md)
  Returns where the range of the selection that should be placed inside marked text.
- [func replacementRange() -> NSRange](imkinputcontroller/replacementrange.md)
  Returns the range in the client document that the text should replace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/mark(forstyle:at:))*