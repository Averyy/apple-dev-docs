# filterArray(fromSerializedXMP:inputImageExtent:error:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Returns an array of filter objects de-serialized from XMP data.

**Availability**:
- iOS 6.0+ - Deprecated in 17.0
- iPadOS 6.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 10.9+ - Deprecated in 14.0
- tvOS - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class func filterArray(fromSerializedXMP xmpData: Data, inputImageExtent extent: CGRect, error outError: NSErrorPointer) -> [CIFilter]
```

```objc
+ (NSArray<CIFilter *> *) filterArrayFromSerializedXMP:(NSData *) xmpData inputImageExtent:(CGRect) extent error:(NSError **) outError;
```

## Parameters

- `xmpData`: The XMP data created previously by calling [`serializedXMP(from:inputImageExtent:)`](./serializedxmp%28from,inputimageextent%29.md).
- `extent`: The extent of the image from which the XMP data was extracted.
- `outError`: The address of an `NSError` object for receiving errors, otherwise `nil`.

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
- [class func supportedRawCameraModels() -> [String]!](./supportedrawcameramodels%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/filterarray(fromserializedxmp:inputimageextent:error:))*