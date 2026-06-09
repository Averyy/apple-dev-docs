# ComputeStream

**Framework**: Core AI  
**Kind**: class

A stream of work to be run asynchronously.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class ComputeStream
```

#### Overview

A compute stream is what is provided to [`encode(inputs:states:outputViews:to:)`](inferencefunction/encode(inputs:states:outputviews:to:).md) to encode the work onto the stream. Multiple inferences encoded to the same stream are serialized as needed based on the the values read/written.

## Topics

### Initializers
- [convenience init()](computestream/init.md)
  Initialize an empty compute stream.
- [init(commandQueue: any MTLCommandQueue)](computestream/init(commandqueue:).md)
  Initialize a compute stream which will encode its work to the provided command queue.
### Instance Methods
- [func currentWorkCompleted() async](computestream/currentworkcompleted.md)
  Waits for all previous work encoded to this stream to be complete.

## See Also

- [struct InferenceFunction](inferencefunction.md)
  A function that performs inference on input values and produces output values.
- [struct InferenceFunctionDescriptor](inferencefunctiondescriptor.md)
  A description of an inference function’s signature.
- [struct InferenceValue](inferencevalue.md)
  A value that an inference function accepts as input or produces as output.
- [struct ImageDescriptor](imagedescriptor.md)
  A description of an image’s dimensions and pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/computestream)*