# translate(text:from:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Presents a translation of the text.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func translate(text: String, from presentationRect: CGRect)
```

```objc
- (void) translateText:(NSString *) text fromRect:(CGRect) presentationRect;
```

## Parameters

- `text`: The text to translate.
- `presentationRect`: The area in the text input view in which the text appears, which the system uses to locate the translation UI.

## See Also

### Translation and transliteration
- [func transliterateChinese(forText: String)](./transliteratechinese%28fortext%29.md)
  Converts text between traditional and simplified Chinese.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinteraction/translate(text:from:))*