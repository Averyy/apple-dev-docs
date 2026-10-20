# updateComposition()

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method

Informs the input controller that the composition has changed.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func updateComposition()
```

```objc
- (void) updateComposition;
```

#### Discussion

This method calls the protocol method composedString: to obtain the current composition. The current composition is sent to the client by a call to the method `setMarkedText(_:selectionRange:replacementRange:)`.

## See Also

### Managing Composition
- [func cancelComposition()](./cancelcomposition%28%29.md)
  Stops the current composition and replaces marked text with the original text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller/updatecomposition())*