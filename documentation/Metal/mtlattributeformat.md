# MTLAttributeFormat

**Framework**: Metal  
**Kind**: enum

The data format options for acceleration structures.

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

All formats use little-endian byte order, which stores the least significant byte first. For GPU compute functions that manipulate data that other parts of your app consume, check that the data it exposes to the GPU matches the byte and bit alignments of the source format.

In a GPU compute function’s attributes, you can use a type that’s different from the original source data if it has the same number of bits. For example, a GPU function can interpret a 128-bit little-endian integer as a four-component vector of unsigned 32-bit integers ([`MTLAttributeFormat.uint4`](mtlattributeformat/uint4.md)).

> 💡 **Tip**:  Avoid visual corruption when manipulating pixel data in a GPU compute function for a subsequent stage by using an exact match for the underlying pixel data.

##### Normalized Integer Formats

Normalized signed integer formats have `Normalized` in the name and signed types like [`MTLAttributeFormat.char`](mtlattributeformat/char.md) or [`MTLAttributeFormat.short`](mtlattributeformat/short.md). For these formats, values in the range `[-1.0, 1.0]` map to `[MIN_INT, MAX_INT]`, where `MIN_INT` is the most negative integer and `MAX_INT` is the most positive integer for the number of bits in the storage size. Positive values and zero distribute uniformly in the range `[0.0, 1.0]`, and negative integer values greater than `(MIN_INT + 1)` distribute uniformly in the range `(-1.0, 0.0)`.

> ❗ **Important**:  For normalized signed integer formats, the values `MIN_INT` and `(MIN_INT + 1)` both map to `-1.0`.

Normalized unsigned integer formats have `Normalized` in the name and unsigned types like [`MTLAttributeFormat.uchar`](mtlattributeformat/uchar.md) or [`MTLAttributeFormat.ushort`](mtlattributeformat/ushort.md). For these formats, values in the range `[0.0, 1.0]` map to `[0, MAX_UINT]`, where `MAX_UINT` is the largest unsigned integer for the number of bits in the storage size.

## Topics

### 32-bit floating-point formats
- [MTLAttributeFormat.float](mtlattributeformat/float.md)
  A 32-bit floating-point value.
- [MTLAttributeFormat.float2](mtlattributeformat/float2.md)
  A two-component vector with 32-bit floating-point values.
- [MTLAttributeFormat.float3](mtlattributeformat/float3.md)
  A three-component vector with 32-bit floating-point values.
- [MTLAttributeFormat.float4](mtlattributeformat/float4.md)
  A four-component vector with 32-bit floating-point values.
- [MTLAttributeFormat.floatRG11B10](mtlattributeformat/floatrg11b10.md)
  One packed 32-bit value representing pixel data containing 11-bit float red and green channels, and a 10-bit float blue channel.
- [MTLAttributeFormat.floatRGB9E5](mtlattributeformat/floatrgb9e5.md)
  One packed 32-bit value representing pixel data containing 9-bit float red, green, and blue channels, and a 5-bit float shared exponent channel.
### 32-bit integer formats
- [MTLAttributeFormat.int](mtlattributeformat/int.md)
  A 32-bit, signed integer value.
- [MTLAttributeFormat.int2](mtlattributeformat/int2.md)
  A two-component vector with 32-bit, signed integer values.
- [MTLAttributeFormat.int3](mtlattributeformat/int3.md)
  A three-component vector with 32-bit, signed integer values.
- [MTLAttributeFormat.int4](mtlattributeformat/int4.md)
  A four-component vector with 32-bit, signed integer values.
- [MTLAttributeFormat.uint](mtlattributeformat/uint.md)
  A 32-bit, unsigned integer value.
- [MTLAttributeFormat.uint2](mtlattributeformat/uint2.md)
  A two-component vector with 32-bit, unsigned integer values.
- [MTLAttributeFormat.uint3](mtlattributeformat/uint3.md)
  A three-component vector with 32-bit, unsigned integer values.
- [MTLAttributeFormat.uint4](mtlattributeformat/uint4.md)
  A four-component vector with 32-bit, unsigned integer values.
### 32-bit normalized integer formats
- [MTLAttributeFormat.int1010102Normalized](mtlattributeformat/int1010102normalized.md)
  One packed 32-bit value with four normalized signed two’s complement integer values, arranged as 10 bits, 10 bits, 10 bits, and 2 bits.
- [MTLAttributeFormat.uint1010102Normalized](mtlattributeformat/uint1010102normalized.md)
  One packed 32-bit value with four normalized unsigned integer values, arranged as 10 bits, 10 bits, 10 bits, and 2 bits.
- [MTLAttributeFormat.uchar4Normalized_bgra](mtlattributeformat/uchar4normalized_bgra.md)
  Four unsigned normalized 8-bit values, arranged as blue, green, red, and alpha components.
### 16-bit floating-point formats
- [MTLAttributeFormat.half](mtlattributeformat/half.md)
  A 16-bit floating-point value.
- [MTLAttributeFormat.half2](mtlattributeformat/half2.md)
  A two-component vector with 16-bit floating-point values.
- [MTLAttributeFormat.half3](mtlattributeformat/half3.md)
  A three-component vector with 16-bit floating-point values.
- [MTLAttributeFormat.half4](mtlattributeformat/half4.md)
  A four-component vector with 16-bit floating-point values.
