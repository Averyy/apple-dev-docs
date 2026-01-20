# MPSCNNInstanceNormalizationDataSource

**Framework**: Metal Performance Shaders  
**Kind**: protocol

A protocol that defines methods that an instance normalization uses to initialize scale factors and bias terms.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
protocol MPSCNNInstanceNormalizationDataSource : NSCopying, NSObjectProtocol
```

## Topics

### Initializers
- [init?(coder: NSCoder)](mpscnninstancenormalizationdatasource/init(coder:).md)
### Instance Properties
- [var numberOfFeatureChannels: Int](mpscnninstancenormalizationdatasource/numberoffeaturechannels.md)
### Instance Methods
- [func beta() -> UnsafeMutablePointer<Float>?](mpscnninstancenormalizationdatasource/beta.md)
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpscnninstancenormalizationdatasource/copy(with:device:).md)
- [func encode(with: NSCoder)](mpscnninstancenormalizationdatasource/encode(with:).md)
- [func epsilon() -> Float](mpscnninstancenormalizationdatasource/epsilon.md)
- [func gamma() -> UnsafeMutablePointer<Float>?](mpscnninstancenormalizationdatasource/gamma.md)
- [func label() -> String?](mpscnninstancenormalizationdatasource/label.md)
- [func load() -> Bool](mpscnninstancenormalizationdatasource/load.md)
- [func purge()](mpscnninstancenormalizationdatasource/purge.md)
- [func updateGammaAndBeta(with: any MTLCommandBuffer, instanceNormalizationStateBatch: [MPSCNNInstanceNormalizationGradientState]) -> MPSCNNNormalizationGammaAndBetaState?](mpscnninstancenormalizationdatasource/updategammaandbeta(with:instancenormalizationstatebatch:).md)
- [func updateGammaAndBeta(withInstanceNormalizationStateBatch: [MPSCNNInstanceNormalizationGradientState]) -> Bool](mpscnninstancenormalizationdatasource/updategammaandbeta(withinstancenormalizationstatebatch:).md)
### Type Properties
- [static var supportsSecureCoding: Bool](mpscnninstancenormalizationdatasource/supportssecurecoding.md)

## Relationships

### Inherits From
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPSCNNCrossChannelNormalizationNode](mpscnncrosschannelnormalizationnode.md)
  A representation of a normalization kernel across feature channels.
- [class MPSCNNLocalContrastNormalizationNode](mpscnnlocalcontrastnormalizationnode.md)
  A representation of a local-contrast normalization kernel.
- [class MPSCNNSpatialNormalizationNode](mpscnnspatialnormalizationnode.md)
  A representation of a spatial normalization kernel.
- [class MPSCNNBatchNormalizationGradientNode](mpscnnbatchnormalizationgradientnode.md)
  A representation of a gradient batch normalization kernel.
- [class MPSCNNBatchNormalizationNode](mpscnnbatchnormalizationnode.md)
  A representation of a batch normalization kernel.
- [protocol MPSCNNBatchNormalizationDataSource](mpscnnbatchnormalizationdatasource.md)
  A protocol that defines methods that a batch normalization state uses to initialize scale factors, bias terms, and batch statistics.
- [class MPSCNNInstanceNormalizationGradientNode](mpscnninstancenormalizationgradientnode.md)
  A representation of a gradient instance normalization kernel.
- [class MPSCNNInstanceNormalizationNode](mpscnninstancenormalizationnode.md)
  A representation of an instance normalization kernel.
- [class MPSCNNLocalContrastNormalizationGradientNode](mpscnnlocalcontrastnormalizationgradientnode.md)
  A representation of a gradient local-contrast normalization kernel.
- [class MPSCNNSpatialNormalizationGradientNode](mpscnnspatialnormalizationgradientnode.md)
  A representation of a gradient spatial normalization kernel.
- [class MPSCNNNormalizationNode](mpscnnnormalizationnode.md)
  Virtual base class for CNN normalization nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnninstancenormalizationdatasource)*