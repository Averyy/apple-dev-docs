# identifier(fromComponents:)

**Framework**: Foundation  
**Kind**: method

Constructs an identifier from a dictionary of components.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static func identifier(fromComponents components: [String : String]) -> String
```

## See Also

- [static func canonicalIdentifier(from: String) -> String](locale/canonicalidentifier(from:).md)
  Returns a canonical identifier from the given string.
- [static func components(fromIdentifier: String) -> [String : String]](locale/components(fromidentifier:).md)
  Returns a dictionary that splits an identifier into its component pieces.
- [static func identifier(Locale.IdentifierType, from: String) -> String](locale/identifier(_:from:).md)
  Returns the identifier conforming to the specified standard for the specified string.
- [Locale.IdentifierType](locale/identifiertype.md)
  A type that indicates the standard that defines a locale’s identifier.
- [static func canonicalLanguageIdentifier(from: String) -> String](locale/canonicallanguageidentifier(from:).md)
  Returns a canonical language identifier from the given string.
- [static func identifier(fromWindowsLocaleCode: Int) -> String?](locale/identifier(fromwindowslocalecode:).md)
  Returns the locale identifier from a given Windows locale code, or `nil` if it could not be converted.
- [static func windowsLocaleCode(fromIdentifier: String) -> Int?](locale/windowslocalecode(fromidentifier:).md)
  Returns the Windows locale code from a given identifier, or `nil` if it could not be converted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/identifier(fromcomponents:))*