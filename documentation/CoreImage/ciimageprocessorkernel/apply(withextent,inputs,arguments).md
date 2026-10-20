# apply(withExtent:inputs:arguments:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Call this method on your Core Image Processor Kernel subclass to create a new image of the specified extent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func apply(withExtent extent: CGRect, inputs: [CIImage]?, arguments: [String : Any]?) throws -> CIImage
```

```objc
+ (CIImage *) applyWithExtent:(CGRect) extent inputs:(NSArray<CIImage *> *) inputs arguments:(NSDictionary<NSString *,id> *) arguments error:(NSError **) error;
```

#### Return Value

 An autoreleased [`CIImage`](../ciimage.md)

#### Discussion

The inputs and arguments will be retained so that your subclass can be called when the image is drawn.

This method will return `nil` and an error if:

- calling [`outputFormat`](./outputformat.md) on your subclass returns an unsupported format.
- calling [`formatForInput(at:)`](./formatforinput%28at%29.md) on your subclass returns an unsupported format.
- your subclass does not implement [`process(with:arguments:output:)`](./process%28with,arguments,output%29.md)

## Parameters

- `extent`: The bounding `CGRect` of pixels that the `CIImageProcessorKernel` can produce. This method will return `/CIImage/emptyImage` if extent is empty.
- `inputs`: An array of [`CIImage`](../ciimage.md) objects to use as input.
- `arguments`: This dictionary contains any additional parameters that the processor needs to produce its output. The argument objects can be of any type but in order for CoreImage to cache intermediates, they must be of the following immutable types: `NSArray`, `NSDictionary`, `NSNumber`, `NSValue`, `NSData`, `NSString`, `NSNull`, [`CIVector`](../civector.md), [`CIColor`](../cicolor.md), `CGImage`, `CGColorSpace`, or `MLModel`.

## See Also

### Type Methods
- [class func formatForInput(at: Int32) -> CIFormat](./formatforinput%28at%29.md)
  Override this class method if you want your any of the inputs to be in a specific pixel format.
- [class func process(with: [any CIImageProcessorInput]?, arguments: [String : Any]?, output: any CIImageProcessorOutput) throws](./process%28with,arguments,output%29.md)
  Override this class method to implement your Core Image Processor Kernel subclass.
- [class func roi(forInput: Int32, arguments: [String : Any]?, outputRect: CGRect) -> CGRect](./roi%28forinput,arguments,outputrect%29.md)
  Override this class method to implement your processor’s ROI callback.
- [class func roiTileArray(forInput: Int32, arguments: [String : Any]?, outputRect: CGRect) -> [CIVector]](./roitilearray%28forinput,arguments,outputrect%29.md)
  Override this class method to implement your processor’s tiled ROI callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/apply(withextent:inputs:arguments:))*