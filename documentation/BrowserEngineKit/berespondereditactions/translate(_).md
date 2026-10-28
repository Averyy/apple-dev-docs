# translate(_:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Presents a translation of the selected text.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
optional func translate(_ sender: Any?)
```

```objc
- (void) translate:(id) sender;
```

## Discussion

To present the standard system UI for translating text, call [`translate(text:from:)`](../betextinteraction/translate%28text,from%29.md) in your implementation of this method.

## Parameters

- `sender`: The object calling this method.

## See Also

### Translating and transliterating text
- [func transliterateChinese(Any?)](./transliteratechinese%28_%29.md)
  Converts the selected text between traditional and simplified Chinese.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berespondereditactions/translate(_:))*