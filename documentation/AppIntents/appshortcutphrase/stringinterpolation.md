# AppShortcutPhrase.StringInterpolation

**Framework**: App Intents  
**Kind**: struct

The type each segment of a string literal containing interpolations should be appended to.

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
struct StringInterpolation
```

#### Overview

The `StringLiteralType` of an interpolation type must match the `StringLiteralType` of the conforming type.

## Topics

### Creating a string interpolation
- [init(literalCapacity: Int, interpolationCount: Int)](appshortcutphrase/stringinterpolation/init(literalcapacity:interpolationcount:).md)
  Creates an empty instance ready to be filled with string literal content.
### Appending values to the string
- [func appendLiteral(String)](appshortcutphrase/stringinterpolation/appendliteral(_:).md)
  Appends a literal segment to the interpolation.
- [func appendInterpolation(AppShortcutPhraseToken)](appshortcutphrase/stringinterpolation/appendinterpolation(_:)-47gqg.md)
### Instance Methods
- [func appendInterpolation<Value, Subject>(Subject)](appshortcutphrase/stringinterpolation/appendinterpolation(_:)-5kcab.md)
### Type Aliases
- [AppShortcutPhrase.StringInterpolation.StringLiteralType](appshortcutphrase/stringinterpolation/stringliteraltype.md)
  The type that should be used for literal segments.

## Relationships

### Conforms To
- [StringInterpolationProtocol](../Swift/StringInterpolationProtocol.md)

## See Also

- [init(String)](appshortcutphrase/init(_:).md)
- [init(stringLiteral: String)](appshortcutphrase/init(stringliteral:).md)
  Creates an instance initialized to the given string value.
- [init(stringInterpolation: AppShortcutPhrase<Intent>.StringInterpolation)](appshortcutphrase/init(stringinterpolation:).md)
  Creates an instance from a string interpolation.
- [enum AppShortcutPhraseToken](appshortcutphrasetoken.md)
  Dynamic values you can include in the spoken phrases that run your shortcut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutphrase/stringinterpolation)*