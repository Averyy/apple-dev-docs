# Initialization with Literals

**Framework**: Swift

Allow values of your type to be expressed using different kinds of literals.

## Topics

### Collection Literals
- [protocol ExpressibleByArrayLiteral](expressiblebyarrayliteral.md)
  A type that can be initialized using an array literal.
- [protocol ExpressibleByDictionaryLiteral](expressiblebydictionaryliteral.md)
  A type that can be initialized using a dictionary literal.
### Value Literals
- [protocol ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md)
  A type that can be initialized with an integer literal.
- [protocol ExpressibleByFloatLiteral](expressiblebyfloatliteral.md)
  A type that can be initialized with a floating-point literal.
- [protocol ExpressibleByBooleanLiteral](expressiblebybooleanliteral.md)
  A type that can be initialized with the Boolean literals `true` and `false`.
- [protocol ExpressibleByNilLiteral](expressiblebynilliteral.md)
  A type that can be initialized using the nil literal, `nil`.
- [struct StaticBigInt](staticbigint.md)
  An immutable arbitrary-precision signed integer.
### String Literals
- [protocol ExpressibleByStringLiteral](expressiblebystringliteral.md)
  A type that can be initialized with a string literal.
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
### Default Types for Literals
- [Default Literal Types](default-literal-types.md)
  Type aliases representing the concrete type that a literal takes when no other type information is provided.

## See Also

- [Basic Behaviors](basic-behaviors.md)
  Use your custom types in operations that depend on testing for equality or order and as members of sets and dictionaries.
- [Encoding, Decoding, and Serialization](encoding-decoding-and-serialization.md)
  Serialize and deserialize instances of your types with implicit or customized encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/initialization-with-literals)*