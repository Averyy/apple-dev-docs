# updateComposition()

**Framework**: InputMethodKit  
**Kind**: method

Informs the input controller that the composition has changed.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func updateComposition()
```

#### Discussion

This method calls the protocol method composedString: to obtain the current composition. The current composition is sent to the client by a call to the method `setMarkedText(_:selectionRange:replacementRange:)`.

## See Also

- [func cancelComposition()](imkinputcontroller/cancelcomposition.md)
  Stops the current composition and replaces marked text with the original text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/updatecomposition())*