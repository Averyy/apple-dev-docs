# model

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

The Core ML model used to apply the effect on the image.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var model: MLModel { get set }
```

## See Also

- [var headIndex: Float](cicoremlmodel/headindex.md)
  A number that specifies which output of a multihead Core ML model applies the effect on the image.
- [var inputImage: CIImage?](cicoremlmodel/inputimage.md)
  The image to use as an input image.
- [var softmaxNormalization: Bool](cicoremlmodel/softmaxnormalization.md)
  A Boolean value that specifies whether to apply Softmax normalization to the output of the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicoremlmodel/model)*