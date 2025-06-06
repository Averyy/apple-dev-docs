# extendedLanguageTag

**Framework**: AVFoundation  
**Kind**: property

The IETF BCP 47 language tag associated with the option

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var extendedLanguageTag: String? { get }
```

#### Discussion

This property may be `nil` indicating that the underlying media presented when the option is selected carries no language information. This can occur with media formats for which language information is optional, such as HTTP Live Streaming playlists, or that do not accommodate language information in machine-readable form.

Clients that are filtering media selection options by language should be prepared to handle cases in which this value is `nil`. Further, they should be prepared to handle cases in which an `extendedLanguageTag` is present but indicates that the language is “undetermined” (a language value of @“und”, as defined in ISO 639-2).

## See Also

- [var displayName: String](avmediaselectionoption/displayname.md)
  A string suitable for display using the current system locale.
- [func displayName(with: Locale) -> String](avmediaselectionoption/displayname(with:).md)
  Returns a string suitable for display using the specified locale.
- [var locale: Locale?](avmediaselectionoption/locale.md)
  The locale for which the media option was authored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/extendedlanguagetag)*