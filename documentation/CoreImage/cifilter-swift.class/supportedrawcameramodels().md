# supportedRawCameraModels()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use new CIRAWFilter class instead.

## Declaration

```swift
class func supportedRawCameraModels() -> [String]!
```

```objc
+ (NSArray<NSString *> *) supportedRawCameraModels;
```

## See Also

### Deprecated
- [init!(CVPixelBuffer: CVPixelBuffer!, properties: [AnyHashable : Any]!, options: [CIRAWFilterOption : Any]!)](./init%28cvpixelbuffer,properties,options%29-7qpsv.md)
  Creates a filter from a Core Video pixel buffer.
- [init!(imageData: Data!, options: [CIRAWFilterOption : Any]!)](./init%28imagedata,options%29.md)
  Creates a filter that allows the processing of RAW images.
- [init!(imageURL: URL!, options: [CIRAWFilterOption : Any]!)](./init%28imageurl,options%29.md)
  Creates a filter that allows the processing of RAW images.
- [struct CIRAWFilterOption](../cirawfilteroption.md)
- [class func serializedXMP(from: [CIFilter], inputImageExtent: CGRect) -> Data?](./serializedxmp%28from,inputimageextent%29.md)
  Serializes filter parameters into XMP form that is suitable for embedding in an image.
- [class func filterArray(fromSerializedXMP: Data, inputImageExtent: CGRect, error: NSErrorPointer) -> [CIFilter]](./filterarray%28fromserializedxmp,inputimageextent,error%29.md)
  Returns an array of filter objects de-serialized from XMP data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/supportedrawcameramodels())*