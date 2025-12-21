# ExpressibleByUnicodeScalarLiteral

**Framework**: Swift  
**Kind**: protocol

A type that can be initialized with a string literal containing a single Unicode scalar value.

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
protocol ExpressibleByUnicodeScalarLiteral
```

#### Overview

The `String`, `StaticString`, `Character`, and `Unicode.Scalar` types all conform to the `ExpressibleByUnicodeScalarLiteral` protocol. You can initialize a variable of any of these types using a string literal that holds a single Unicode scalar.

```swift
let ñ: Unicode.Scalar = "ñ"
print(ñ)
// Prints "ñ"
```

### Conforming to Expressiblebyunicodescalarliteral

To add `ExpressibleByUnicodeScalarLiteral` conformance to your custom type, implement the required initializer.

## Topics

### Associated Types
- [associatedtype UnicodeScalarLiteralType : _ExpressibleByBuiltinUnicodeScalarLiteral](expressiblebyunicodescalarliteral/unicodescalarliteraltype.md)
  A type that represents a Unicode scalar literal.
### Initializers
- [init(unicodeScalarLiteral: Self.UnicodeScalarLiteralType)](expressiblebyunicodescalarliteral/init(unicodescalarliteral:).md)
  Creates an instance initialized to the given value.

## Relationships

### Inherited By
- [ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringInterpolation](expressiblebystringinterpolation.md)
- [ExpressibleByStringLiteral](expressiblebystringliteral.md)
- [StringProtocol](stringprotocol.md)
### Conforming Types
- [Character](character.md)
- [StaticString](staticstring.md)
- [String](string.md)
- [String.LocalizationValue](string/localizationvalue.md)
- [Substring](substring.md)
- [Unicode.Scalar](unicode/scalar.md)

## See Also

- [protocol ExpressibleByStringLiteral](expressiblebystringliteral.md)
  A type that can be initialized with a string literal.
- [protocol ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md)
  A type that can be initialized with a string literal containing a single extended grapheme cluster.
- [protocol ExpressibleByStringInterpolation](expressiblebystringinterpolation.md)
  A type that can be initialized by string interpolation with a string literal that includes expressions.
- [protocol StringInterpolationProtocol](stringinterpolationprotocol.md)
  Represents the contents of a string literal with interpolations while it’s being built up.
- [struct DefaultStringInterpolation](defaultstringinterpolation.md)
  Represents a string literal with interpolations while it’s being built up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/expressiblebyunicodescalarliteral)*