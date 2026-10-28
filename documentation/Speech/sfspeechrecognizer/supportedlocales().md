# supportedLocales()

**Framework**: Speech  
**Kind**: method  
**Role**: Type Method

Returns the set of locales that are supported by the speech recognizer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class func supportedLocales() -> Set<Locale>
```

```objc
+ (NSSet<NSLocale *> *) supportedLocales;
```

## Return Value

A set of locales that support speech recognition.

## Discussion

This method returns the locales for which speech recognition is supported. Support for a locale does not guarantee that speech recognition is currently possible for that locale. For some locales, the speech recognizer requires an active Internet connection to communicate with Apple’s servers. If the speech recognizer is currently unable to process requests,   [`isAvailable`](./isavailable.md) returns `false`.

Speech recognition supports the same locales that are supported by the keyboard’s dictation feature. For a list of these locales, see [QuickType Keyboard: Dictation](https://www.apple.com/ios/feature-availability/#quicktype-keyboard-dictation).

## See Also

### Getting the current language
- [var locale: Locale](./locale.md)
  The locale of the speech recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizer/supportedlocales())*