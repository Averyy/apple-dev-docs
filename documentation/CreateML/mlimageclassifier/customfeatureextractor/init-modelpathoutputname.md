# init(modelPath:outputName:)

**Framework**: Create ML  
**Kind**: init

Creates a custom feature extractor given a model file and an optional output layer name.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
init(modelPath: URL, outputName: String? = nil)
```

## Parameters

- `modelPath`: The location of the neural network   which contains the feature extractor.
- `outputName`: The name of a feature extraction layer within the model has one output type of   . Set this value to   if the   model, as a whole, accepts an input image and has exactly one output of type   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/customfeatureextractor/init(modelpath:outputname:))*