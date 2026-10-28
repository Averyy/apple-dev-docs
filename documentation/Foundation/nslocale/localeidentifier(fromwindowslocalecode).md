# localeIdentifier(fromWindowsLocaleCode:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a locale identifier from a Windows locale code.

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
class func localeIdentifier(fromWindowsLocaleCode lcid: UInt32) -> String?
```

```objc
+ (NSString *) localeIdentifierFromWindowsLocaleCode:(uint32_t) lcid;
```

## Return Value

The locale identifier.

## Parameters

- `lcid`: The Windows locale code.

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
- [class func windowsLocaleCode(fromLocaleIdentifier: String) -> UInt32](./windowslocalecode%28fromlocaleidentifier%29.md)
  Returns a Window locale code from the locale identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/localeidentifier(fromwindowslocalecode:))*