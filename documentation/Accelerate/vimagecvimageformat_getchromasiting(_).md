# vImageCVImageFormat_GetChromaSiting(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns the chrominance siting of a Core Video image format.

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
func vImageCVImageFormat_GetChromaSiting(_ format: vImageConstCVImageFormat) -> Unmanaged<CFString>!
```

```c
CFStringRefvImageCVImageFormat_GetChromaSiting(vImageConstCVImageFormatRef format);
```

## Return Value

A [`CFString`](../CoreFoundation/cfstring.md) that describes the positioning of the chrominance samples.

## Discussion

4:2:0 and 4:2:0 YpCbCr image formats that have subsampled chrominance require the position of the chrominance samples relative to the luminance samples.

The functions that create Core Video image formats, such as [`vImageCVImageFormat_CreateWithCVPixelBuffer(_:)`](./vimagecvimageformat_createwithcvpixelbuffer%28_%29.md), return a [`vImageCVImageFormat`](./vimagecvimageformat.md). The following code shows how you create a [`vImageConstCVImageFormat`](./vimageconstcvimageformat.md) representation of a [`vImageCVImageFormat`](./vimagecvimageformat.md) instance to pass to [`vImageCVImageFormat_GetChromaSiting(_:)`](./vimagecvimageformat_getchromasiting%28_%29.md):

**Swift**:

```swift
let chromaSiting = withUnsafeBytes(of: cvImageFormat) { bytes in
    let format = bytes.assumingMemoryBound(
        to: vImageConstCVImageFormat.self).first!
    
    return vImageCVImageFormat_GetChromaSiting(format)
}
```

**Objective-C**:

```objc
vImageConstCVImageFormatRef constFormat = cvImageFormat;

CFStringRef chromaSiting = vImageCVImageFormat_GetChromaSiting(constFormat);
```

## Parameters

- `format`: The Core Video image format to query.

## See Also

### Related Documentation
- [var chromaSiting: vImageCVImageFormat.ChromaSiting?](./vimagecvimageformat/chromasiting-swift.property.md)
  The chrominance siting of the Core Video image format.
### Querying and setting the chrominance siting
- [func vImageCVImageFormat_SetChromaSiting(vImageCVImageFormat, CFString!) -> vImage_Error](./vimagecvimageformat_setchromasiting%28_,_%29.md)
  Sets the chrominance siting of a Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_getchromasiting(_:))*