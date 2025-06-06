# cancelComposition()

**Framework**: InputMethodKit  
**Kind**: method

Stops the current composition and replaces marked text with the original text.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func cancelComposition()
```

#### Discussion

This method calls the method originalString: to obtain the original text and sends that text to the client using a call to the `IMKTextInput`  protocol method `insertText(_:replacementRange:)`

## See Also

- [func updateComposition()](imkinputcontroller/updatecomposition.md)
  Informs the input controller that the composition has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/cancelcomposition())*