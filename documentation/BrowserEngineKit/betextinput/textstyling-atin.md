# textStyling(at:in:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Provides a dictionary that customizes the appearance of strings.

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

The returned strings might pertain to text styling information for a correction rectangle, for example.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/textstyling(at:in:))*