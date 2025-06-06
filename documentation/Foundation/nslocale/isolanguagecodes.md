# isoLanguageCodes

**Framework**: Foundation  
**Kind**: property

The list of known language codes.

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
class var isoLanguageCodes: [String] { get }
```

#### Discussion

A language code is a short string that represent a particular language. All languages have a three-character ISO 639-2 string, while some languages also have a two-character ISO 639-1 string. See [`ISO 639.2 Codes for the Representation of Names of Languages`](https://developer.apple.comhttp://www.loc.gov/standards/iso639-2/php/English_list.php) for the complete list of standardized language codes.

The array provided by this property contains a list of codes for all the languages the system knows about, designated by the ISO 639-1 code if available, or the ISO 639-2 code if not. Use the method [`localizedString(forLanguageCode:)`](nslocale/localizedstring(forlanguagecode:).md) to obtain a human readable string for any of the codes in the list.

For more information about language localization in your app, see [`Language and Locale IDs`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html#//apple_ref/doc/uid/10000171i-CH15).

Not all language codes have supporting locale data in the system.

## See Also

- [class var availableLocaleIdentifiers: [String]](nslocale/availablelocaleidentifiers.md)
  The list of locale identifiers available on the system.
- [class var isoCountryCodes: [String]](nslocale/isocountrycodes.md)
  The list of known country or region codes.
- [class var isoCurrencyCodes: [String]](nslocale/isocurrencycodes.md)
  The list of known currency codes.
- [class var commonISOCurrencyCodes: [String]](nslocale/commonisocurrencycodes.md)
  A list of commonly encountered currency codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/isolanguagecodes)*