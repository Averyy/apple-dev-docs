# localizedIntegerCurrency(code:locale:)

**Framework**: Swift  
**Kind**: method

Creates a regex component that matches a localized currency string, capturing it as an integer value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func localizedIntegerCurrency(code: Locale.Currency, locale: Locale) -> Self
```

#### Return Value

A `RegexComponent` that matches localized currency substrings as [`Int`](int.md) instances.

#### Discussion

This method matches currency substrings in accordance with the provided currency code and locale. For example, the currency code `USD` matches U.S. dollars, which use the symbol `$`, and `JPY` matches Japanese yen, which use the symbol `¥`. The locale determines formatting conventions for number separators in the currency value. The regex uses both of these to match currency substrings.

The method truncates fractional parts in currency strings. To match currency strings with fractional parts, use [`localizedCurrency(code:locale:)`](regexcomponent/localizedcurrency(code:locale:).md) instead.

The following example creates a [`Regex`](regex.md) that matches a date and time followed by whitespace and a currency value that uses U.S. dollars and the `en_US` locale. It then matches this regex against a source string containing a date with this format, some whitespace, and a currency value in dollars.

```swift
let enUSLocale = Locale(languageCode: .english, languageRegion: .unitedStates)
let source = "7/31/2022, 5:15:12 AM    $39,739"
let matcher = Regex {
    One(.dateTime(date: .numeric,
                  time: .standard,
                  locale: enUSLocale,
                  timeZone: TimeZone(identifier: "PST")!))
    OneOrMore(.horizontalWhitespace)
    Capture {
        One(.localizedIntegerCurrency(code: Locale.Currency("USD"),
                                      locale: enUSLocale))
    }
}

guard let match = source.firstMatch(of: matcher) else { return }
let currency = match?.1 // currency == 39739
```

## Parameters

- `code`: The currency code that indicates the currency symbol or name to match against.
- `locale`: The locale that specifies formatting conventions to use when matching currency strings.

## See Also

- [static func localizedInteger(locale: Locale) -> Self](regexcomponent/localizedinteger(locale:).md)
  Creates a regex component that matches a localized numeric string, capturing it as an integer value.
- [static func localizedDouble(locale: Locale) -> Self](regexcomponent/localizeddouble(locale:).md)
  Creates a regex component that matches a localized numeric string, capturing it as a double-precision floating-point value.
- [static func localizedDecimal(locale: Locale) -> Self](regexcomponent/localizeddecimal(locale:).md)
  Creates a regex component that matches a localized decimal string, capturing it as a Foundation decimal.
- [static func localizedCurrency(code: Locale.Currency, locale: Locale) -> Self](regexcomponent/localizedcurrency(code:locale:).md)
  Creates a regex component that matches a localized currency string, capturing it as a decimal value.
- [static func localizedIntegerPercentage(locale: Locale) -> Self](regexcomponent/localizedintegerpercentage(locale:).md)
  Creates a regex component that matches a localized percentage string, capturing it as a double-precision floating-point value.
- [static func localizedDoublePercentage(locale: Locale) -> Self](regexcomponent/localizeddoublepercentage(locale:).md)
  Creates a regex component that matches a localized percentage string, capturing it as a double-precision floating-point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexcomponent/localizedintegercurrency(code:locale:))*