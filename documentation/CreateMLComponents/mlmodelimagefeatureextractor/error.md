# MLModelImageFeatureExtractor.Error

**Framework**: Create ML Components  
**Kind**: enum

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
- [MLModelImageFeatureExtractor.Error.invalidInput(_:)](mlmodelimagefeatureextractor/error/invalidinput(_:).md)
  An error indicating that the mlmodel does not take required input.
- [MLModelImageFeatureExtractor.Error.invalidOutput(_:)](mlmodelimagefeatureextractor/error/invalidoutput(_:).md)
  An error indicating that the mlmodel does not produce the required output.
### Getting the debug description
- [var debugDescription: String](mlmodelimagefeatureextractor/error/debugdescription.md)
  A text representation of the error.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func applied(to: CIImage, eventHandler: EventHandler?) async throws -> MLShapedArray<Float>](mlmodelimagefeatureextractor/applied(to:eventhandler:).md)
  Uses the CoreML model to create image features from the input pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/mlmodelimagefeatureextractor/error)*