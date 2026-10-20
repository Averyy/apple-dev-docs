# localeIdentifier(fromComponents:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSString *) localeIdentifierFromComponents:(NSDictionary<NSString *,NSString *> *) dict;
```

#### Return Value

A locale identifier created from the components specified in `dict`.

#### Discussion

This reverses the actions of [`components(fromLocaleIdentifier:)`](./components%28fromlocaleidentifier%29.md), so for example the dictionary `{NSLocaleLanguageCode="en", NSLocaleCountryCode="US", NSLocaleCalendar=NSJapaneseCalendar}` becomes `"en_US@calendar=japanese"`.

## Parameters

- `dict`: A dictionary containing components that specify a locale. For possible values, see `NSLocale Component Keys`.

## See Also

### Related Documentation
- [class var isoLanguageCodes: [String]](./isolanguagecodes.md)
  The list of known language codes.
### Converting Between Identifiers
- [class func canonicalLocaleIdentifier(from: String) -> String](./canonicallocaleidentifier%28from%29.md)
  Returns the canonical identifier for a given locale identification string.
- [class func components(fromLocaleIdentifier: String) -> [String : String]](./components%28fromlocaleidentifier%29.md)
  Returns a dictionary that is the result of parsing a locale ID.
- [class func canonicalLanguageIdentifier(from: String) -> String](./canonicallanguageidentifier%28from%29.md)
  Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [class func localeIdentifier(fromWindowsLocaleCode: UInt32) -> String?](./localeidentifier%28fromwindowslocalecode%29.md)
  Returns a locale identifier from a Windows locale code.
- [class func windowsLocaleCode(fromLocaleIdentifier: String) -> UInt32](./windowslocalecode%28fromlocaleidentifier%29.md)
  Returns a Window locale code from the locale identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/localeidentifier(fromcomponents:))*