# MTLAttributeFormat

**Framework**: Metal  
**Kind**: enum

Values indicating the organization and format of data for function attributes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLAttributeFormat
```

#### Overview

All data formats are least significant bit first (little-endian). For compute functions which manipulate data consumed by other parts of your app, ensure that the data exposed to the GPU is byte- and bit-aligned correctly to the source format. Your compute function’s attributes can be of a different type than the original source data, so long as they use the same number of bits. For example, your compute function can interpret a 128-bit little-endian integer as [`MTLAttributeFormat.uint4`](mtlattributeformat/uint4.md).

> **Note**:  When manipulating pixel data in a compute function for a future pipeline stage, use an exact match for the underlying pixel data to avoid visual corruption.

## Topics

### Invalid format
- [MTLAttributeFormat.invalid](mtlattributeformat/invalid.md)
  An invalid format.
### Character data formats
- [MTLAttributeFormat.uchar](mtlattributeformat/uchar.md)
  One unsigned 8-bit value.
- [MTLAttributeFormat.uchar2](mtlattributeformat/uchar2.md)
  Two unsigned 8-bit values.
- [MTLAttributeFormat.uchar3](mtlattributeformat/uchar3.md)
  Three unsigned 8-bit values.
- [MTLAttributeFormat.uchar4](mtlattributeformat/uchar4.md)
  Four unsigned 8-bit values.
- [MTLAttributeFormat.char](mtlattributeformat/char.md)
  One signed 8-bit two’s complement value.
- [MTLAttributeFormat.char2](mtlattributeformat/char2.md)
  Two signed 8-bit two’s complement values.
- [MTLAttributeFormat.char3](mtlattributeformat/char3.md)
  Three signed 8-bit two’s complement values.
- [MTLAttributeFormat.char4](mtlattributeformat/char4.md)
  Four signed 8-bit two’s complement values.
- [MTLAttributeFormat.ucharNormalized](mtlattributeformat/ucharnormalized.md)
  One unsigned normalized 8-bit value.
- [MTLAttributeFormat.uchar2Normalized](mtlattributeformat/uchar2normalized.md)
  Two unsigned normalized 8-bit values.
- [MTLAttributeFormat.uchar3Normalized](mtlattributeformat/uchar3normalized.md)
  Three unsigned normalized 8-bit values.
- [MTLAttributeFormat.uchar4Normalized](mtlattributeformat/uchar4normalized.md)
  Four unsigned normalized 8-bit values.
- [MTLAttributeFormat.charNormalized](mtlattributeformat/charnormalized.md)
  One signed normalized 8-bit two’s complement value.
- [MTLAttributeFormat.char2Normalized](mtlattributeformat/char2normalized.md)
  Two signed normalized 8-bit two’s complement values.
- [MTLAttributeFormat.char3Normalized](mtlattributeformat/char3normalized.md)
  Three signed normalized 8-bit two’s complement values.
- [MTLAttributeFormat.char4Normalized](mtlattributeformat/char4normalized.md)
  Four signed normalized 8-bit two’s complement values.
### 16-bit integer data formats
- [MTLAttributeFormat.ushort](mtlattributeformat/ushort.md)
  One unsigned 16-bit value.
- [MTLAttributeFormat.ushort2](mtlattributeformat/ushort2.md)
  Two unsigned 16-bit values.
- [MTLAttributeFormat.ushort3](mtlattributeformat/ushort3.md)
  Three unsigned 16-bit values.
- [MTLAttributeFormat.ushort4](mtlattributeformat/ushort4.md)
  Four unsigned 16-bit values.
- [MTLAttributeFormat.short](mtlattributeformat/short.md)
  One signed 16-bit two’s complement value.
- [MTLAttributeFormat.short2](mtlattributeformat/short2.md)
  Two signed 16-bit two’s complement values.
- [MTLAttributeFormat.short3](mtlattributeformat/short3.md)
  Three signed 16-bit two’s complement values.
- [MTLAttributeFormat.short4](mtlattributeformat/short4.md)
  Four signed 16-bit two’s complement values.
- [MTLAttributeFormat.ushortNormalized](mtlattributeformat/ushortnormalized.md)
  One unsigned normalized 16-bit value.
- [MTLAttributeFormat.ushort2Normalized](mtlattributeformat/ushort2normalized.md)
  Two unsigned normalized 16-bit values
- [MTLAttributeFormat.ushort3Normalized](mtlattributeformat/ushort3normalized.md)
  Three unsigned normalized 16-bit values.
- [MTLAttributeFormat.ushort4Normalized](mtlattributeformat/ushort4normalized.md)
  Four unsigned normalized 16-bit values.
- [MTLAttributeFormat.shortNormalized](mtlattributeformat/shortnormalized.md)
  One signed normalized 16-bit two’s complement value.
- [MTLAttributeFormat.short2Normalized](mtlattributeformat/short2normalized.md)
  Two signed normalized 16-bit two’s complement values.
- [MTLAttributeFormat.short3Normalized](mtlattributeformat/short3normalized.md)
  Three signed normalized 16-bit two’s complement values.
- [MTLAttributeFormat.short4Normalized](mtlattributeformat/short4normalized.md)
  Four signed normalized 16-bit two’s complement values.
### 32-bit integer data formats
- [MTLAttributeFormat.uint](mtlattributeformat/uint.md)
  One unsigned 32-bit value.
- [MTLAttributeFormat.uint2](mtlattributeformat/uint2.md)
  Two unsigned 32-bit values.
- [MTLAttributeFormat.uint3](mtlattributeformat/uint3.md)
  Three unsigned 32-bit values.
- [MTLAttributeFormat.uint4](mtlattributeformat/uint4.md)
  Four unsigned 32-bit values.
- [MTLAttributeFormat.int](mtlattributeformat/int.md)
  One signed 32-bit two’s complement value.
- [MTLAttributeFormat.int2](mtlattributeformat/int2.md)
  Two signed 32-bit two’s complement values.
- [MTLAttributeFormat.int3](mtlattributeformat/int3.md)
  Three signed 32-bit two’s complement values.
- [MTLAttributeFormat.int4](mtlattributeformat/int4.md)
  Four signed 32-bit two’s complement values.
- [MTLAttributeFormat.int1010102Normalized](mtlattributeformat/int1010102normalized.md)
  One packed 32-bit value with four normalized signed two’s complement integer values, arranged as 10 bits, 10 bits, 10 bits, and 2 bits.
- [MTLAttributeFormat.uint1010102Normalized](mtlattributeformat/uint1010102normalized.md)
  One packed 32-bit value with four normalized unsigned integer values, arranged as 10 bits, 10 bits, 10 bits, and 2 bits.
### 16-bit floating point formats
- [MTLAttributeFormat.half](mtlattributeformat/half.md)
  One half-precision floating-point value.
- [MTLAttributeFormat.half2](mtlattributeformat/half2.md)
  Two half-precision floating-point values.
- [MTLAttributeFormat.half3](mtlattributeformat/half3.md)
  Three half-precision floating-point values.
- [MTLAttributeFormat.half4](mtlattributeformat/half4.md)
  Four half-precision floating-point values.
### 32-bit floating point formats
- [MTLAttributeFormat.float](mtlattributeformat/float.md)
  One single-precision floating-point value.
- [MTLAttributeFormat.float2](mtlattributeformat/float2.md)
  Two single-precision floating-point values.
- [MTLAttributeFormat.float3](mtlattributeformat/float3.md)
  Three single-precision floating-point values.
- [MTLAttributeFormat.float4](mtlattributeformat/float4.md)
  Four single-precision floating-point values.
### Pixel data types
- [MTLAttributeFormat.uchar4Normalized_bgra](mtlattributeformat/uchar4normalized_bgra.md)
  Four unsigned normalized 8-bit values, arranged as blue, green, red, and alpha components.
- [MTLAttributeFormat.floatRG11B10](mtlattributeformat/floatrg11b10.md)
  One packed 32-bit value representing pixel data containing 11-bit float red and green channels, and a 10-bit float blue channel.
- [MTLAttributeFormat.floatRGB9E5](mtlattributeformat/floatrgb9e5.md)
  One packed 32-bit value representing pixel data containing 9-bit float red, green, and blue channels, and a 5-bit float shared exponent channel.
### Initializers
- [init?(rawValue: UInt)](mtlattributeformat/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var bufferIndex: Int](mtlattributedescriptor/bufferindex.md)
  The index in the buffer argument table for the buffer that contains the data for this attribute.
- [var offset: Int](mtlattributedescriptor/offset.md)
  The offset, in bytes, from the start of the buffer containing the attribute data to the start of the data itself.
- [var format: MTLAttributeFormat](mtlattributedescriptor/format.md)
  The format of the attribute’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlattributeformat)*