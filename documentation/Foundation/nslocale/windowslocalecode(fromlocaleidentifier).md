# windowsLocaleCode(fromLocaleIdentifier:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a Window locale code from the locale identifier.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func windowsLocaleCode(fromLocaleIdentifier localeIdentifier: String) -> UInt32
```

```objc
+ (uint32_t) windowsLocaleCodeFromLocaleIdentifier:(NSString *) localeIdentifier;
```

## Return Value

The Windows locale code.

## Parameters

- `localeIdentifier`: The locale identifier.

## See Also

### Converting Between Identifiers
- [class func canonicalLocaleIdentifier(from: String) -> String](./canonicallocaleidentifier%28from%29.md)
  Returns the canonical identifier for a given locale identification string.
- [class func components(fromLocaleIdentifier: String) -> [String : String]](./components%28fromlocaleidentifier%29.md)
  Returns a dictionary that is the result of parsing a locale ID.
- [class func localeIdentifier(fromComponents: [String : String]) -> String](./localeidentifier%28fromcomponents%29.md)
  Returns a locale identifier from the components specified in a given dictionary.
- [class func canonicalLanguageIdentifier(from: String) -> String](./canonicallanguageidentifier%28from%29.md)
  Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [class func localeIdentifier(fromWindowsLocaleCode: UInt32) -> String?](./localeidentifier%28fromwindowslocalecode%29.md)
  Returns a locale identifier from a Windows locale code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/windowslocalecode(fromlocaleidentifier:))*