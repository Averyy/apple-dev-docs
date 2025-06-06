# textStyling(at:in:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Returns a dictionary containing NSAttributedString keys represeting appearance customizations.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func textStyling(at position: UITextPosition, in direction: UITextStorageDirection) -> [NSAttributedString.Key : Any]?
```

#### Discussion

For example, text styling information influence the appearance of a correction rect.

## See Also

- [var extendedTextInputTraits: (any BEExtendedTextInputTraits)?](betextinput/extendedtextinputtraits.md)
  Object from which the BEExtendedTextInputTraits will be gathered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/textstyling(at:in:))*