# supportedLocales()

**Framework**: Speech  
**Kind**: method

Returns the set of locales that are supported by the speech recognizer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class func supportedLocales() -> Set<Locale>
```

#### Return Value

A set of locales that support speech recognition.

#### Discussion

This method returns the locales for which speech recognition is supported. Support for a locale does not guarantee that speech recognition is currently possible for that locale. For some locales, the speech recognizer requires an active Internet connection to communicate with Apple’s servers. If the speech recognizer is currently unable to process requests,   [`isAvailable`](sfspeechrecognizer/isavailable.md) returns [`false`](https://developer.apple.com/documentation/swift/false).

Speech recognition supports the same locales that are supported by the keyboard’s dictation feature. For a list of these locales, see [`QuickType Keyboard: Dictation`](https://developer.apple.comhttps://www.apple.com/ios/feature-availability/#quicktype-keyboard-dictation).

## See Also

- [var locale: Locale](sfspeechrecognizer/locale.md)
  The locale of the speech recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizer/supportedlocales())*