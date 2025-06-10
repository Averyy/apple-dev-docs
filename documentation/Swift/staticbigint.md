# StaticBigInt

**Framework**: Swift  
**Kind**: struct

An immutable arbitrary-precision signed integer.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
@frozen
struct StaticBigInt
```

#### Overview

`StaticBigInt` is primarily intended to be used as the associated type of an `ExpressibleByIntegerLiteral` conformance.

```swift
extension UInt256: ExpressibleByIntegerLiteral {
    public init(integerLiteral value: StaticBigInt) {
        precondition(
            value.signum() >= 0 && value.bitWidth <= 1 + Self.bitWidth,
            "integer overflow: '\(value)' as '\(Self.self)'"
        )
        self.words = Words()
        for wordIndex in 0..<Words.count {
            self.words[wordIndex] = value[wordIndex]
        }
    }
}
```

## Topics

### Instance Properties
- [var bitWidth: Int](staticbigint/bitwidth.md)
  Returns the minimal number of bits in this value’s binary representation, including the sign bit, and excluding the sign extension.
### Instance Methods
- [func signum() -> Int](staticbigint/signum.md)
  Indicates the value’s sign.
### Subscripts
- [subscript(Int) -> UInt](staticbigint/subscript(_:).md)
  Returns a 32-bit or 64-bit word of this value’s binary representation.
### Type Aliases
- [StaticBigInt.IntegerLiteralType](staticbigint/integerliteraltype.md)
  A type that represents an integer literal.
### Default Implementations
- [CustomDebugStringConvertible Implementations](staticbigint/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](staticbigint/customreflectable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](staticbigint/expressiblebyintegerliteral-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomReflectable](customreflectable.md)
- [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [protocol ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md)
  A type that can be initialized with an integer literal.
- [protocol ExpressibleByFloatLiteral](expressiblebyfloatliteral.md)
  A type that can be initialized with a floating-point literal.
- [protocol ExpressibleByBooleanLiteral](expressiblebybooleanliteral.md)
  A type that can be initialized with the Boolean literals `true` and `false`.
- [protocol ExpressibleByNilLiteral](expressiblebynilliteral.md)
  A type that can be initialized using the nil literal, `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/staticbigint)*