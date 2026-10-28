# init(imageURL:options:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Creates a filter that allows the processing of RAW images.

**Availability**:
- iOS 10.0+ - Deprecated in 27.2
- iPadOS 10.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.5+ - Deprecated in 27.2
- tvOS 10.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`init(imageURL:)`](../cirawfilter/init%28imageurl%29.md) instead.

## Declaration

```swift
init!(imageURL url: URL!, options: [CIRAWFilterOption : Any]! = [:])
```

```objc
+ (CIFilter *) filterWithImageURL:(NSURL *) url options:(NSDictionary<NSString *,id> *) options;
```

## Return Value

A [`CIFilter`](../cifilter-swift.class.md) object.

## Discussion

The first step when working with RAW images in Core Image is to process the image using either [`init(imageData:options:)`](./init%28imagedata,options%29.md) or [`init(imageURL:options:)`](./init%28imageurl,options%29.md). These initializers create a [`CIFilter`](../cifilter-swift.class.md) object with an [`outputImage`](./outputimage.md) which is a [`CIImage`](../ciimage.md) representation of the supplied RAW image.

The newly created filter object allows you fine control over the image processing that isn’t available when working with processed images such a JPEG. The following listing shows how to create a Core Image filter based on a URL named `imageURL`. The image is processed so that its neutral temperature is set to 2,000 Kelvin (giving a blue tint) and its baseline exposure doubled. Finally, a Core Image vignette filter is applied to the processed image in the same way it would be with any other source image:

```objc
let rawFilter = CIFilter(imageURL: imageURL, options: nil)
rawFilter?.setValue(2000,    
                    forKey: kCIInputNeutralTemperatureKey)
if let baselineExposure = rawFilter?.value(forKey: kCIInputBaselineExposureKey) as? NSNumber {    
    rawFilter?.setValue(baselineExposure.doubleValue * 2.5,                        forKey: kCIInputBaselineExposureKey)
}
let vignettedImage = rawFilter?.outputImage?.applyingFilter(    
    "CIVignette",    
    withInputParameters: [kCIInputIntensityKey: 5])
if let outputImage = vignettedImage {    
    imageView.image = UIImage(ciImage: outputImage)
}
```

> ❗ **Important**:  Core Image doesn’t process the supplied RAW image until the filter’s [`outputImage`](./outputimage.md) is rendered. For this reason, if you supply this initializer with a RAW image of an unsupported format, the filter object will be initialized but its [`outputImage`](./outputimage.md) will be `nil`.

## Parameters

- `url`: The location of a RAW image file.
- `options`: An options dictionary.  You can pass any of the keys defined in [RAW Image Options](../raw-image-options.md).

## See Also

### Deprecated
- [init!(CVPixelBuffer: CVPixelBuffer!, properties: [AnyHashable : Any]!, options: [CIRAWFilterOption : Any]!)](./init%28cvpixelbuffer,properties,options%29-7qpsv.md)
  Creates a filter from a Core Video pixel buffer.
- [init!(imageData: Data!, options: [CIRAWFilterOption : Any]!)](./init%28imagedata,options%29.md)
  Creates a filter that allows the processing of RAW images.
- [struct CIRAWFilterOption](../cirawfilteroption.md)
- [class func serializedXMP(from: [CIFilter], inputImageExtent: CGRect) -> Data?](./serializedxmp%28from,inputimageextent%29.md)
  Serializes filter parameters into XMP form that is suitable for embedding in an image.
- [class func filterArray(fromSerializedXMP: Data, inputImageExtent: CGRect, error: NSErrorPointer) -> [CIFilter]](./filterarray%28fromserializedxmp,inputimageextent,error%29.md)
  Returns an array of filter objects de-serialized from XMP data.
- [class func supportedRawCameraModels() -> [String]!](./supportedrawcameramodels%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/init(imageurl:options:))*