# localizedString(forRegionCode:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

### Getting display information about a locale
- [func localizedString(for: Calendar.Identifier) -> String?](./localizedstring%28for%29.md)
  Returns a localized string for a specified calendar.
- [func localizedString(forCollationIdentifier: String) -> String?](./localizedstring%28forcollationidentifier%29.md)
  Returns a localized string for a specified ICU collation identifier.
- [func localizedString(forCollatorIdentifier: String) -> String?](./localizedstring%28forcollatoridentifier%29.md)
  Returns a localized string for a specified ICU collator identifier.
- [func localizedString(forCurrencyCode: String) -> String?](./localizedstring%28forcurrencycode%29.md)
  Returns a localized string for a specified ISO 4217 currency code.
- [func localizedString(forIdentifier: String) -> String?](./localizedstring%28foridentifier%29.md)
  Returns a localized string for a specified locale identifier.
- [func localizedString(forLanguageCode: String) -> String?](./localizedstring%28forlanguagecode%29.md)
  Returns a localized string for a specified language code.
- [func localizedString(forScriptCode: String) -> String?](./localizedstring%28forscriptcode%29.md)
  Returns a localized string for a specified script code.
- [func localizedString(forVariantCode: String) -> String?](./localizedstring%28forvariantcode%29.md)
  Returns a localized string for a specified variant code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/localizedstring(forregioncode:))*