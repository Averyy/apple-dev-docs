# canonicalLanguageIdentifier(from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier.

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
class func canonicalLanguageIdentifier(from string: String) -> String
```

```objc
+ (NSString *) canonicalLanguageIdentifierFromString:(NSString *) string;
```

## Return Value

A string that represents the canonical language identifier for the specified arbitrary locale identifier.

## Parameters

- `string`: A string representation of an arbitrary locale identifier.

## See Also

### Converting Between Identifiers
- [class func canonicalLocaleIdentifier(from: String) -> String](./canonicallocaleidentifier%28from%29.md)
  Returns the canonical identifier for a given locale identification string.
- [class func components(fromLocaleIdentifier: String) -> [String : String]](./components%28fromlocaleidentifier%29.md)
  Returns a dictionary that is the result of parsing a locale ID.
- [class func localeIdentifier(fromComponents: [String : String]) -> String](./localeidentifier%28fromcomponents%29.md)
  Returns a locale identifier from the components specified in a given dictionary.
- [class func localeIdentifier(fromWindowsLocaleCode: UInt32) -> String?](./localeidentifier%28fromwindowslocalecode%29.md)
  Returns a locale identifier from a Windows locale code.
- [class func windowsLocaleCode(fromLocaleIdentifier: String) -> UInt32](./windowslocalecode%28fromlocaleidentifier%29.md)
  Returns a Window locale code from the locale identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/canonicallanguageidentifier(from:))*