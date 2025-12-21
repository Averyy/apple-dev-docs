# StringInterpolationProtocol

**Framework**: Swift  
**Kind**: protocol

Represents the contents of a string literal with interpolations while it’s being built up.

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
protocol StringInterpolationProtocol
```

#### Overview

Each `ExpressibleByStringInterpolation` type has an associated `StringInterpolation` type which conforms to `StringInterpolationProtocol`. Swift converts an expression like `"The time is \(time)." as MyString` into a series of statements similar to:

```swift
var interpolation = MyString.StringInterpolation(literalCapacity: 13, 
                                                 interpolationCount: 1)

interpolation.appendLiteral("The time is ")
interpolation.appendInterpolation(time)
interpolation.appendLiteral(".")

MyString(stringInterpolation: interpolation)
```

The `StringInterpolation` type is responsible for collecting the segments passed to its `appendLiteral(_:)` and `appendInterpolation` methods and assembling them into a whole, converting as necessary. Once all of the segments are appended, the interpolation is passed to an `init(stringInterpolation:)` initializer on the type being created, which must extract the accumulated data from the `StringInterpolation`.

In simple cases, you can use `DefaultStringInterpolation` as the interpolation type for types that conform to the `ExpressibleByStringLiteral` protocol. To use the default interpolation, conform a type to `ExpressibleByStringInterpolation` and implement `init(stringLiteral: String)`. Values in interpolations are converted to strings, and then passed to that initializer just like any other string literal.

### Handling String Interpolations

With a custom interpolation type, each interpolated segment is translated into a call to a special `appendInterpolation` method. The contents of the interpolation’s parentheses are treated as the call’s argument list. That argument list can include multiple arguments and argument labels.

The following examples show how string interpolations are translated into calls to `appendInterpolation`:

- `\(x)` translates to `appendInterpolation(x)`
- `\(x, y)` translates to `appendInterpolation(x, y)`
- `\(foo: x)` translates to `appendInterpolation(foo: x)`
- `\(x, foo: y)` translates to `appendInterpolation(x, foo: y)`

The `appendInterpolation` methods in your custom type must be mutating instance methods that return `Void`. This code shows a custom interpolation type’s declaration of an `appendInterpolation` method that provides special validation for user input:

```swift
extension MyString.StringInterpolation {
    mutating func appendInterpolation(validating input: String) {
        // Perform validation of `input` and store for later use
    }
}
```

To use this interpolation method, create a string literal with an interpolation using the `validating` parameter label.

```swift
let userInput = readLine() ?? ""
let myString = "The user typed '\(validating: userInput)'." as MyString
```

`appendInterpolation` methods support virtually all features of methods: they can have any number of parameters, can specify labels for any or all of their parameters, can provide default values, can have variadic parameters, and can have parameters with generic types. Most importantly, they can be overloaded, so a type that conforms to `StringInterpolationProtocol` can provide several different `appendInterpolation` methods with different behaviors. An `appendInterpolation` method can also throw; when a user writes a literal with one of these interpolations, they must mark the string literal with `try` or one of its variants.

## Topics

### Associated Types
- [associatedtype StringLiteralType : _ExpressibleByBuiltinStringLiteral](stringinterpolationprotocol/stringliteraltype.md)
  The type that should be used for literal segments.
### Initializers
- [init(literalCapacity: Int, interpolationCount: Int)](stringinterpolationprotocol/init(literalcapacity:interpolationcount:).md)
  Creates an empty instance ready to be filled with string literal content.
### Instance Methods
- [func appendLiteral(Self.StringLiteralType)](stringinterpolationprotocol/appendliteral(_:).md)
  Appends a literal segment to the interpolation.

## Relationships

### Conforming Types
- [DefaultStringInterpolation](defaultstringinterpolation.md)

## See Also

- [protocol ExpressibleByStringLiteral](expressiblebystringliteral.md)
  A type that can be initialized with a string literal.
- [protocol ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md)
  A type that can be initialized with a string literal containing a single extended grapheme cluster.
- [protocol ExpressibleByUnicodeScalarLiteral](expressiblebyunicodescalarliteral.md)
  A type that can be initialized with a string literal containing a single Unicode scalar value.
- [protocol ExpressibleByStringInterpolation](expressiblebystringinterpolation.md)
  A type that can be initialized by string interpolation with a string literal that includes expressions.
- [struct DefaultStringInterpolation](defaultstringinterpolation.md)
  Represents a string literal with interpolations while it’s being built up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringinterpolationprotocol)*