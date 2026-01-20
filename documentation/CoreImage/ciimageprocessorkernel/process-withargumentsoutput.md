# process(with:arguments:output:)

**Framework**: Core Image  
**Kind**: method

Override this class method to implement your Core Image Processor Kernel subclass.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func process(with inputs: [any CIImageProcessorInput]?, arguments: [String : Any]?, output: any CIImageProcessorOutput) throws
```

#### Discussion

When a `CIImage` containing your `CIImageProcessorKernel` class is rendered, your class’ implementation of this method will be called as needed for that render.  The method may be called more than once if Core Image needs to tile to limit memory usage.

When your implementation of this class method is called, use the provided `inputs` and `arguments` objects to return processed pixel data to Core Image via `output`.

> ❗ **Important**: This is a class method so that you cannot use or capture any state by accident. All the parameters that affect the output results must be passed to [`apply(withExtent:inputs:arguments:)`](ciimageprocessorkernel/apply(withextent:inputs:arguments:).md).

## Parameters

- `inputs`: An array of   that the class consumes to produce its output.   The   may be larger than the rect returned by  .
- `arguments`: The arguments dictionary that was passed to  .
- `output`: The   that the   must provide results to.

## See Also

- [class func apply(withExtent: CGRect, inputs: [CIImage]?, arguments: [String : Any]?) throws -> CIImage](ciimageprocessorkernel/apply(withextent:inputs:arguments:).md)
  Call this method on your Core Image Processor Kernel subclass to create a new image of the specified extent.
- [class func formatForInput(at: Int32) -> CIFormat](ciimageprocessorkernel/formatforinput(at:).md)
  Override this class method if you want your any of the inputs to be in a specific pixel format.
- [class func roi(forInput: Int32, arguments: [String : Any]?, outputRect: CGRect) -> CGRect](ciimageprocessorkernel/roi(forinput:arguments:outputrect:).md)
  Override this class method to implement your processor’s ROI callback.
- [class func roiTileArray(forInput: Int32, arguments: [String : Any]?, outputRect: CGRect) -> [CIVector]](ciimageprocessorkernel/roitilearray(forinput:arguments:outputrect:).md)
  Override this class method to implement your processor’s tiled ROI callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/process(with:arguments:output:))*