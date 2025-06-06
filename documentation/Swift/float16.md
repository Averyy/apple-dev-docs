# Float16

**Framework**: Swift  
**Kind**: struct

A half-precision (16b), floating-point value type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@frozen
struct Float16
```

#### Overview

`Float16` is available on Apple silicon, and unavailable on Intel when targeting macOS.

## Topics

### Initializers
- [init()](float16/init.md)
- [init?(Substring)](float16/init(_:)-5x2si.md)
- [init(Float16)](float16/init(_:)-77b3g.md)
  Creates a new instance initialized to the given value.
- [init(bitPattern: UInt16)](float16/init(bitpattern:).md)
  Creates a new value with the given bit pattern.
- [init?(exactly: Float16)](float16/init(exactly:)-27ijx.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Double)](float16/init(exactly:)-4hyr3.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float)](float16/init(exactly:)-8rmd7.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(nan: Float16.RawSignificand, signaling: Bool)](float16/init(nan:signaling:).md)
  Creates a NaN (“not a number”) value with the specified payload.
### Instance Properties
- [var bitPattern: UInt16](float16/bitpattern.md)
  The bit pattern of the value’s encoding.
### Default Implementations
- [AdditiveArithmetic Implementations](float16/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](float16/atomicrepresentable-implementations.md)
- [BinaryFloatingPoint Implementations](float16/binaryfloatingpoint-implementations.md)
- [Comparable Implementations](float16/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](float16/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](float16/customstringconvertible-implementations.md)
- [Decodable Implementations](float16/decodable-implementations.md)
- [Encodable Implementations](float16/encodable-implementations.md)
- [Equatable Implementations](float16/equatable-implementations.md)
- [ExpressibleByFloatLiteral Implementations](float16/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](float16/expressiblebyintegerliteral-implementations.md)
- [FloatingPoint Implementations](float16/floatingpoint-implementations.md)
- [Hashable Implementations](float16/hashable-implementations.md)
- [LosslessStringConvertible Implementations](float16/losslessstringconvertible-implementations.md)
- [Numeric Implementations](float16/numeric-implementations.md)
- [SIMDScalar Implementations](float16/simdscalar-implementations.md)
- [SignedNumeric Implementations](float16/signednumeric-implementations.md)
- [Strideable Implementations](float16/strideable-implementations.md)
- [TextOutputStreamable Implementations](float16/textoutputstreamable-implementations.md)

## Relationships

### Conforms To
- [AdditiveArithmetic](additivearithmetic.md)
- [AtomicRepresentable](../synchronization/atomicrepresentable.md)
- [BNNSScalar](../Accelerate/BNNSScalar.md)
- [BinaryFloatingPoint](binaryfloatingpoint.md)
- [BitwiseCopyable](bitwisecopyable.md)
- [Comparable](comparable.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [ExpressibleByFloatLiteral](expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md)
- [FloatingPoint](floatingpoint.md)
- [Hashable](hashable.md)
- [LosslessStringConvertible](losslessstringconvertible.md)
- [MLShapedArrayScalar](../CoreML/MLShapedArrayScalar.md)
- [MLTensorScalar](../CoreML/MLTensorScalar.md)
- [Numeric](numeric.md)
- [Plottable](../Charts/Plottable.md)
- [PrimitivePlottableProtocol](../Charts/PrimitivePlottableProtocol.md)
- [SIMDScalar](simdscalar.md)
- [Sendable](sendable.md)
- [SignedNumeric](signednumeric.md)
- [Strideable](strideable.md)
- [TextOutputStreamable](textoutputstreamable.md)

## See Also

- [struct Float80](float80.md)
  An extended-precision, floating-point value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16)*