# selectionRange()

**Framework**: InputMethodKit  
**Kind**: method

Returns where the range of the selection that should be placed inside marked text.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func selectionRange() -> NSRange
```

#### Return Value

The range of the selection.

#### Discussion

This method is called by [`updateComposition()`](imkinputcontroller/updatecomposition().md) to obtain the selection range for marked text. The default implementation sets the selection range at the end of the marked text. You should override this method if your input method provides font or glyph information.

## See Also

- [func compositionAttributes(at: NSRange) -> NSMutableDictionary!](imkinputcontroller/compositionattributes(at:).md)
  Returns a dictionary of text attributes.
- [func replacementRange() -> NSRange](imkinputcontroller/replacementrange.md)
  Returns the range in the client document that the text should replace.
- [func mark(forStyle: Int, at: NSRange) -> [AnyHashable : Any]!](imkinputcontroller/mark(forstyle:at:).md)
  Returns a dictionary of text attributes that can mark a range of an attributed string to send to a client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/selectionrange())*