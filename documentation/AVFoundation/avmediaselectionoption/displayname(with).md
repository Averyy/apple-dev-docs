# displayName(with:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns a string suitable for display using the specified locale.

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
func displayName(with locale: Locale) -> String
```

```objc
- (NSString *) displayNameWithLocale:(NSLocale *) locale;
```

#### Return Value

A string containing the localized display name.

#### Discussion

The string takes into account this option’s common metadata, media characteristics and locale properties in addition to the provided locale to formulate a string intended for display

## Parameters

- `locale`: The locale to use in generating the display name.

## See Also

### Getting the language and locale settings
- [var displayName: String](./displayname.md)
  A string suitable for display using the current system locale.
- [var locale: Locale?](./locale.md)
  The locale for which the media option was authored.
- [var extendedLanguageTag: String?](./extendedlanguagetag.md)
  The IETF BCP 47 language tag associated with the option


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/displayname(with:))*