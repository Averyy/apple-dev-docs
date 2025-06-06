# localizedString(forRegionCode:)

**Framework**: Foundation  
**Kind**: method

Returns a localized string for a specified region code.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func localizedString(forRegionCode regionCode: String) -> String?
```

#### Discussion

For example, in the “en” locale, the result for `"fr"` is `"France"`.

## See Also

- [func localizedString(for: Calendar.Identifier) -> String?](locale/localizedstring(for:).md)
  Returns a localized string for a specified calendar.
- [func localizedString(forCollationIdentifier: String) -> String?](locale/localizedstring(forcollationidentifier:).md)
  Returns a localized string for a specified ICU collation identifier.
- [func localizedString(forCollatorIdentifier: String) -> String?](locale/localizedstring(forcollatoridentifier:).md)
  Returns a localized string for a specified ICU collator identifier.
- [func localizedString(forCurrencyCode: String) -> String?](locale/localizedstring(forcurrencycode:).md)
  Returns a localized string for a specified ISO 4217 currency code.
- [func localizedString(forIdentifier: String) -> String?](locale/localizedstring(foridentifier:).md)
  Returns a localized string for a specified locale identifier.
- [func localizedString(forLanguageCode: String) -> String?](locale/localizedstring(forlanguagecode:).md)
  Returns a localized string for a specified language code.
- [func localizedString(forScriptCode: String) -> String?](locale/localizedstring(forscriptcode:).md)
  Returns a localized string for a specified script code.
- [func localizedString(forVariantCode: String) -> String?](locale/localizedstring(forvariantcode:).md)
  Returns a localized string for a specified variant code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/localizedstring(forregioncode:))*