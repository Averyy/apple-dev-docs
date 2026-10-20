# identifier(_:from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns the identifier conforming to the specified standard for the specified string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func identifier(_ type: Locale.IdentifierType, from string: String) -> String
```

#### Return Value

A locale identifier.

## Parameters

- `type`: The identifier type used by `string`, such as [`Locale.IdentifierType.icu`](./identifiertype/icu.md) or [`Locale.IdentifierType.bcp47`](./identifiertype/bcp47.md).
- `string`: An identifier string that complies with the standard indicated by `type`.

## See Also

### Converting between identifiers
- [static func canonicalIdentifier(from: String) -> String](./canonicalidentifier%28from%29.md)
  Returns a canonical identifier from the given string.
- [static func components(fromIdentifier: String) -> [String : String]](./components%28fromidentifier%29.md)
  Returns a dictionary that splits an identifier into its component pieces.
- [static func identifier(fromComponents: [String : String]) -> String](./identifier%28fromcomponents%29.md)
  Constructs an identifier from a dictionary of components.
- [Locale.IdentifierType](./identifiertype.md)
  A type that indicates the standard that defines a locale’s identifier.
- [static func canonicalLanguageIdentifier(from: String) -> String](./canonicallanguageidentifier%28from%29.md)
  Returns a canonical language identifier from the given string.
- [static func identifier(fromWindowsLocaleCode: Int) -> String?](./identifier%28fromwindowslocalecode%29.md)
  Returns the locale identifier from a given Windows locale code, or `nil` if it could not be converted.
- [static func windowsLocaleCode(fromIdentifier: String) -> Int?](./windowslocalecode%28fromidentifier%29.md)
  Returns the Windows locale code from a given identifier, or `nil` if it could not be converted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/identifier(_:from:))*