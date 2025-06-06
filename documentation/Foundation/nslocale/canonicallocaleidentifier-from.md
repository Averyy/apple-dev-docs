# canonicalLocaleIdentifier(from:)

**Framework**: Foundation  
**Kind**: method

Returns the canonical identifier for a given locale identification string.

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
class func canonicalLocaleIdentifier(from string: String) -> String
```

#### Return Value

The canonical identifier for an the locale identified by `string`.

## Parameters

- `string`: A locale identification string.

## See Also

- [class func components(fromLocaleIdentifier: String) -> [String : String]](nslocale/components(fromlocaleidentifier:).md)
  Returns a dictionary that is the result of parsing a locale ID.
- [class func localeIdentifier(fromComponents: [String : String]) -> String](nslocale/localeidentifier(fromcomponents:).md)
  Returns a locale identifier from the components specified in a given dictionary.
- [class func canonicalLanguageIdentifier(from: String) -> String](nslocale/canonicallanguageidentifier(from:).md)
  Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [class func localeIdentifier(fromWindowsLocaleCode: UInt32) -> String?](nslocale/localeidentifier(fromwindowslocalecode:).md)
  Returns a locale identifier from a Windows locale code.
- [class func windowsLocaleCode(fromLocaleIdentifier: String) -> UInt32](nslocale/windowslocalecode(fromlocaleidentifier:).md)
  Returns a Window locale code from the locale identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/canonicallocaleidentifier(from:))*