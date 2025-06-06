# translate(text:from:)

**Framework**: BrowserEngineKit  
**Kind**: method

Presents a translation of the text.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
func translate(text: String, from presentationRect: CGRect)
```

## Parameters

- `text`: The text to translate.
- `presentationRect`: The area in the text input view in which the text appears, which the operating system uses to locate the translation UI.

## See Also

- [func transliterateChinese(forText: String)](betextinteraction/transliteratechinese(fortext:).md)
  Converts the text between traditional and simplified Chinese.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinteraction/translate(text:from:))*