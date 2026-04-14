# isTypingAdaptationEnabled

**Framework**: BrowserEngineKit  
**Kind**: property

A Boolean value that controls whether the system learns new words and corrections.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
optional var isTypingAdaptationEnabled: Bool { get }
```

#### Discussion

Setting this property to `false` prevents the system from learning of words or corrections by omitting their addition to the keyboard lexicon.

## See Also

- [var isSingleLineDocument: Bool](beextendedtextinputtraits/issinglelinedocument.md)
  A Boolean value that represents whether the active web input field is a single line document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beextendedtextinputtraits/istypingadaptationenabled)*