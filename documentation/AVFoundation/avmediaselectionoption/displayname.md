# displayName

**Framework**: AVFoundation  
**Kind**: property

A string suitable for display using the current system locale.

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
var displayName: String { get }
```

#### Discussion

The string takes into account this option’s common metadata, media characteristics, and locale properties in addition to the provided locale to formulate a string intended for display

## See Also

- [func displayName(with: Locale) -> String](avmediaselectionoption/displayname(with:).md)
  Returns a string suitable for display using the specified locale.
- [var locale: Locale?](avmediaselectionoption/locale.md)
  The locale for which the media option was authored.
- [var extendedLanguageTag: String?](avmediaselectionoption/extendedlanguagetag.md)
  The IETF BCP 47 language tag associated with the option


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/displayname)*