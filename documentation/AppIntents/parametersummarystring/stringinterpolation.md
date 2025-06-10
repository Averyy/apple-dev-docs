# ParameterSummaryString.StringInterpolation

**Framework**: App Intents  
**Kind**: struct

The type each segment of a string literal containing interpolations should be appended to.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct StringInterpolation
```

#### Overview

The `StringLiteralType` of an interpolation type must match the `StringLiteralType` of the conforming type.

## Topics

### Initializers
- [init(literalCapacity: Int, interpolationCount: Int)](parametersummarystring/stringinterpolation/init(literalcapacity:interpolationcount:).md)
  Creates an empty instance ready to be filled with string literal content.
### Instance Methods
- [func appendInterpolation<ValueType, Subject>(Subject)](parametersummarystring/stringinterpolation/appendinterpolation(_:).md)
- [func appendLiteral(String)](parametersummarystring/stringinterpolation/appendliteral(_:).md)
  Appends a literal segment to the interpolation.
### Type Aliases
- [ParameterSummaryString.StringInterpolation.StringLiteralType](parametersummarystring/stringinterpolation/stringliteraltype.md)
  The type that should be used for literal segments.

## Relationships

### Conforms To
- [StringInterpolationProtocol](../Swift/StringInterpolationProtocol.md)

## See Also

- [init(String)](parametersummarystring/init(_:).md)
- [init(stringLiteral: String)](parametersummarystring/init(stringliteral:).md)
  Creates an instance initialized to the given string value.
- [init(stringInterpolation: ParameterSummaryString<Intent>.StringInterpolation)](parametersummarystring/init(stringinterpolation:).md)
  Creates an instance from a string interpolation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummarystring/stringinterpolation)*