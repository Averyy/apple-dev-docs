# localizedDecimal(locale:)

**Framework**: Swift  
**Kind**: method

Creates a regex component that matches a localized decimal string, capturing it as a Foundation decimal.

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
static func localizedDecimal(locale: Locale) -> Self
```

#### Return Value

A `RegexComponent` that matches localized decimal substrings as Foundation [`Decimal`](https://developer.apple.com/documentation/Foundation/Decimal) instances.

#### Discussion

This method matches decimal substrings in accordance with the provided locale. For example, the value `1234567890.1234` formats as `1,234,567,890.1234` in the `en_US` locale, as `1 234 567 890,1234` in the `FR` locale, and as `1234567890.1234` in the `JP` locale. Because of this, the regex needs to know what locale convention to match against.

The following example creates a [`Regex`](regex.md) that matches a date and time followed by whitespace and a decimal formatted in the `en_US` locale. It then matches this regex against a source string containing a date with this format, some whitespace, and a decimal value.

```swift
let enUSLocale = Locale(languageCode: .english, languageRegion: .unitedStates)
let source = "7/31/2022, 5:15:12 AM  1,234,567,890.1234"
let matcher = Regex {
    One(.dateTime(date: .numeric,
                  time: .standard,
                  locale: enUSLocale,
                  timeZone: TimeZone(identifier: "PST")!))
    OneOrMore(.horizontalWhitespace)
    Capture {
        One(.localizedDecimal(locale: enUSLocale))
    }
}
guard let match = source.firstMatch(of: matcher) else { return }
let decimal = match.1 // decimal == 1234567890.1234
```

## Parameters

- `locale`: The locale that specifies formatting conventions to use when matching decimal strings.

## See Also

- [static func localizedInteger(locale: Locale) -> Self](regexcomponent/localizedinteger(locale:).md)
  Creates a regex component that matches a localized numeric string, capturing it as an integer value.
- [static func localizedDouble(locale: Locale) -> Self](regexcomponent/localizeddouble(locale:).md)
  Creates a regex component that matches a localized numeric string, capturing it as a double-precision floating-point value.
- [static func localizedCurrency(code: Locale.Currency, locale: Locale) -> Self](regexcomponent/localizedcurrency(code:locale:).md)
  Creates a regex component that matches a localized currency string, capturing it as a decimal value.
- [static func localizedIntegerCurrency(code: Locale.Currency, locale: Locale) -> Self](regexcomponent/localizedintegercurrency(code:locale:).md)
  Creates a regex component that matches a localized currency string, capturing it as an integer value.
- [static func localizedIntegerPercentage(locale: Locale) -> Self](regexcomponent/localizedintegerpercentage(locale:).md)
  Creates a regex component that matches a localized percentage string, capturing it as a double-precision floating-point value.
- [static func localizedDoublePercentage(locale: Locale) -> Self](regexcomponent/localizeddoublepercentage(locale:).md)
  Creates a regex component that matches a localized percentage string, capturing it as a double-precision floating-point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexcomponent/localizeddecimal(locale:))*