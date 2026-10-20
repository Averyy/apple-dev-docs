# locale

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The locale for which the media option was authored.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var locale: Locale? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSLocale * locale;
```

## See Also

### Getting the language and locale settings
- [var displayName: String](./displayname.md)
  A string suitable for display using the current system locale.
- [func displayName(with: Locale) -> String](./displayname%28with%29.md)
  Returns a string suitable for display using the specified locale.
- [var extendedLanguageTag: String?](./extendedlanguagetag.md)
  The IETF BCP 47 language tag associated with the option


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/locale)*