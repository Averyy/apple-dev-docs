# EntityURLRepresentation.StringInterpolation

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
- [init(literalCapacity: Int, interpolationCount: Int)](entityurlrepresentation/stringinterpolation/init(literalcapacity:interpolationcount:).md)
  Creates an empty instance ready to be filled with string literal content.
### Instance Methods
- [func appendInterpolation<ValueType, Subject>(Subject)](entityurlrepresentation/stringinterpolation/appendinterpolation(_:)-8cuwi.md)
- [func appendInterpolation(EntityURLRepresentation<Entity>.StringInterpolation.Token)](entityurlrepresentation/stringinterpolation/appendinterpolation(_:)-r282.md)
- [func appendLiteral(String)](entityurlrepresentation/stringinterpolation/appendliteral(_:).md)
  Appends a literal segment to the interpolation.
### Type Aliases
- [EntityURLRepresentation.StringInterpolation.StringLiteralType](entityurlrepresentation/stringinterpolation/stringliteraltype.md)
  The type that should be used for literal segments.
### Enumerations
- [EntityURLRepresentation.StringInterpolation.Token](entityurlrepresentation/stringinterpolation/token.md)

## Relationships

### Conforms To
- [StringInterpolationProtocol](../Swift/StringInterpolationProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityurlrepresentation/stringinterpolation)*