# locale

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

The locale of the speech recognizer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var locale: Locale { get }
```

```objc
@property (nonatomic, copy, readonly) NSLocale * locale;
```

## Discussion

The locale of the speech recognizer is an `NSLocale` object. The default value of this property is the system locale (that is, `+[NSLocale systemLocale]`).

## See Also

### Getting the current language
- [class func supportedLocales() -> Set<Locale>](./supportedlocales%28%29.md)
  Returns the set of locales that are supported by the speech recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognizer/locale)*