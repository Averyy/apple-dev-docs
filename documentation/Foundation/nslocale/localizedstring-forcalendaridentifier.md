# localizedString(forCalendarIdentifier:)

**Framework**: Foundation  
**Kind**: method

Returns the localized string for the specified calendar identifier.

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
func localizedString(forCalendarIdentifier calendarIdentifier: String) -> String?
```

#### Return Value

A human readable string suitable for display to the user corresponding to the given calendar.

#### Discussion

For example, on an American English (`en_US`) locale, passing [`gregorian`](nscalendar/identifier/gregorian.md) as the identifier, produces the string `"Gregorian Calendar"`.

## Parameters

- `calendarIdentifier`: The calendar identifier indicating the calendar whose name you want. Use one of the values listed in  .

## See Also

- [func localizedString(forLocaleIdentifier: String) -> String](nslocale/localizedstring(forlocaleidentifier:).md)
  Returns the localized string for the specified locale identifier.
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
- [Locale Calendar Identifiers](locale-calendar-identifiers.md)
  The types of calendars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/localizedstring(forcalendaridentifier:))*