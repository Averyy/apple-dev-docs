# serializedXMP(from:inputImageExtent:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Serializes filter parameters into XMP form that is suitable for embedding in an image.

**Availability**:
- iOS 6.0+ - Deprecated in 17.0
- iPadOS 6.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 10.9+ - Deprecated in 14.0
- tvOS - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class func serializedXMP(from filters: [CIFilter], inputImageExtent extent: CGRect) -> Data?
```

```objc
+ (NSData *) serializedXMPFromFilters:(NSArray<CIFilter *> *) filters inputImageExtent:(CGRect) extent;
```

#### Discussion

At this time the only filters classes that can be serialized using this method are, CIAffineTransform, CICrop, and the filters returned by the [`CIImage`](../ciimage.md) methods [`autoAdjustmentFilters()`](../ciimage/autoadjustmentfilters%28%29.md) and [`autoAdjustmentFilters(options:)`](../ciimage/autoadjustmentfilters%28options%29.md). The parameters of other filter classes will not be serialized.

## Parameters

- `filters`: The array of filters to serialize. See Discussion for the filters that can be serialized.
- `extent`: The extent of the input image to the filter.

## See Also

### Deprecated
- [init!(CVPixelBuffer: CVPixelBuffer!, properties: [AnyHashable : Any]!, options: [CIRAWFilterOption : Any]!)](./init%28cvpixelbuffer,properties,options%29-7qpsv.md)
  Creates a filter from a Core Video pixel buffer.
- [init!(imageData: Data!, options: [CIRAWFilterOption : Any]!)](./init%28imagedata,options%29.md)
  Creates a filter that allows the processing of RAW images.
- [init!(imageURL: URL!, options: [CIRAWFilterOption : Any]!)](./init%28imageurl,options%29.md)
  Creates a filter that allows the processing of RAW images.
- [struct CIRAWFilterOption](../cirawfilteroption.md)
- [class func filterArray(fromSerializedXMP: Data, inputImageExtent: CGRect, error: NSErrorPointer) -> [CIFilter]](./filterarray%28fromserializedxmp,inputimageextent,error%29.md)
  Returns an array of filter objects de-serialized from XMP data.
- [class func supportedRawCameraModels() -> [String]!](./supportedrawcameramodels%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/serializedxmp(from:inputimageextent:))*