# MTLDataType.rgb10a2Unorm

**Framework**: Metal  
**Kind**: case  
**Role**: Case

A packed 32-bit format with three color components, each of which is a 10-bit, normalized, unsigned integer value.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
case rgb10a2Unorm
```

```c
MTLDataTypeRGB10A2Unorm
```

#### Discussion

The color components are in RGBA order, which stands for red, green, blue, and alpha. The red, green, and blue components each have 10 bits, and the alpha component has 2 bits.

## See Also

### 32-bit color integer types
- [MTLDataType.rgba8Snorm](./rgba8snorm.md)
  An ordinary pixel with four components, each of which is an 8-bit, normalized, signed integer value.
- [MTLDataType.rgba8Unorm](./rgba8unorm.md)
  An ordinary pixel with four components, each of which is an 8-bit, normalized, unsigned integer value.
- [MTLDataType.rgba8Unorm_srgb](./rgba8unorm_srgb.md)
  An ordinary pixel with four components, each of which is an 8-bit, normalized, unsigned integer value in the sRGB color space.
- [MTLDataType.rg16Snorm](./rg16snorm.md)
  An ordinary pixel with two components, each of which is a 16-bit, normalized, signed integer value.
- [MTLDataType.rg16Unorm](./rg16unorm.md)
  An ordinary pixel with two components, each of which is a 16-bit, normalized, unsigned integer value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldatatype/rgb10a2unorm)*