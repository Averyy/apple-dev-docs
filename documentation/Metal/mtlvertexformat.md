# MTLVertexFormat

**Framework**: Metal  
**Kind**: enum

Values that specify the organization of function vertex data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MTLVertexFormat
```

## Topics

### Vertex formats
- [MTLVertexFormat.invalid](mtlvertexformat/invalid.md)
  An invalid vertex format.
- [MTLVertexFormat.uchar](mtlvertexformat/uchar.md)
  One unsigned 8-bit value.
- [MTLVertexFormat.uchar2](mtlvertexformat/uchar2.md)
  Two unsigned 8-bit values.
- [MTLVertexFormat.uchar3](mtlvertexformat/uchar3.md)
  Three unsigned 8-bit values.
- [MTLVertexFormat.uchar4](mtlvertexformat/uchar4.md)
  Four unsigned 8-bit values.
- [MTLVertexFormat.char](mtlvertexformat/char.md)
  One signed 8-bit two’s complement value.
- [MTLVertexFormat.char2](mtlvertexformat/char2.md)
  Two signed 8-bit two’s complement values.
- [MTLVertexFormat.char3](mtlvertexformat/char3.md)
  Three signed 8-bit two’s complement values.
- [MTLVertexFormat.char4](mtlvertexformat/char4.md)
  Four signed 8-bit two’s complement values.
- [MTLVertexFormat.ucharNormalized](mtlvertexformat/ucharnormalized.md)
  One unsigned normalized 8-bit value.
- [MTLVertexFormat.uchar2Normalized](mtlvertexformat/uchar2normalized.md)
  Two unsigned normalized 8-bit values.
- [MTLVertexFormat.uchar3Normalized](mtlvertexformat/uchar3normalized.md)
  Three unsigned normalized 8-bit values.
- [MTLVertexFormat.uchar4Normalized](mtlvertexformat/uchar4normalized.md)
  Four unsigned normalized 8-bit values.
- [MTLVertexFormat.charNormalized](mtlvertexformat/charnormalized.md)
  One signed normalized 8-bit two’s complement value.
- [MTLVertexFormat.char2Normalized](mtlvertexformat/char2normalized.md)
  Two signed normalized 8-bit two’s complement values.
- [MTLVertexFormat.char3Normalized](mtlvertexformat/char3normalized.md)
  Three signed normalized 8-bit two’s complement values.
- [MTLVertexFormat.char4Normalized](mtlvertexformat/char4normalized.md)
  Four signed normalized 8-bit two’s complement values.
- [MTLVertexFormat.ushort](mtlvertexformat/ushort.md)
  One unsigned 16-bit value.
- [MTLVertexFormat.ushort2](mtlvertexformat/ushort2.md)
  Two unsigned 16-bit values.
- [MTLVertexFormat.ushort3](mtlvertexformat/ushort3.md)
  Three unsigned 16-bit values.
- [MTLVertexFormat.ushort4](mtlvertexformat/ushort4.md)
  Four unsigned 16-bit values.
- [MTLVertexFormat.short](mtlvertexformat/short.md)
  One signed 16-bit two’s complement value.
- [MTLVertexFormat.short2](mtlvertexformat/short2.md)
  Two signed 16-bit two’s complement values.
- [MTLVertexFormat.short3](mtlvertexformat/short3.md)
  Three signed 16-bit two’s complement values.
- [MTLVertexFormat.short4](mtlvertexformat/short4.md)
  Four signed 16-bit two’s complement values.
- [MTLVertexFormat.ushortNormalized](mtlvertexformat/ushortnormalized.md)
  One unsigned normalized 16-bit value.
- [MTLVertexFormat.ushort2Normalized](mtlvertexformat/ushort2normalized.md)
  Two unsigned normalized 16-bit values.
- [MTLVertexFormat.ushort3Normalized](mtlvertexformat/ushort3normalized.md)
  Three unsigned normalized 16-bit values.
- [MTLVertexFormat.ushort4Normalized](mtlvertexformat/ushort4normalized.md)
  Four unsigned normalized 16-bit values.
- [MTLVertexFormat.shortNormalized](mtlvertexformat/shortnormalized.md)
  One signed normalized 16-bit two’s complement value.
- [MTLVertexFormat.short2Normalized](mtlvertexformat/short2normalized.md)
  Two signed normalized 16-bit two’s complement values.
- [MTLVertexFormat.short3Normalized](mtlvertexformat/short3normalized.md)
  Three signed normalized 16-bit two’s complement values.
- [MTLVertexFormat.short4Normalized](mtlvertexformat/short4normalized.md)
  Four signed normalized 16-bit two’s complement values.
- [MTLVertexFormat.half](mtlvertexformat/half.md)
  One half-precision floating-point value.
- [MTLVertexFormat.half2](mtlvertexformat/half2.md)
  Two half-precision floating-point values.
- [MTLVertexFormat.half3](mtlvertexformat/half3.md)
  Three half-precision floating-point values.
- [MTLVertexFormat.half4](mtlvertexformat/half4.md)
  Four half-precision floating-point values.
- [MTLVertexFormat.float](mtlvertexformat/float.md)
  One single-precision floating-point value.
- [MTLVertexFormat.float2](mtlvertexformat/float2.md)
  Two single-precision floating-point values.
- [MTLVertexFormat.float3](mtlvertexformat/float3.md)
  Three single-precision floating-point values.
- [MTLVertexFormat.float4](mtlvertexformat/float4.md)
  Four single-precision floating-point values.
- [MTLVertexFormat.uint](mtlvertexformat/uint.md)
  One unsigned 32-bit value.
- [MTLVertexFormat.uint2](mtlvertexformat/uint2.md)
  Two unsigned 32-bit values.
- [MTLVertexFormat.uint3](mtlvertexformat/uint3.md)
  Three unsigned 32-bit values.
- [MTLVertexFormat.uint4](mtlvertexformat/uint4.md)
  Four unsigned 32-bit values.
- [MTLVertexFormat.int](mtlvertexformat/int.md)
  One signed 32-bit two’s complement value.
- [MTLVertexFormat.int2](mtlvertexformat/int2.md)
  Two signed 32-bit two’s complement values.
- [MTLVertexFormat.int3](mtlvertexformat/int3.md)
  Three signed 32-bit two’s complement values.
- [MTLVertexFormat.int4](mtlvertexformat/int4.md)
  Four signed 32-bit two’s complement values.
- [MTLVertexFormat.int1010102Normalized](mtlvertexformat/int1010102normalized.md)
  One packed 32-bit value with four normalized signed two’s complement integer values, arranged as 10 bits, 10 bits, 10 bits, and 2 bits.
- [MTLVertexFormat.uint1010102Normalized](mtlvertexformat/uint1010102normalized.md)
  One packed 32-bit value with four normalized unsigned integer values, arranged as 10 bits, 10 bits, 10 bits, and 2 bits.
- [MTLVertexFormat.uchar4Normalized_bgra](mtlvertexformat/uchar4normalized_bgra.md)
  Four unsigned normalized 8-bit values, arranged as blue, green, red, and alpha components.
### Enumeration Cases
- [MTLVertexFormat.floatRG11B10](mtlvertexformat/floatrg11b10.md)
- [MTLVertexFormat.floatRGB9E5](mtlvertexformat/floatrgb9e5.md)
### Initializers
- [init?(rawValue: UInt)](mtlvertexformat/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var format: MTLVertexFormat](mtlvertexattributedescriptor/format.md)
  The format of the vertex attribute.
- [var offset: Int](mtlvertexattributedescriptor/offset.md)
  The location of an attribute in vertex data, determined by the byte offset from the start of the vertex data.
- [var bufferIndex: Int](mtlvertexattributedescriptor/bufferindex.md)
  The index in the argument table for the associated vertex buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexformat)*