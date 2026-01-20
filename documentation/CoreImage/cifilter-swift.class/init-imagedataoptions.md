# init(imageData:options:)

**Framework**: Core Image  
**Kind**: init

Creates a filter that allows the processing of RAW images.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init!(imageData data: Data!, options: [CIRAWFilterOption : Any]! = [:])
```

#### Return Value

A [`CIFilter`](cifilter-swift.class.md) object.

#### Discussion

You can pass any of the keys defined in [`RAW Image Options`](raw-image-options.md) along with the appropriate value in `options`. You should provide a source type identifier hint key ([`kCGImageSourceTypeIdentifierHint`](https://developer.apple.com/documentation/ImageIO/kCGImageSourceTypeIdentifierHint)) and the appropriate source type value to help the decoder determine the file type. Otherwise it’s possible to obtain incorrect results.

The first step when working with RAW images in Core Image is to process the image using either [`init(imageData:options:)`](cifilter-swift.class/init(imagedata:options:).md) or [`init(imageURL:options:)`](cifilter-swift.class/init(imageurl:options:).md). These initializers create a [`CIFilter`](cifilter-swift.class.md) object with an [`outputImage`](cifilter-swift.class/outputimage.md) which is a [`CIImage`](ciimage.md) representation of the supplied RAW image. You can process After calling this method, the [`CIFilter`](cifilter-swift.class.md) object returns a [`CIImage`](ciimage.md) object that’s properly processed similar to images retrieved using the `outputImage` key.

> ❗ **Important**:  Core Image doesn’t process the supplied RAW image until the filter’s [`outputImage`](cifilter-swift.class/outputimage.md) is rendered. For this reason, if you supply this initializer with a RAW image of an unsupported format, the filter object will be initialized but its [`outputImage`](cifilter-swift.class/outputimage.md) will be `nil`.

## Parameters

- `data`: The RAW image data to initialize the object with.
- `options`: An options dictionary.

## See Also

- [init!(CVPixelBuffer: CVPixelBuffer!, properties: [AnyHashable : Any]!, options: [CIRAWFilterOption : Any]!)](cifilter-swift.class/init(cvpixelbuffer:properties:options:).md)
  Creates a filter from a Core Video pixel buffer.
- [init!(imageURL: URL!, options: [CIRAWFilterOption : Any]!)](cifilter-swift.class/init(imageurl:options:).md)
  Creates a filter that allows the processing of RAW images.
- [struct CIRAWFilterOption](cirawfilteroption.md)
- [class func serializedXMP(from: [CIFilter], inputImageExtent: CGRect) -> Data?](cifilter-swift.class/serializedxmp(from:inputimageextent:).md)
  Serializes filter parameters into XMP form that is suitable for embedding in an image.
- [class func filterArray(fromSerializedXMP: Data, inputImageExtent: CGRect, error: NSErrorPointer) -> [CIFilter]](cifilter-swift.class/filterarray(fromserializedxmp:inputimageextent:error:).md)
  Returns an array of filter objects de-serialized from XMP data.
- [class func supportedRawCameraModels() -> [String]!](cifilter-swift.class/supportedrawcameramodels.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/init(imagedata:options:))*