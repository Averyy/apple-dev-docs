# setBaseWritingDirection(_:for:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Informs the text view of the writing direction for a given range of text.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func setBaseWritingDirection(_ writingDirection: NSWritingDirection, for range: UITextRange)
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

- writingDirection: Whether the writing direction is left-to-right, right-to-left, or the natural direction for the current script.
- range: The range in the text view’s document for which the writing direction applies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/setbasewritingdirection(_:for:))*