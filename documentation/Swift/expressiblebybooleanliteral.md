# ExpressibleByBooleanLiteral

**Framework**: Swift  
**Kind**: protocol

A type that can be initialized with the Boolean literals `true` and `false`.

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
protocol ExpressibleByBooleanLiteral
```

#### Overview

`Bool`, `DarwinBoolean`, `ObjCBool`, and `WindowsBool` are treated as Boolean values. Expanding this set to include types that represent more than simple Boolean values is discouraged.

To add `ExpressibleByBooleanLiteral` conformance to your custom type, implement the `init(booleanLiteral:)` initializer that creates an instance of your type with the given Boolean value.

## Topics

### Associated Types
- [associatedtype BooleanLiteralType : _ExpressibleByBuiltinBooleanLiteral](expressiblebybooleanliteral/booleanliteraltype.md)
  A type that represents a Boolean literal, such as `Bool`.
### Initializers
- [init(booleanLiteral: Self.BooleanLiteralType)](expressiblebybooleanliteral/init(booleanliteral:).md)
  Creates an instance initialized to the given Boolean value.

## Relationships

### Conforming Types
- [Bool](bool.md)

## See Also

- [protocol ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md)
  A type that can be initialized with an integer literal.
- [protocol ExpressibleByFloatLiteral](expressiblebyfloatliteral.md)
  A type that can be initialized with a floating-point literal.
- [protocol ExpressibleByNilLiteral](expressiblebynilliteral.md)
  A type that can be initialized using the nil literal, `nil`.
- [struct StaticBigInt](staticbigint.md)
  An immutable arbitrary-precision signed integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/expressiblebybooleanliteral)*