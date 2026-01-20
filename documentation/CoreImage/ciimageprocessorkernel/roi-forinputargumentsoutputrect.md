# roi(forInput:arguments:outputRect:)

**Framework**: Core Image  
**Kind**: method

Override this class method to implement your processor’s ROI callback.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func roi(forInput inputIndex: Int32, arguments: [String : Any]?, outputRect: CGRect) -> CGRect
```

#### Return Value

 The `CGRect` of the `inputIndex`th input that is required for the above `outputRect`

#### Discussion

This will be called one or more times per render to determine what portion of the input images are needed to render a given ‘outputRect’ of the output. This will not be called if processor has no input images.

The default implementation would return outputRect.

> ❗ **Important**: This is a class method so that you cannot use or capture any state by accident. All the parameters that affect the output results must be passed to [`apply(withExtent:inputs:arguments:)`](ciimageprocessorkernel/apply(withextent:inputs:arguments:).md).

## Parameters

- `inputIndex`: The index that tells you which processor input for which to return the ROI rectangle.
- `arguments`: The arguments dictionary that was passed to  .
- `outputRect`: The output   that processor will be asked to output.

## See Also

- [class func apply(withExtent: CGRect, inputs: [CIImage]?, arguments: [String : Any]?) throws -> CIImage](ciimageprocessorkernel/apply(withextent:inputs:arguments:).md)
  Call this method on your Core Image Processor Kernel subclass to create a new image of the specified extent.
- [class func formatForInput(at: Int32) -> CIFormat](ciimageprocessorkernel/formatforinput(at:).md)
  Override this class method if you want your any of the inputs to be in a specific pixel format.
- [class func process(with: [any CIImageProcessorInput]?, arguments: [String : Any]?, output: any CIImageProcessorOutput) throws](ciimageprocessorkernel/process(with:arguments:output:).md)
  Override this class method to implement your Core Image Processor Kernel subclass.
- [class func roiTileArray(forInput: Int32, arguments: [String : Any]?, outputRect: CGRect) -> [CIVector]](ciimageprocessorkernel/roitilearray(forinput:arguments:outputrect:).md)
  Override this class method to implement your processor’s tiled ROI callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/roi(forinput:arguments:outputrect:))*