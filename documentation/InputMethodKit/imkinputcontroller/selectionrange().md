# selectionRange()

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method

Returns where the range of the selection that should be placed inside marked text.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func selectionRange() -> NSRange
```

```objc
- (NSRange) selectionRange;
```

## Return Value

The range of the selection.

## Discussion

This method is called by [`updateComposition()`](./updatecomposition%28%29.md) to obtain the selection range for marked text. The default implementation sets the selection range at the end of the marked text. You should override this method if your input method provides font or glyph information.

## See Also

### Working with Ranges
- [func compositionAttributes(at: NSRange) -> NSMutableDictionary!](./compositionattributes%28at%29.md)
  Returns a dictionary of text attributes.
- [func replacementRange() -> NSRange](./replacementrange%28%29.md)
  Returns the range in the client document that the text should replace.
- [func mark(forStyle: Int, at: NSRange) -> [AnyHashable : Any]!](./mark%28forstyle,at%29.md)
  Returns a dictionary of text attributes that can mark a range of an attributed string to send to a client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/selectionrange())*