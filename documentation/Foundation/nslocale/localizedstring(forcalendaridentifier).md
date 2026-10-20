# localizedString(forCalendarIdentifier:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSString *) localizedStringForCalendarIdentifier:(NSString *) calendarIdentifier;
```

#### Return Value

A human readable string suitable for display to the user corresponding to the given calendar.

#### Discussion

For example, on an American English (`en_US`) locale, passing [`gregorian`](../nscalendar/identifier/gregorian.md) as the identifier, produces the string `"Gregorian Calendar"`.

## Parameters

- `calendarIdentifier`: The calendar identifier indicating the calendar whose name you want. Use one of the values listed in `Calendar Identifiers`.

## See Also

### Getting Display Information About a Locale
- [func localizedString(forLocaleIdentifier: String) -> String](./localizedstring%28forlocaleidentifier%29.md)
  Returns the localized string for the specified locale identifier.
- [func localizedString(forCountryCode: String) -> String?](./localizedstring%28forcountrycode%29.md)
  Returns the localized string for a country or region code.
- [func localizedString(forLanguageCode: String) -> String?](./localizedstring%28forlanguagecode%29.md)
  Returns the localized string for the specified language code.
- [func localizedString(forScriptCode: String) -> String?](./localizedstring%28forscriptcode%29.md)
  Returns the localized string for the specified script code.
- [func localizedString(forVariantCode: String) -> String?](./localizedstring%28forvariantcode%29.md)
  Returns the localized string for the specified variant code.
- [func localizedString(forCollationIdentifier: String) -> String?](./localizedstring%28forcollationidentifier%29.md)
  Returns the localized string for the specified collation identifier.
- [func localizedString(forCollatorIdentifier: String) -> String?](./localizedstring%28forcollatoridentifier%29.md)
  Returns the localized string for the specified collator identifier.
- [func localizedString(forCurrencyCode: String) -> String?](./localizedstring%28forcurrencycode%29.md)
  Returns the localized string for the specified currency code.
- [Locale Calendar Identifiers](../locale-calendar-identifiers.md)
  The types of calendars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/localizedstring(forcalendaridentifier:))*