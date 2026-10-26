# varianceEpsilon

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The variance epsilon you use for numerical stability.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var varianceEpsilon: Float { get }
```

```objc
@property (nonatomic, readonly) float varianceEpsilon;
```

## See Also

### Inspecting Layer Normalization Layers
- [var normalizedShape: [Int]](./normalizedshape-8ujvv.md)
  The shape of the axes where normalization occurs.
- [var beta: MLCTensor?](./beta.md)
  The beta tensor.
- [var gamma: MLCTensor?](./gamma.md)
  The gamma tensor.
- [var betaParameter: MLCTensorParameter?](./betaparameter.md)
  The beta tensor parameter you use for optimizer updates.
- [var gammaParameter: MLCTensorParameter?](./gammaparameter.md)
  The gamma tensor parameter you use for optimizer updates.
- [normalizedShape](./normalizedshape-2cz6k.md)
  The shape of the axes where normalization occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclayernormalizationlayer/varianceepsilon)*