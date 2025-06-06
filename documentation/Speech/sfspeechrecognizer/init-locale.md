# init(locale:)

**Framework**: Speech  
**Kind**: init

Creates a speech recognizer associated with the specified locale.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
init?(locale: Locale)
```

#### Return Value

An initialized speech recognizer object, or `nil` if the specified language was not supported.

#### Discussion

If you specify a language that is not supported by the speech recognizer, this method attempts to fall back to the language used by the keyboard for dictation. If that fails, this method returns `nil`.

Even if this method returns a valid speech recognizer object, the speech recognition services may be temporarily unavailable. To determine whether speech recognition services are available, check the [`isAvailable`](sfspeechrecognizer/isavailable.md) property.

## Parameters

- `locale`: The locale object representing the language you want to use for speech recognition. For a list of languages supported by the speech recognizer, see  .

## See Also

- [convenience init?()](sfspeechrecognizer/init.md)
  Creates a speech recognizer associated with the user’s default language settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizer/init(locale:))*