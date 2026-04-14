# transliterateChinese(forText:)

**Framework**: BrowserEngineKit  
**Kind**: method

Converts text between traditional and simplified Chinese.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func transliterateChinese(forText text: String)
```

#### Discussion

Call this method to invoke the system’s standard transliteration behavior, for example, when your browser text view receives [`transliterateChinese(_:)`](berespondereditactions/transliteratechinese(_:).md).

## Parameters

- `text`: The text to transliterate.

## See Also

- [func translate(text: String, from: CGRect)](betextinteraction/translate(text:from:).md)
  Presents a translation of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinteraction/transliteratechinese(fortext:))*