# NegativeAppShortcutPhrase.StringInterpolation

**Framework**: App Intents  
**Kind**: struct

A string you construct using literal values, content from intent parameters, and other interpolated values.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct StringInterpolation
```

## Topics

### Initializers
- [init(literalCapacity: Int, interpolationCount: Int)](negativeappshortcutphrase/stringinterpolation/init(literalcapacity:interpolationcount:).md)
  Creates an empty instance ready to be filled with string literal content.
### Instance Methods
- [func appendInterpolation(AppShortcutPhraseToken)](negativeappshortcutphrase/stringinterpolation/appendinterpolation(_:).md)
- [func appendLiteral(String)](negativeappshortcutphrase/stringinterpolation/appendliteral(_:).md)
  Appends a literal segment to the interpolation.
### Type Aliases
- [NegativeAppShortcutPhrase.StringInterpolation.StringLiteralType](negativeappshortcutphrase/stringinterpolation/stringliteraltype.md)
  The type that should be used for literal segments.

## Relationships

### Conforms To
- [StringInterpolationProtocol](../Swift/StringInterpolationProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/negativeappshortcutphrase/stringinterpolation)*