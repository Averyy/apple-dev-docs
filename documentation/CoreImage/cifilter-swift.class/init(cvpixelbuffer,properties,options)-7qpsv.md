# init(CVPixelBuffer:properties:options:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Creates a filter from a Core Video pixel buffer.

**Availability**:
- iOS 10.0+ - Deprecated in 27.2
- iPadOS 10.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.12+ - Deprecated in 27.2
- tvOS 10.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`init(cvPixelBuffer:properties:)`](../cirawfilter/init%28cvpixelbuffer,properties%29-6209q.md) instead.

## Declaration

```swift
init!(CVPixelBuffer pixelBuffer: CVPixelBuffer!, properties: [AnyHashable : Any]!, options: [CIRAWFilterOption : Any]! = [:])
```

## Return Value

A [`CIFilter`](../cifilter-swift.class.md) object.

## Discussion

The first step when working with RAW images in Core Image is to process the image using either [`init(imageData:options:)`](./init%28imagedata,options%29.md) or [`init(imageURL:options:)`](./init%28imageurl,options%29.md). These initializers create a [`CIFilter`](../cifilter-swift.class.md) object with an [`outputImage`](./outputimage.md) which is a [`CIImage`](../ciimage.md) representation of the supplied RAW image.

> ❗ **Important**:  Core Image doesn’t process the supplied RAW image until the filter’s [`outputImage`](./outputimage.md) is rendered. For this reason, if you supply this initializer with a RAW image of an unsupported format, the filter object will be initialized but its [`outputImage`](./outputimage.md) will be nil.

## Parameters

- `pixelBuffer`: CVPixelBufferRef with one of the following RAW pixel format types:

  [`kCVPixelFormatType_14Bayer_GRBG`](../../CoreVideo/kcvpixelformattype_14bayer_grbg.md)

  [`kCVPixelFormatType_14Bayer_RGGB`](../../CoreVideo/kcvpixelformattype_14bayer_rggb.md)

  [`kCVPixelFormatType_14Bayer_BGGR`](../../CoreVideo/kcvpixelformattype_14bayer_bggr.md)

  [`kCVPixelFormatType_14Bayer_GBRG`](../../CoreVideo/kcvpixelformattype_14bayer_gbrg.md)
- `properties`: A properties dictionary. Defines the properties of the pixel buffer.
- `options`: An options dictionary.  You can pass any of the keys defined in [RAW Image Options](../raw-image-options.md).

## See Also

### Deprecated
- [init!(imageData: Data!, options: [CIRAWFilterOption : Any]!)](./init%28imagedata,options%29.md)
  Creates a filter that allows the processing of RAW images.
- [init!(imageURL: URL!, options: [CIRAWFilterOption : Any]!)](./init%28imageurl,options%29.md)
  Creates a filter that allows the processing of RAW images.
- [struct CIRAWFilterOption](../cirawfilteroption.md)
- [class func serializedXMP(from: [CIFilter], inputImageExtent: CGRect) -> Data?](./serializedxmp%28from,inputimageextent%29.md)
  Serializes filter parameters into XMP form that is suitable for embedding in an image.
- [class func filterArray(fromSerializedXMP: Data, inputImageExtent: CGRect, error: NSErrorPointer) -> [CIFilter]](./filterarray%28fromserializedxmp,inputimageextent,error%29.md)
  Returns an array of filter objects de-serialized from XMP data.
- [class func supportedRawCameraModels() -> [String]!](./supportedrawcameramodels%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/init(cvpixelbuffer:properties:options:)-7qpsv)*