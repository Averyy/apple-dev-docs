# init(model:inputName:outputName:context:)

**Framework**: Create ML Components  
**Kind**: init

Creates an image feature extractor from a CoreML model.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(model: MLModel, inputName: String = "image", outputName: String, context: CIContext = CIContext()) throws
```

## Parameters

- `model`: The CoreML model which will be used for feature extraction.
- `inputName`: The name of the input which the   expects.
- `outputName`: The name of the output from the  .
- `context`: A Core Image context.

## See Also

- [init(contentsOf: URL, configuration: MLModelConfiguration, inputName: String, outputName: String, context: CIContext) async throws](mlmodelimagefeatureextractor/init(contentsof:configuration:inputname:outputname:context:).md)
  Creates an image feature extractor from a CoreML model URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/mlmodelimagefeatureextractor/init(model:inputname:outputname:context:))*