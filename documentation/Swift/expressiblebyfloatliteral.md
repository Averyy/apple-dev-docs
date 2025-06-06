# ExpressibleByFloatLiteral

**Framework**: Swift  
**Kind**: protocol

A type that can be initialized with a floating-point literal.

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
protocol ExpressibleByFloatLiteral
```

#### Overview

The standard library floating-point types—`Float`, `Double`, and `Float80` where available—all conform to the `ExpressibleByFloatLiteral` protocol. You can initialize a variable or constant of any of these types by assigning a floating-point literal.

```swift
// Type inferred as 'Double'
let threshold = 6.0

// An array of 'Double'
let measurements = [2.2, 4.1, 3.65, 4.2, 9.1]
```

### Conforming to Expressiblebyfloatliteral

To add `ExpressibleByFloatLiteral` conformance to your custom type, implement the required initializer.

## Topics

### Associated Types
- [associatedtype FloatLiteralType : _ExpressibleByBuiltinFloatLiteral](expressiblebyfloatliteral/floatliteraltype.md)
  A type that represents a floating-point literal.
### Initializers
- [init(floatLiteral: Self.FloatLiteralType)](expressiblebyfloatliteral/init(floatliteral:).md)
  Creates an instance initialized to the specified floating-point value.

## Relationships

### Inherited By
- [BinaryFloatingPoint](binaryfloatingpoint.md)
### Conforming Types
- [Double](double.md)
- [Float](float.md)
- [Float16](float16.md)
- [Float80](float80.md)

## See Also

- [protocol ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md)
  A type that can be initialized with an integer literal.
- [protocol ExpressibleByBooleanLiteral](expressiblebybooleanliteral.md)
  A type that can be initialized with the Boolean literals `true` and `false`.
- [protocol ExpressibleByNilLiteral](expressiblebynilliteral.md)
  A type that can be initialized using the nil literal, `nil`.
- [struct StaticBigInt](staticbigint.md)
  An immutable arbitrary-precision signed integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/expressiblebyfloatliteral)*