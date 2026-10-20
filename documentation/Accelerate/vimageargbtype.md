# vImageARGBType

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Constants that describe the encoding of an ARGB image for conversions between RGB and YpCbCr.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct vImageARGBType
```

```c
typedef enum { ... } vImageARGBType;
```

## Topics

### Constants
- [init(UInt32)](./vimageargbtype/init%28_%29.md)
  Creates a new ARGB type.
- [init(rawValue: UInt32)](./vimageargbtype/init%28rawvalue%29.md)
  Creates a new ARGB type with an unsigned integer value.
- [var rawValue: UInt32](./vimageargbtype/rawvalue.md)
  The unsigned integer raw value.
- [var kvImageARGB16Q12: vImageARGBType](./kvimageargb16q12.md)
  Any 8-bit four-channel interleaved buffer.
- [var kvImageARGB16U: vImageARGBType](./kvimageargb16u.md)
  Any 16-bit unsigned, four-channel interleaved buffer.
- [var kvImageARGB8888: vImageARGBType](./kvimageargb8888.md)
  Any 16-bit signed fixed-point, four-channel interleaved buffer.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Generating conversion information
- [func vImageConvert_ARGBToYpCbCr_GenerateConversion(UnsafePointer<vImage_ARGBToYpCbCrMatrix>, UnsafePointer<vImage_YpCbCrPixelRange>, UnsafeMutablePointer<vImage_ARGBToYpCbCr>, vImageARGBType, vImageYpCbCrType, vImage_Flags) -> vImage_Error](./vimageconvert_argbtoypcbcr_generateconversion%28_,_,_,_,_,_%29.md)
  Generates the information that describes the conversion from ARGB to YpCbCr.
- [struct vImageYpCbCrType](./vimageypcbcrtype.md)
  Constants that describe the encoding of a YpCbCr image for conversions between RGB and YpCbCr.
- [struct vImage_ARGBToYpCbCrMatrix](./vimage_argbtoypcbcrmatrix.md)
  The 3 x 3 matrix that the vImage library uses to convert from RGB to YpCbCr.
- [struct vImage_ARGBToYpCbCr](./vimage_argbtoypcbcr.md)
  The information that describes the conversion from ARGB to YpCbCr.
- [struct vImage_YpCbCrPixelRange](./vimage_ypcbcrpixelrange.md)
  The description of range and clamping information for YpCbCr pixel formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageargbtype)*