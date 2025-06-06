# localeIdentifier(fromComponents:)

**Framework**: Foundation  
**Kind**: method

Returns a locale identifier from the components specified in a given dictionary.

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
class func localeIdentifier(fromComponents dict: [String : String]) -> String
```

#### Return Value

A locale identifier created from the components specified in `dict`.

#### Discussion

This reverses the actions of [`components(fromLocaleIdentifier:)`](nslocale/components(fromlocaleidentifier:).md), so for example the dictionary `{NSLocaleLanguageCode="en", NSLocaleCountryCode="US", NSLocaleCalendar=NSJapaneseCalendar}` becomes `"en_US@calendar=japanese"`.

## Parameters

- `dict`: A dictionary containing components that specify a locale. For possible values, see  .

## See Also

- [class var isoLanguageCodes: [String]](nslocale/isolanguagecodes.md)
  The list of known language codes.
- [class func canonicalLocaleIdentifier(from: String) -> String](nslocale/canonicallocaleidentifier(from:).md)
  Returns the canonical identifier for a given locale identification string.
- [class func components(fromLocaleIdentifier: String) -> [String : String]](nslocale/components(fromlocaleidentifier:).md)
  Returns a dictionary that is the result of parsing a locale ID.
- [class func canonicalLanguageIdentifier(from: String) -> String](nslocale/canonicallanguageidentifier(from:).md)
  Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [class func localeIdentifier(fromWindowsLocaleCode: UInt32) -> String?](nslocale/localeidentifier(fromwindowslocalecode:).md)
  Returns a locale identifier from a Windows locale code.
- [class func windowsLocaleCode(fromLocaleIdentifier: String) -> UInt32](nslocale/windowslocalecode(fromlocaleidentifier:).md)
  Returns a Window locale code from the locale identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/localeidentifier(fromcomponents:))*