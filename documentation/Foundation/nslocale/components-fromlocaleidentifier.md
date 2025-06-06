# components(fromLocaleIdentifier:)

**Framework**: Foundation  
**Kind**: method

Returns a dictionary that is the result of parsing a locale ID.

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
class func components(fromLocaleIdentifier string: String) -> [String : String]
```

#### Return Value

A dictionary that is the result of parsing `string` as a locale ID. The keys are the constant NSString constants corresponding to the locale ID components, and the values correspond to constants where available. For possible values, see [`NSLocale.Key`](nslocale/key.md).

#### Discussion

For example, the locale identifier `"en_US@calendar=japanese"` yields a dictionary with three entries:

- [`languageCode`](nslocale/key/languagecode.md) = `en`
- [`countryCode`](nslocale/key/countrycode.md) = `US`
- [`calendar`](nslocale/key/calendar.md) = [`NSJapaneseCalendar`](nsjapanesecalendar.md)

## Parameters

- `string`: A locale ID, consisting of language, script, country, variant, and keyword/value pairs, for example,  .

## See Also

- [class func canonicalLocaleIdentifier(from: String) -> String](nslocale/canonicallocaleidentifier(from:).md)
  Returns the canonical identifier for a given locale identification string.
- [class func localeIdentifier(fromComponents: [String : String]) -> String](nslocale/localeidentifier(fromcomponents:).md)
  Returns a locale identifier from the components specified in a given dictionary.
- [class func canonicalLanguageIdentifier(from: String) -> String](nslocale/canonicallanguageidentifier(from:).md)
  Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [class func localeIdentifier(fromWindowsLocaleCode: UInt32) -> String?](nslocale/localeidentifier(fromwindowslocalecode:).md)
  Returns a locale identifier from a Windows locale code.
- [class func windowsLocaleCode(fromLocaleIdentifier: String) -> UInt32](nslocale/windowslocalecode(fromlocaleidentifier:).md)
  Returns a Window locale code from the locale identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/components(fromlocaleidentifier:))*