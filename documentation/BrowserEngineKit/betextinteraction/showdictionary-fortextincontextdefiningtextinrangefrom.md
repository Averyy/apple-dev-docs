# showDictionary(forTextInContext:definingTextInRange:from:)

**Framework**: BrowserEngineKit  
**Kind**: method

Presents a dictionary definition for the supplied text.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
func showDictionary(forTextInContext textWithContext: String, definingTextInRange range: NSRange, from presentationRect: CGRect)
```

## Parameters

- `textWithContext`: The text to supply a definition for, embedded in the sentence in which it appears in the text view’s document.
- `range`: The range of the word to define in the context text.
- `presentationRect`: The location of the text in the view, which the operating system uses to position the definition UI.

## See Also

- [func share(text: String, from: CGRect)](betextinteraction/share(text:from:).md)
  Presents standard UI for someone to share text from a browser text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinteraction/showdictionary(fortextincontext:definingtextinrange:from:))*