# canonicalLocaleIdentifier(from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSString *) canonicalLocaleIdentifierFromString:(NSString *) string;
```

## Return Value

The canonical identifier for an the locale identified by `string`.

## Parameters

- `string`: A locale identification string.

## See Also

### Converting Between Identifiers
- [class func components(fromLocaleIdentifier: String) -> [String : String]](./components%28fromlocaleidentifier%29.md)
  Returns a dictionary that is the result of parsing a locale ID.
- [class func localeIdentifier(fromComponents: [String : String]) -> String](./localeidentifier%28fromcomponents%29.md)
  Returns a locale identifier from the components specified in a given dictionary.
- [class func canonicalLanguageIdentifier(from: String) -> String](./canonicallanguageidentifier%28from%29.md)
  Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [class func localeIdentifier(fromWindowsLocaleCode: UInt32) -> String?](./localeidentifier%28fromwindowslocalecode%29.md)
  Returns a locale identifier from a Windows locale code.
- [class func windowsLocaleCode(fromLocaleIdentifier: String) -> UInt32](./windowslocalecode%28fromlocaleidentifier%29.md)
  Returns a Window locale code from the locale identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/canonicallocaleidentifier(from:))*