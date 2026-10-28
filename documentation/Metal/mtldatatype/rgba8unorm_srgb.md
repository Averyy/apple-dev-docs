# MTLDataType.rgba8Unorm_srgb

**Framework**: Metal  
**Kind**: case  
**Role**: Case

An ordinary pixel with four components, each of which is an 8-bit, normalized, unsigned integer value in the sRGB color space.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
case rgba8Unorm_srgb
```

```c
MTLDataTypeRGBA8Unorm_sRGB
```

## Discussion

The color components are in RGBA order, which stands for red, green, blue, and alpha.

## See Also

### 32-bit color integer types
- [MTLDataType.rgba8Snorm](./rgba8snorm.md)
  An ordinary pixel with four components, each of which is an 8-bit, normalized, signed integer value.
- [MTLDataType.rgba8Unorm](./rgba8unorm.md)
  An ordinary pixel with four components, each of which is an 8-bit, normalized, unsigned integer value.
- [MTLDataType.rg16Snorm](./rg16snorm.md)
  An ordinary pixel with two components, each of which is a 16-bit, normalized, signed integer value.
- [MTLDataType.rg16Unorm](./rg16unorm.md)
  An ordinary pixel with two components, each of which is a 16-bit, normalized, unsigned integer value.
- [MTLDataType.rgb10a2Unorm](./rgb10a2unorm.md)
  A packed 32-bit format with three color components, each of which is a 10-bit, normalized, unsigned integer value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldatatype/rgba8unorm_srgb)*