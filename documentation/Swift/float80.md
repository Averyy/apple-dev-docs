# Float80

**Framework**: Swift  
**Kind**: struct

An extended-precision, floating-point value type.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@frozen
struct Float80
```

#### Overview

`Float80` is available on Intel when the target system supports an 80-bit long double type, and unavailable on Apple silicon.

## Topics

### Initializers
- [init()](float80/init.md)
- [init?(Substring)](float80/init(_:)-2iufm.md)
- [init?(exactly: Double)](float80/init(exactly:)-2szlu.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float)](float80/init(exactly:)-6kkqt.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float80)](float80/init(exactly:)-7ol5e.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(nan: Float80.RawSignificand, signaling: Bool)](float80/init(nan:signaling:).md)
  Creates a NaN (“not a number”) value with the specified payload.
### Default Implementations
- [AdditiveArithmetic Implementations](float80/additivearithmetic-implementations.md)
- [BinaryFloatingPoint Implementations](float80/binaryfloatingpoint-implementations.md)
- [Comparable Implementations](float80/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](float80/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](float80/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](float80/customstringconvertible-implementations.md)
- [Equatable Implementations](float80/equatable-implementations.md)
- [ExpressibleByFloatLiteral Implementations](float80/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](float80/expressiblebyintegerliteral-implementations.md)
- [FloatingPoint Implementations](float80/floatingpoint-implementations.md)
- [Hashable Implementations](float80/hashable-implementations.md)
- [LosslessStringConvertible Implementations](float80/losslessstringconvertible-implementations.md)
- [Numeric Implementations](float80/numeric-implementations.md)
- [SignedNumeric Implementations](float80/signednumeric-implementations.md)
- [Strideable Implementations](float80/strideable-implementations.md)
- [TextOutputStreamable Implementations](float80/textoutputstreamable-implementations.md)

## Relationships

### Conforms To
- [AdditiveArithmetic](additivearithmetic.md)
- [BinaryFloatingPoint](binaryfloatingpoint.md)
- [BitwiseCopyable](bitwisecopyable.md)
- [CVarArg](cvararg.md)
- [Comparable](comparable.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomReflectable](customreflectable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Equatable](equatable.md)
- [ExpressibleByFloatLiteral](expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md)
- [FloatingPoint](floatingpoint.md)
- [Hashable](hashable.md)
- [LosslessStringConvertible](losslessstringconvertible.md)
- [Numeric](numeric.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [SignedNumeric](signednumeric.md)
- [Strideable](strideable.md)
- [TextOutputStreamable](textoutputstreamable.md)

## See Also

- [struct Float16](float16.md)
  A half-precision (16b), floating-point value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80)*