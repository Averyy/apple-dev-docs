# ExpressibleByNilLiteral

**Framework**: Swift  
**Kind**: protocol

A type that can be initialized using the nil literal, `nil`.

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
protocol ExpressibleByNilLiteral : ~Copyable, ~Escapable
```

#### Overview

`nil` has a specific meaning in Swift—the absence of a value. Only the `Optional` type conforms to `ExpressibleByNilLiteral`. `ExpressibleByNilLiteral` conformance for types that use `nil` for other purposes is discouraged.

## Topics

### Initializers
- [init(nilLiteral: ())](expressiblebynilliteral/init(nilliteral:).md)
  Creates an instance initialized with `nil`.

## Relationships

### Conforming Types
- [Optional](optional.md)

## See Also

- [protocol ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md)
  A type that can be initialized with an integer literal.
- [protocol ExpressibleByFloatLiteral](expressiblebyfloatliteral.md)
  A type that can be initialized with a floating-point literal.
- [protocol ExpressibleByBooleanLiteral](expressiblebybooleanliteral.md)
  A type that can be initialized with the Boolean literals `true` and `false`.
- [struct StaticBigInt](staticbigint.md)
  An immutable arbitrary-precision signed integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/expressiblebynilliteral)*