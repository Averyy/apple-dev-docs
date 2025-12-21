# ExpressibleByStringLiteral

**Framework**: Swift  
**Kind**: protocol

A type that can be initialized with a string literal.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol ExpressibleByStringLiteral : ExpressibleByExtendedGraphemeClusterLiteral
```

#### Overview

The `String` and `StaticString` types conform to the `ExpressibleByStringLiteral` protocol. You can initialize a variable or constant of either of these types using a string literal of any length.

```swift
let picnicGuest = "Deserving porcupine"
```

### Conforming to Expressiblebystringliteral

To add `ExpressibleByStringLiteral` conformance to your custom type, implement the required initializer.

## Topics

### Associated Types
- [associatedtype StringLiteralType : _ExpressibleByBuiltinStringLiteral](expressiblebystringliteral/stringliteraltype.md)
  A type that represents a string literal.
### Initializers
- [init(stringLiteral: Self.StringLiteralType)](expressiblebystringliteral/init(stringliteral:).md)
  Creates an instance initialized to the given string value.

## Relationships

### Inherits From
- [ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByUnicodeScalarLiteral](expressiblebyunicodescalarliteral.md)
### Inherited By
- [ExpressibleByStringInterpolation](expressiblebystringinterpolation.md)
- [StringProtocol](stringprotocol.md)
### Conforming Types
- [StaticString](staticstring.md)
- [String](string.md)
- [String.LocalizationValue](string/localizationvalue.md)
- [Substring](substring.md)

## See Also

- [protocol ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md)
  A type that can be initialized with a string literal containing a single extended grapheme cluster.
- [protocol ExpressibleByUnicodeScalarLiteral](expressiblebyunicodescalarliteral.md)
  A type that can be initialized with a string literal containing a single Unicode scalar value.
- [protocol ExpressibleByStringInterpolation](expressiblebystringinterpolation.md)
  A type that can be initialized by string interpolation with a string literal that includes expressions.
- [protocol StringInterpolationProtocol](stringinterpolationprotocol.md)
  Represents the contents of a string literal with interpolations while it’s being built up.
- [struct DefaultStringInterpolation](defaultstringinterpolation.md)
  Represents a string literal with interpolations while it’s being built up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/expressiblebystringliteral)*