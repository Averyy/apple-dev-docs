# EnumURLRepresentation.StringInterpolation

**Framework**: App Intents  
**Kind**: struct

The type each segment of a string literal containing interpolations should be appended to.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct StringInterpolation
```

#### Overview

The `StringLiteralType` of an interpolation type must match the `StringLiteralType` of the conforming type.

## Topics

### Initializers
- [init(literalCapacity: Int, interpolationCount: Int)](enumurlrepresentation/stringinterpolation/init(literalcapacity:interpolationcount:).md)
  Creates an empty instance ready to be filled with string literal content.
### Instance Methods
- [func appendInterpolation(Enum)](enumurlrepresentation/stringinterpolation/appendinterpolation(_:)-70nx3.md)
- [func appendInterpolation(EnumURLRepresentation<Enum>.StringInterpolation.Token)](enumurlrepresentation/stringinterpolation/appendinterpolation(_:)-r06h.md)
- [func appendLiteral(String)](enumurlrepresentation/stringinterpolation/appendliteral(_:).md)
  Appends a literal segment to the interpolation.
### Type Aliases
- [EnumURLRepresentation.StringInterpolation.StringLiteralType](enumurlrepresentation/stringinterpolation/stringliteraltype.md)
  The type that should be used for literal segments.
### Enumerations
- [EnumURLRepresentation.StringInterpolation.Token](enumurlrepresentation/stringinterpolation/token.md)

## Relationships

### Conforms To
- [StringInterpolationProtocol](../Swift/StringInterpolationProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/enumurlrepresentation/stringinterpolation)*