### 16-bit integer formats
- [MTLAttributeFormat.short](mtlattributeformat/short.md)
  A 16-bit, signed integer value.
- [MTLAttributeFormat.short2](mtlattributeformat/short2.md)
  A two-component vector with 16-bit, signed integer values.
- [MTLAttributeFormat.short3](mtlattributeformat/short3.md)
  A three-component vector with 16-bit, signed integer values.
- [MTLAttributeFormat.short4](mtlattributeformat/short4.md)
  A four-component vector with 16-bit, signed integer values.
- [MTLAttributeFormat.ushort](mtlattributeformat/ushort.md)
  A 16-bit, unsigned integer value.
- [MTLAttributeFormat.ushort2](mtlattributeformat/ushort2.md)
  A two-component vector with 16-bit, unsigned integer values.
- [MTLAttributeFormat.ushort3](mtlattributeformat/ushort3.md)
  A three-component vector with 16-bit, unsigned integer values.
- [MTLAttributeFormat.ushort4](mtlattributeformat/ushort4.md)
  A four-component vector with 16-bit, unsigned integer values.
### 16-bit normalized integer formats
- [MTLAttributeFormat.shortNormalized](mtlattributeformat/shortnormalized.md)
  A 16-bit, normalized, signed integer value.
- [MTLAttributeFormat.short2Normalized](mtlattributeformat/short2normalized.md)
  A two-component vector with 16-bit, normalized, signed integer values.
- [MTLAttributeFormat.short3Normalized](mtlattributeformat/short3normalized.md)
  A three-component vector with 16-bit, normalized, signed integer values.
- [MTLAttributeFormat.short4Normalized](mtlattributeformat/short4normalized.md)
  A four-component vector with 16-bit, normalized, signed integer values.
- [MTLAttributeFormat.ushortNormalized](mtlattributeformat/ushortnormalized.md)
  A 16-bit, normalized, unsigned integer value.
- [MTLAttributeFormat.ushort2Normalized](mtlattributeformat/ushort2normalized.md)
  Two unsigned normalized 16-bit values
- [MTLAttributeFormat.ushort3Normalized](mtlattributeformat/ushort3normalized.md)
  A three-component vector with 16-bit, normalized, unsigned integer values.
- [MTLAttributeFormat.ushort4Normalized](mtlattributeformat/ushort4normalized.md)
  A four-component vector with 16-bit, normalized, unsigned integer values.
### 8-bit integer formats
- [MTLAttributeFormat.char](mtlattributeformat/char.md)
  An 8-bit, signed integer value.
- [MTLAttributeFormat.char2](mtlattributeformat/char2.md)
  A two-component vector with 8-bit, signed integer values.
- [MTLAttributeFormat.char3](mtlattributeformat/char3.md)
  A three-component vector with 8-bit, signed integer values.
- [MTLAttributeFormat.char4](mtlattributeformat/char4.md)
  A four-component vector with 8-bit, signed integer values.
- [MTLAttributeFormat.uchar](mtlattributeformat/uchar.md)
  An 8-bit, unsigned integer value.
- [MTLAttributeFormat.uchar2](mtlattributeformat/uchar2.md)
  A two-component vector with 8-bit, unsigned integer values.
- [MTLAttributeFormat.uchar3](mtlattributeformat/uchar3.md)
  A three-component vector with 8-bit, unsigned integer values.
- [MTLAttributeFormat.uchar4](mtlattributeformat/uchar4.md)
  A four-component vector with 8-bit, unsigned integer values.
### 8-bit normalized integer formats
- [MTLAttributeFormat.charNormalized](mtlattributeformat/charnormalized.md)
  An 8-bit, normalized, signed integer value.
- [MTLAttributeFormat.char2Normalized](mtlattributeformat/char2normalized.md)
  A two-component vector with 8-bit, normalized, signed integer values.
- [MTLAttributeFormat.char3Normalized](mtlattributeformat/char3normalized.md)
  A three-component vector with 8-bit, normalized, signed integer values.
- [MTLAttributeFormat.char4Normalized](mtlattributeformat/char4normalized.md)
  A four-component vector with 8-bit, normalized, signed integer values.
- [MTLAttributeFormat.ucharNormalized](mtlattributeformat/ucharnormalized.md)
  An 8-bit, normalized, unsigned integer value.
- [MTLAttributeFormat.uchar2Normalized](mtlattributeformat/uchar2normalized.md)
  A two-component vector with 8-bit, normalized, unsigned integer values.
- [MTLAttributeFormat.uchar3Normalized](mtlattributeformat/uchar3normalized.md)
  A three-component vector with 8-bit, normalized, unsigned integer values.
- [MTLAttributeFormat.uchar4Normalized](mtlattributeformat/uchar4normalized.md)
  A four-component vector with 8-bit, normalized, unsigned integer values.
### Sentinel values
- [MTLAttributeFormat.invalid](mtlattributeformat/invalid.md)
  A sentinel value that represents an invalid attribute format.
### Swift support
- [init?(rawValue: UInt)](mtlattributeformat/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var bufferIndex: Int](mtlattributedescriptor/bufferindex.md)
  The index in the buffer argument table for the buffer that contains the data for this attribute.
- [var offset: Int](mtlattributedescriptor/offset.md)
  The offset, in bytes, from the start of the buffer that contains the attribute data to the start of the data itself.
- [var format: MTLAttributeFormat](mtlattributedescriptor/format.md)
  The format of the attribute’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlattributeformat)*