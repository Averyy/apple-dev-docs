# AppShortcutParameterPresentationTitleString.StringInterpolation

**Framework**: App Intents  
**Kind**: struct

The type each segment of a string literal containing interpolations should be appended to.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+
- Unknown ?+ - Deprecated
- visionOS 1.0+

## Declaration

```swift
struct StringInterpolation
```

#### Overview

The `StringLiteralType` of an interpolation type must match the `StringLiteralType` of the conforming type.

## Topics

### Initializers
- [init(literalCapacity: Int, interpolationCount: Int)](appshortcutparameterpresentationtitlestring/stringinterpolation/init(literalcapacity:interpolationcount:).md)
  Creates an empty instance ready to be filled with string literal content.
### Instance Methods
- [func appendInterpolation(ParameterKeyPath)](appshortcutparameterpresentationtitlestring/stringinterpolation/appendinterpolation(_:).md)
- [func appendLiteral(String)](appshortcutparameterpresentationtitlestring/stringinterpolation/appendliteral(_:).md)
  Appends a literal segment to the interpolation.
### Type Aliases
- [AppShortcutParameterPresentationTitleString.StringInterpolation.StringLiteralType](appshortcutparameterpresentationtitlestring/stringinterpolation/stringliteraltype.md)
  The type that should be used for literal segments.

## Relationships

### Conforms To
- [StringInterpolationProtocol](../Swift/StringInterpolationProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutparameterpresentationtitlestring/stringinterpolation)*