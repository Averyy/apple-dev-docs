# localizedString(forLocaleIdentifier:)

**Framework**: Foundation  
**Kind**: method

Returns the localized string for the specified locale identifier.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func localizedString(forLocaleIdentifier localeIdentifier: String) -> String
```

#### Return Value

The localized name of the locale.

#### Discussion

For example, calling this method on an American English (`en_US`) locale, passing `"fr_FR"` for `localeIdentifier`, produces the string `"French (France)"`.

This method is equivalent to calling the [`displayName(forKey:value:)`](nslocale/displayname(forkey:value:).md) method passing the [`identifier`](nslocale/key/identifier.md) key and `localeIdentifier` value.

## Parameters

- `localeIdentifier`: The identifier for which you want the localized name.

## See Also

- [class var availableLocaleIdentifiers: [String]](nslocale/availablelocaleidentifiers.md)
  The list of locale identifiers available on the system.
- [func localizedString(forCountryCode: String) -> String?](nslocale/localizedstring(forcountrycode:).md)
  Returns the localized string for a country or region code.
- [func localizedString(forLanguageCode: String) -> String?](nslocale/localizedstring(forlanguagecode:).md)
  Returns the localized string for the specified language code.
- [func localizedString(forScriptCode: String) -> String?](nslocale/localizedstring(forscriptcode:).md)
  Returns the localized string for the specified script code.
- [func localizedString(forVariantCode: String) -> String?](nslocale/localizedstring(forvariantcode:).md)
  Returns the localized string for the specified variant code.
- [func localizedString(forCollationIdentifier: String) -> String?](nslocale/localizedstring(forcollationidentifier:).md)
  Returns the localized string for the specified collation identifier.
- [func localizedString(forCollatorIdentifier: String) -> String?](nslocale/localizedstring(forcollatoridentifier:).md)
  Returns the localized string for the specified collator identifier.
- [func localizedString(forCurrencyCode: String) -> String?](nslocale/localizedstring(forcurrencycode:).md)
  Returns the localized string for the specified currency code.
- [func localizedString(forCalendarIdentifier: String) -> String?](nslocale/localizedstring(forcalendaridentifier:).md)
  Returns the localized string for the specified calendar identifier.
- [Locale Calendar Identifiers](locale-calendar-identifiers.md)
  The types of calendars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/localizedstring(forlocaleidentifier:))*