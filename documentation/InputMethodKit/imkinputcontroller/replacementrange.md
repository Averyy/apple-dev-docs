# replacementRange()

**Framework**: InputMethodKit  
**Kind**: method

Returns the range in the client document that the text should replace.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func replacementRange() -> NSRange
```

#### Return Value

The range to replace.

#### Discussion

This method is called by [`updateComposition()`](imkinputcontroller/updatecomposition().md) to obtain the range in the client  document where marked text should be placed. The default implementation returns an `NSRange` object whose location and length are `NSNotFound`. That indicates that the marked text should be placed at the current insertion point. Input methods that insert marked text somewhere other than at the current insertion point should override this method.

An example of an input method that might override this method would be one replaces words with synonyms. That input method would watch for certain words and when it detects such a word it would replaced the word by marked text that was a synonym of the word.

## See Also

- [func compositionAttributes(at: NSRange) -> NSMutableDictionary!](imkinputcontroller/compositionattributes(at:).md)
  Returns a dictionary of text attributes.
- [func selectionRange() -> NSRange](imkinputcontroller/selectionrange.md)
  Returns where the range of the selection that should be placed inside marked text.
- [func mark(forStyle: Int, at: NSRange) -> [AnyHashable : Any]!](imkinputcontroller/mark(forstyle:at:).md)
  Returns a dictionary of text attributes that can mark a range of an attributed string to send to a client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/replacementrange())*