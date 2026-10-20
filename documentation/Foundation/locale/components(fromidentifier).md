# components(fromIdentifier:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a dictionary that splits an identifier into its component pieces.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 8.0+ - Deprecated in 16.0
- macOS 10.10+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+
- watchOS 2.0+ - Deprecated in 9.0

> **Deprecated**: Use `Locale.Components(identifier:)` to access components

## Declaration

```swift
static func components(fromIdentifier string: String) -> [String : String]
```

## See Also

### Converting between identifiers
- [static func canonicalIdentifier(from: String) -> String](./canonicalidentifier%28from%29.md)
  Returns a canonical identifier from the given string.
- [static func identifier(fromComponents: [String : String]) -> String](./identifier%28fromcomponents%29.md)
  Constructs an identifier from a dictionary of components.
- [static func identifier(Locale.IdentifierType, from: String) -> String](./identifier%28_,from%29.md)
  Returns the identifier conforming to the specified standard for the specified string.
- [Locale.IdentifierType](./identifiertype.md)
  A type that indicates the standard that defines a locale’s identifier.
- [static func canonicalLanguageIdentifier(from: String) -> String](./canonicallanguageidentifier%28from%29.md)
  Returns a canonical language identifier from the given string.
- [static func identifier(fromWindowsLocaleCode: Int) -> String?](./identifier%28fromwindowslocalecode%29.md)
  Returns the locale identifier from a given Windows locale code, or `nil` if it could not be converted.
- [static func windowsLocaleCode(fromIdentifier: String) -> Int?](./windowslocalecode%28fromidentifier%29.md)
  Returns the Windows locale code from a given identifier, or `nil` if it could not be converted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/components(fromidentifier:))*