# init(contentsOf:configuration:inputName:outputName:context:)

**Framework**: Create ML Components  
**Kind**: init

Creates an image feature extractor from a CoreML model URL.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(contentsOf url: URL, configuration: MLModelConfiguration, inputName: String = "image", outputName: String, context: CIContext = CIContext()) async throws
```

## Parameters

- `url`: URL of the .mlmodel file.
- `configuration`: The model configuration of the CoreML model.
- `inputName`: The name of the input which the   expects.
- `outputName`: The name of the output from the  .
- `context`: The Core Image context.

## See Also

- [init(model: MLModel, inputName: String, outputName: String, context: CIContext) throws](mlmodelimagefeatureextractor/init(model:inputname:outputname:context:).md)
  Creates an image feature extractor from a CoreML model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/mlmodelimagefeatureextractor/init(contentsof:configuration:inputname:outputname:context:))*