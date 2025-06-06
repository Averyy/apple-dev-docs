# DefaultStringInterpolation

**Framework**: Swift  
**Kind**: struct

Represents a string literal with interpolations while it is being built up.

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
@frozen
struct DefaultStringInterpolation
```

#### Overview

Do not create an instance of this type directly. It is used by the compiler when you create a string using string interpolation. Instead, use string interpolation to create a new string by including values, literals, variables, or expressions enclosed in parentheses, prefixed by a backslash (`\(`…`)`).

```swift
let price = 2
let number = 3
let message = """
              If one cookie costs \(price) dollars, \
              \(number) cookies cost \(price * number) dollars.
              """
print(message)
// Prints "If one cookie costs 2 dollars, 3 cookies cost 6 dollars."
```

When implementing an `ExpressibleByStringInterpolation` conformance, set the `StringInterpolation` associated type to `DefaultStringInterpolation` to get the same interpolation behavior as Swift’s built-in `String` type and construct a `String` with the results. If you don’t want the default behavior or don’t want to construct a `String`, use a custom type conforming to `StringInterpolationProtocol` instead.

### Extending Default String Interpolation Behavior

Code outside the standard library can extend string interpolation on `String` and many other common types by extending `DefaultStringInterpolation` and adding an `appendInterpolation(...)` method. For example:

```swift
extension DefaultStringInterpolation {
    fileprivate mutating func appendInterpolation(
             escaped value: String, asASCII forceASCII: Bool = false) {
        for char in value.unicodeScalars {
            appendInterpolation(char.escaped(asASCII: forceASCII))
        }
    }
}

print("Escaped string: \(escaped: string)")
```

See `StringInterpolationProtocol` for details on `appendInterpolation` methods.

`DefaultStringInterpolation` extensions should add only `mutating` members and should not copy `self` or capture it in an escaping closure.

## Topics

### Initializers
- [init(literalCapacity: Int, interpolationCount: Int)](defaultstringinterpolation/init(literalcapacity:interpolationcount:).md)
  Creates a string interpolation with storage pre-sized for a literal with the indicated attributes.
### Instance Methods
- [func appendInterpolation<T>(T)](defaultstringinterpolation/appendinterpolation(_:)-2bzja.md)
  Interpolates the given value’s textual representation into the string literal being created.
- [func appendInterpolation<T>(T)](defaultstringinterpolation/appendinterpolation(_:)-468zr.md)
  Interpolates the given value’s textual representation into the string literal being created.
- [func appendInterpolation<T>(T)](defaultstringinterpolation/appendinterpolation(_:)-6kx4d.md)
  Interpolates the given value’s textual representation into the string literal being created.
- [func appendInterpolation<T>(T)](defaultstringinterpolation/appendinterpolation(_:)-8x6aw.md)
  Interpolates the given value’s textual representation into the string literal being created.
- [func appendInterpolation(any Any.Type)](defaultstringinterpolation/appendinterpolation(_:)-jfy9.md)
- [func appendLiteral(String)](defaultstringinterpolation/appendliteral(_:).md)
  Appends a literal segment of a string interpolation.
### Type Aliases
- [DefaultStringInterpolation.StringLiteralType](defaultstringinterpolation/stringliteraltype.md)
  The type that should be used for literal segments.
### Default Implementations
- [CustomStringConvertible Implementations](defaultstringinterpolation/customstringconvertible-implementations.md)
- [TextOutputStream Implementations](defaultstringinterpolation/textoutputstream-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Sendable](sendable.md)
- [StringInterpolationProtocol](stringinterpolationprotocol.md)
- [TextOutputStream](textoutputstream.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/defaultstringinterpolation)*