# components(fromLocaleIdentifier:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSDictionary<NSString *,NSString *> *) componentsFromLocaleIdentifier:(NSString *) string;
```

## Return Value

A dictionary that is the result of parsing `string` as a locale ID. The keys are the constant NSString constants corresponding to the locale ID components, and the values correspond to constants where available. For possible values, see [`NSLocale.Key`](./key.md).

## Discussion

For example, the locale identifier `"en_US@calendar=japanese"` yields a dictionary with three entries:

- [`languageCode`](./key/languagecode.md) = `en`
- [`countryCode`](./key/countrycode.md) = `US`
- [`calendar`](./key/calendar.md) = [`NSJapaneseCalendar`](../nsjapanesecalendar.md)

## Parameters

- `string`: A locale ID, consisting of language, script, country, variant, and keyword/value pairs, for example, `"en_US@calendar=japanese"`.

## See Also

### Converting Between Identifiers
- [class func canonicalLocaleIdentifier(from: String) -> String](./canonicallocaleidentifier%28from%29.md)
  Returns the canonical identifier for a given locale identification string.
- [class func localeIdentifier(fromComponents: [String : String]) -> String](./localeidentifier%28fromcomponents%29.md)
  Returns a locale identifier from the components specified in a given dictionary.
- [class func canonicalLanguageIdentifier(from: String) -> String](./canonicallanguageidentifier%28from%29.md)
  Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [class func localeIdentifier(fromWindowsLocaleCode: UInt32) -> String?](./localeidentifier%28fromwindowslocalecode%29.md)
  Returns a locale identifier from a Windows locale code.
- [class func windowsLocaleCode(fromLocaleIdentifier: String) -> UInt32](./windowslocalecode%28fromlocaleidentifier%29.md)
  Returns a Window locale code from the locale identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/components(fromlocaleidentifier:))*