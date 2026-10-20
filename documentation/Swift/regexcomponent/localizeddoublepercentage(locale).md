# localizedDoublePercentage(locale:)

**Framework**: Swift  
**Kind**: method

Creates a regex component that matches a localized percentage string, capturing it as a double-precision floating-point value.

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
static func localizedDoublePercentage(locale: Locale) -> Self
```

#### Return Value

A `RegexComponent` that matches localized percentage substrings as [`Double`](double.md) instances.

#### Discussion

This method matches percentage substrings in accordance with the provided locale. For example, in the `en_US` locale, `0.75` formats as `75%`, and `12345.67` formats as `1,234,567%`. Other locales use different separators, or omit them entirely. Because of this, the regex needs to know what locale convention to match against.

The following example creates a [`Regex`](regex.md) that matches a date and time followed by whitespace and a percentage string formatted in the `en_US` locale. It then matches this regex against a source string containing a date with this format, some whitespace, and a percentage string.

```swift
let enUSLocale = Locale(languageCode: .english, languageRegion: .unitedStates)
let source = "7/31/2022, 5:15:12 AM  75.3%"
let matcher = Regex {
    One(.dateTime(date: .numeric,
                  time: .standard,
                  locale: enUSLocale,
                  timeZone: TimeZone(identifier: "PST")!))
    OneOrMore(.horizontalWhitespace)
    Capture {
        One(.localizedDoublePercentage(locale: enUSLocale))
    }
}
guard let match = source.firstMatch(of: matcher) else { return }
let percentage = match.1 // percentage == 0.753
```

## Parameters

- `locale`: The locale that specifies formatting conventions to use when matching percentage strings.

## See Also

- [static func localizedInteger(locale: Locale) -> Self](regexcomponent/localizedinteger(locale:).md)
  Creates a regex component that matches a localized numeric string, capturing it as an integer value.
- [static func localizedDouble(locale: Locale) -> Self](regexcomponent/localizeddouble(locale:).md)
  Creates a regex component that matches a localized numeric string, capturing it as a double-precision floating-point value.
- [static func localizedDecimal(locale: Locale) -> Self](regexcomponent/localizeddecimal(locale:).md)
  Creates a regex component that matches a localized decimal string, capturing it as a Foundation decimal.
- [static func localizedCurrency(code: Locale.Currency, locale: Locale) -> Self](regexcomponent/localizedcurrency(code:locale:).md)
  Creates a regex component that matches a localized currency string, capturing it as a decimal value.
- [static func localizedIntegerCurrency(code: Locale.Currency, locale: Locale) -> Self](regexcomponent/localizedintegercurrency(code:locale:).md)
  Creates a regex component that matches a localized currency string, capturing it as an integer value.
- [static func localizedIntegerPercentage(locale: Locale) -> Self](regexcomponent/localizedintegerpercentage(locale:).md)
  Creates a regex component that matches a localized percentage string, capturing it as a double-precision floating-point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexcomponent/localizeddoublepercentage(locale:))*