# process(with:arguments:outputs:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Override this class method of your Core Image Processor Kernel subclass if it needs to produce multiple outputs.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class func process(with inputs: [any CIImageProcessorInput]?, arguments: [String : Any]?, outputs: [any CIImageProcessorOutput]) throws
```

```objc
+ (BOOL) processWithInputs:(NSArray<id<CIImageProcessorInput>> *) inputs arguments:(NSDictionary<NSString *,id> *) arguments outputs:(NSArray<id<CIImageProcessorOutput>> *) outputs error:(NSError **) error;
```

## Discussion

This supports 0, 1, 2 or more input images and 2 or more output images.

When a `CIImage` containing your `CIImageProcessorKernel` class is rendered, your class’ implementation of this method will be called as needed for that render.  The method may be called more than once if Core Image needs to tile to limit memory usage.

When your implementation of this class method is called, use the provided `inputs` and `arguments` objects to return processed pixel data to Core Image via multiple `outputs`.

> ❗ **Important**: This is a class method so that you cannot use or capture any state by accident. All the parameters that affect the output results must be passed to [`apply(withExtent:inputs:arguments:)`](./apply%28withextent,inputs,arguments%29.md).

## Parameters

- `inputs`: An array of `id<CIImageProcessorInput>` that the class consumes to produce its output. The `input.region` may be larger than the rect returned by [`roi(forInput:arguments:outputRect:)`](./roi%28forinput,arguments,outputrect%29.md).
- `arguments`: The arguments dictionary that was passed to [`apply(withExtent:inputs:arguments:)`](./apply%28withextent,inputs,arguments%29.md).
- `outputs`: An array `id<CIImageProcessorOutput>` that the `CIImageProcessorKernel` must provide results to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/process(with:arguments:outputs:))*