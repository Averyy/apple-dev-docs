# Float16

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

A half-precision (16-bit), floating-point value type.

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

On macOS, `Float16` is only available when targeting Apple silicon. On other supported platforms, `Float16` is available for all architectures. If the specified target supports 16-bit floating point arithmetic directly, those instructions will be used; otherwise Float16 arithmetic will be emulated by the swift compiler and runtime.

## Topics

### Initializers
- [init()](./float16/init%28%29.md)
- [init?(Substring)](./float16/init%28_%29-5x2si.md)
- [init(Float16)](./float16/init%28_%29-77b3g.md)
  Creates a new instance initialized to the given value.
- [init(bitPattern: UInt16)](./float16/init%28bitpattern%29.md)
  Creates a new value with the given bit pattern.
- [init?(exactly: Float16)](./float16/init%28exactly%29-27ijx.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Double)](./float16/init%28exactly%29-4hyr3.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float)](./float16/init%28exactly%29-8rmd7.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(nan: Float16.RawSignificand, signaling: Bool)](./float16/init%28nan,signaling%29.md)
  Creates a NaN (“not a number”) value with the specified payload.
### Instance Properties
- [var bitPattern: UInt16](./float16/bitpattern.md)
  The bit pattern of the value’s encoding.
### Default Implementations
- [AdditiveArithmetic Implementations](./float16/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](./float16/atomicrepresentable-implementations.md)
- [BinaryFloatingPoint Implementations](./float16/binaryfloatingpoint-implementations.md)
- [Comparable Implementations](./float16/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](./float16/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](./float16/customstringconvertible-implementations.md)
- [Decodable Implementations](./float16/decodable-implementations.md)
- [Encodable Implementations](./float16/encodable-implementations.md)
- [Equatable Implementations](./float16/equatable-implementations.md)
- [ExpressibleByFloatLiteral Implementations](./float16/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](./float16/expressiblebyintegerliteral-implementations.md)
- [FloatingPoint Implementations](./float16/floatingpoint-implementations.md)
- [Hashable Implementations](./float16/hashable-implementations.md)
- [LosslessStringConvertible Implementations](./float16/losslessstringconvertible-implementations.md)
- [Numeric Implementations](./float16/numeric-implementations.md)
- [OperationParameter Implementations](./float16/operationparameter-implementations.md)
- [SIMDScalar Implementations](./float16/simdscalar-implementations.md)
- [SignedNumeric Implementations](./float16/signednumeric-implementations.md)
- [Strideable Implementations](./float16/strideable-implementations.md)
- [TextOutputStreamable Implementations](./float16/textoutputstreamable-implementations.md)

## Relationships

### Conforms To
- [AdditiveArithmetic](./additivearithmetic.md)
- [AtomicRepresentable](../Synchronization/atomicrepresentable.md)
- [BNNSGraph.Builder.OperationParameter](../Accelerate/bnnsgraph/builder/operationparameter.md)
- [BNNSScalar](../Accelerate/bnnsscalar.md)
- [BinaryFloatingPoint](./binaryfloatingpoint.md)
- [BitwiseCopyable](./bitwisecopyable.md)
- [Comparable](./comparable.md)
- [ConvertibleFromBytes](./convertiblefrombytes.md)
- [ConvertibleToBytes](./convertibletobytes.md)
- [Copyable](./copyable.md)
- [CustomDebugStringConvertible](./customdebugstringconvertible.md)
- [CustomStringConvertible](./customstringconvertible.md)
- [Decodable](./decodable.md)
- [Encodable](./encodable.md)
- [Equatable](./equatable.md)
- [Escapable](./escapable.md)
- [ExpressibleByFloatLiteral](./expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](./expressiblebyintegerliteral.md)
- [FloatingPoint](./floatingpoint.md)
- [Hashable](./hashable.md)
- [LosslessStringConvertible](./losslessstringconvertible.md)
- [MLShapedArrayScalar](../CoreML/mlshapedarrayscalar.md)
- [MLTensorScalar](../CoreML/mltensorscalar.md)
- [Numeric](./numeric.md)
- [Plottable](../Charts/plottable.md)
- [PrimitivePlottableProtocol](../Charts/primitiveplottableprotocol.md)
- [SIMDScalar](./simdscalar.md)
- [Sendable](./sendable.md)
- [SendableMetatype](./sendablemetatype.md)
- [SignedNumeric](./signednumeric.md)
- [Strideable](./strideable.md)
- [TextOutputStreamable](./textoutputstreamable.md)
- [USDPrim.Attribute.Value](../USDKit/usdprim/attribute/value.md)
- [USDStage.Object.MetadataValue](../USDKit/usdstage/object/metadatavalue.md)
- [USDValueProtocol](../USDKit/usdvalueprotocol.md)

## See Also

### Floating-Point Values
- [struct Float80](./float80.md)
  An extended-precision, floating-point value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16)*