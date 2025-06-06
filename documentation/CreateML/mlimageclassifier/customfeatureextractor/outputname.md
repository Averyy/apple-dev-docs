# outputName

**Framework**: Create ML  
**Kind**: property

The name of the output from a feature extraction layer within the model.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var outputName: String?
```

#### Discussion

When training an image classifier with a custom feature extractor, use [`outputName`](mlimageclassifier/customfeatureextractor/outputname.md) to select a layer within the model that has an output of [`MLMultiArray`](https://developer.apple.com/documentation/CoreML/MLMultiArray).

Set [`outputName`](mlimageclassifier/customfeatureextractor/outputname.md) to `nil` if the model (specified by [`modelPath`](mlimageclassifier/customfeatureextractor/modelpath.md)) has only one output of type [`MLMultiArray`](https://developer.apple.com/documentation/CoreML/MLMultiArray).

## See Also

- [var modelPath: URL](mlimageclassifier/customfeatureextractor/modelpath.md)
  The location of a neural network `.mlmodel` file that takes an image as an input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/customfeatureextractor/outputname)*