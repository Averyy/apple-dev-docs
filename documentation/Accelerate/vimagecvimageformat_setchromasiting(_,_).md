# vImageCVImageFormat_SetChromaSiting(_:_:)

**Framework**: Accelerate  
**Kind**: func

Sets the chrominance siting of a Core Video image format.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 8.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageCVImageFormat_SetChromaSiting(_ format: vImageCVImageFormat, _ siting: CFString!) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

4:2:0 and 4:2:0 YpCbCr image formats that have subsampled chrominance require the position of the chrominance samples relative to the luminance samples.

## Parameters

- `format`: The Core Video image format to update.
- `siting`: The new siting information for the format.

## See Also

- [var chromaSiting: vImageCVImageFormat.ChromaSiting?](vimagecvimageformat/chromasiting-swift.property.md)
  The chrominance siting of the Core Video image format.
- [func vImageCVImageFormat_GetChromaSiting(vImageConstCVImageFormat) -> Unmanaged<CFString>!](vimagecvimageformat_getchromasiting(_:).md)
  Returns the chrominance siting of a Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_setchromasiting(_:_:))*