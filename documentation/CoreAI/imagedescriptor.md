# ImageDescriptor

**Framework**: Core AI  
**Kind**: struct

A description of an image’s dimensions and pixel format.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ImageDescriptor
```

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
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct InferenceFunction](inferencefunction.md)
  A function that performs inference on input values and produces output values.
- [struct InferenceFunctionDescriptor](inferencefunctiondescriptor.md)
  A description of an inference function’s signature.
- [struct InferenceValue](inferencevalue.md)
  A value that an inference function accepts as input or produces as output.
- [class ComputeStream](computestream.md)
  A stream of work to be run asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/imagedescriptor)*