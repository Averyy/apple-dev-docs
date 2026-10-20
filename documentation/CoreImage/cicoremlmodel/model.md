# model

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The Core ML model used to apply the effect on the image.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var model: MLModel { get set }
```

```objc
@property (nonatomic, retain) MLModel * model;
```

## See Also

### Instance Properties
- [var headIndex: Float](./headindex.md)
  A number that specifies which output of a multihead Core ML model applies the effect on the image.
- [var inputImage: CIImage?](./inputimage.md)
  The image to use as an input image.
- [var softmaxNormalization: Bool](./softmaxnormalization.md)
  A Boolean value that specifies whether to apply Softmax normalization to the output of the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicoremlmodel/model)*