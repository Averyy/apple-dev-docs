# MLModelImageFeatureExtractor.Error

**Framework**: Create ML Components  
**Kind**: enum  
**Role**: Enumeration

CoreML Extraction error.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum Error
```

## Topics

### Analyzing the error
- [MLModelImageFeatureExtractor.Error.invalidInput(_:)](./error/invalidinput%28_%29.md)
  An error indicating that the mlmodel does not take required input.
- [MLModelImageFeatureExtractor.Error.invalidOutput(_:)](./error/invalidoutput%28_%29.md)
  An error indicating that the mlmodel does not produce the required output.
### Getting the debug description
- [var debugDescription: String](./error/debugdescription.md)
  A text representation of the error.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Applying
- [func applied(to: CIImage, eventHandler: EventHandler?) async throws -> MLShapedArray<Float>](./applied%28to,eventhandler%29.md)
  Uses the CoreML model to create image features from the input pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/mlmodelimagefeatureextractor/error)*