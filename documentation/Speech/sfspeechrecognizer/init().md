# init()

**Framework**: Speech  
**Kind**: init  
**Role**: Initializer

Creates a speech recognizer associated with the user’s default language settings.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
convenience init?()
```

```objc
- (instancetype) init;
```

#### Return Value

An initialized speech recognizer object, or `nil` if there was a problem creating the object.

#### Discussion

If the user’s default language is not supported for speech recognition, this method attempts to fall back to the language used by the keyboard for dictation. If that fails, this method returns `nil`.

Even if this method returns a valid speech recognizer object, the speech recognition services may be temporarily unavailable. To determine whether speech recognition services are available, check the [`isAvailable`](./isavailable.md) property.

## See Also

### Creating a speech recognizer
- [init?(locale: Locale)](./init%28locale%29.md)
  Creates a speech recognizer associated with the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizer/init())*