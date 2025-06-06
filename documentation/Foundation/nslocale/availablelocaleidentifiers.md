# availableLocaleIdentifiers

**Framework**: Foundation  
**Kind**: property

The list of locale identifiers available on the system.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var availableLocaleIdentifiers: [String] { get }
```

#### Discussion

A locale identifier starts with a language code, often includes a region code, and occasionally includes a script designator.  See [`Locale IDs`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html#//apple_ref/doc/uid/10000171i-CH15-SW9) for more information about the structure of a locale identifier.

Use [`localizedString(forLocaleIdentifier:)`](nslocale/localizedstring(forlocaleidentifier:).md) to obtain a human readable description of any of the locale identifiers in this list.

## See Also

- [Internationalization and Localization Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i)
- [class var isoCountryCodes: [String]](nslocale/isocountrycodes.md)
  The list of known country or region codes.
- [class var isoLanguageCodes: [String]](nslocale/isolanguagecodes.md)
  The list of known language codes.
- [class var isoCurrencyCodes: [String]](nslocale/isocurrencycodes.md)
  The list of known currency codes.
- [class var commonISOCurrencyCodes: [String]](nslocale/commonisocurrencycodes.md)
  A list of commonly encountered currency codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/availablelocaleidentifiers)*