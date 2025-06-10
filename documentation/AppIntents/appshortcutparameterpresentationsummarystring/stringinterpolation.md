# AppShortcutParameterPresentationSummaryString.StringInterpolation

**Framework**: App Intents  
**Kind**: struct

The type each segment of a string literal containing interpolations should be appended to.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
struct StringInterpolation
```

#### Overview

The `StringLiteralType` of an interpolation type must match the `StringLiteralType` of the conforming type.

## Topics

### Initializers
- [init(literalCapacity: Int, interpolationCount: Int)](appshortcutparameterpresentationsummarystring/stringinterpolation/init(literalcapacity:interpolationcount:).md)
  Creates an empty instance ready to be filled with string literal content.
### Instance Methods
- [func appendInterpolation(ParameterKeyPath)](appshortcutparameterpresentationsummarystring/stringinterpolation/appendinterpolation(_:).md)
- [func appendLiteral(String)](appshortcutparameterpresentationsummarystring/stringinterpolation/appendliteral(_:).md)
  Appends a literal segment to the interpolation.
### Type Aliases
- [AppShortcutParameterPresentationSummaryString.StringInterpolation.StringLiteralType](appshortcutparameterpresentationsummarystring/stringinterpolation/stringliteraltype.md)
  The type that should be used for literal segments.

## Relationships

### Conforms To
- [StringInterpolationProtocol](../Swift/StringInterpolationProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutparameterpresentationsummarystring/stringinterpolation)*