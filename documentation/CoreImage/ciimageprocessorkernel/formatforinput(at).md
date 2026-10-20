# formatForInput(at:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Override this class method if you want your any of the inputs to be in a specific pixel format.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func formatForInput(at inputIndex: Int32) -> CIFormat
```

```objc
+ (CIFormat) formatForInputAtIndex:(int) inputIndex;
```

#### Discussion

The format must be one of `kCIFormatBGRA8`, `kCIFormatRGBAh`, `kCIFormatRGBAf` or `kCIFormatR8`. On iOS 12 and macOS 10.14, the formats `kCIFormatRh` and `kCIFormatRf` are also supported.

If the requested inputFormat is `0`, then the input will be a supported format that best matches the rendering context’s `/CIContext/workingFormat`.

If a processor wants data in a colorspace other than the context’s working color space, then call `/CIImage/imageByColorMatchingWorkingSpaceToColorSpace:` on the processor input. If a processor wants it input as alpha-unpremultiplied RGBA data, then call `/CIImage/imageByUnpremultiplyingAlpha` on the processor input.

## See Also

### Type Methods
- [class func apply(withExtent: CGRect, inputs: [CIImage]?, arguments: [String : Any]?) throws -> CIImage](./apply%28withextent,inputs,arguments%29.md)
  Call this method on your Core Image Processor Kernel subclass to create a new image of the specified extent.
- [class func process(with: [any CIImageProcessorInput]?, arguments: [String : Any]?, output: any CIImageProcessorOutput) throws](./process%28with,arguments,output%29.md)
  Override this class method to implement your Core Image Processor Kernel subclass.
- [class func roi(forInput: Int32, arguments: [String : Any]?, outputRect: CGRect) -> CGRect](./roi%28forinput,arguments,outputrect%29.md)
  Override this class method to implement your processor’s ROI callback.
- [class func roiTileArray(forInput: Int32, arguments: [String : Any]?, outputRect: CGRect) -> [CIVector]](./roitilearray%28forinput,arguments,outputrect%29.md)
  Override this class method to implement your processor’s tiled ROI callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/formatforinput(at:))*