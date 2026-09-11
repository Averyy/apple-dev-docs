# ImageDescriptor

**Framework**: Core AI  
**Kind**: struct

A description of an image’s dimensions and pixel format.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct ImageDescriptor
```

## Mentions

- [Integrating on-device AI models in your app with Core AI](integrating-on-device-ai-models-in-your-app-with-core-ai.md)

## Topics

### Inspecting image properties
- [let pixelFormatType: OSType](imagedescriptor/pixelformattype.md)
  The four-character code that identifies the pixel format.
- [let width: Int](imagedescriptor/width.md)
  The width of the image, in pixels.
- [let height: Int](imagedescriptor/height.md)
  The height of the image, in pixels.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct InferenceFunction](inferencefunction.md)
  A function that performs inference on input values and produces output values.
- [struct InferenceFunctionDescriptor](inferencefunctiondescriptor.md)
  A description of an inference function’s signature.
- [struct InferenceValue](inferencevalue.md)
  A value that an inference function accepts as input or produces as output.
- [class ComputeStream](computestream.md)
  A stream of work to be run asynchronously.
- [Background Inference](../bundleresources/entitlements/com.apple.developer.background-tasks.continued-processing.inference.md)
  An entitlement that lets a background task run inference on the Neural Engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/imagedescriptor)*