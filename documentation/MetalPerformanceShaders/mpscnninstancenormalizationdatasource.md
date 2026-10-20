# MPSCNNInstanceNormalizationDataSource

**Framework**: Metal Performance Shaders  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol MPSCNNInstanceNormalizationDataSource <NSObject, NSCopying>
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./mpscnninstancenormalizationdatasource/init%28coder%29.md)
### Instance Properties
- [var numberOfFeatureChannels: Int](./mpscnninstancenormalizationdatasource/numberoffeaturechannels.md)
### Instance Methods
- [func beta() -> UnsafeMutablePointer<Float>?](./mpscnninstancenormalizationdatasource/beta%28%29.md)
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpscnninstancenormalizationdatasource/copy%28with,device%29.md)
- [func encode(with: NSCoder)](./mpscnninstancenormalizationdatasource/encode%28with%29.md)
- [func epsilon() -> Float](./mpscnninstancenormalizationdatasource/epsilon%28%29.md)
- [func gamma() -> UnsafeMutablePointer<Float>?](./mpscnninstancenormalizationdatasource/gamma%28%29.md)
- [func label() -> String?](./mpscnninstancenormalizationdatasource/label%28%29.md)
- [func load() -> Bool](./mpscnninstancenormalizationdatasource/load%28%29.md)
- [func purge()](./mpscnninstancenormalizationdatasource/purge%28%29.md)
- [func updateGammaAndBeta(with: any MTLCommandBuffer, instanceNormalizationStateBatch: [MPSCNNInstanceNormalizationGradientState]) -> MPSCNNNormalizationGammaAndBetaState?](./mpscnninstancenormalizationdatasource/updategammaandbeta%28with,instancenormalizationstatebatch%29.md)
- [func updateGammaAndBeta(withInstanceNormalizationStateBatch: [MPSCNNInstanceNormalizationGradientState]) -> Bool](./mpscnninstancenormalizationdatasource/updategammaandbeta%28withinstancenormalizationstatebatch%29.md)
### Type Properties
- [static var supportsSecureCoding: Bool](./mpscnninstancenormalizationdatasource/supportssecurecoding.md)

## Relationships

### Inherits From
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Normalization Layer Nodes
- [class MPSCNNCrossChannelNormalizationNode](./mpscnncrosschannelnormalizationnode.md)
  A representation of a normalization kernel across feature channels.
- [class MPSCNNLocalContrastNormalizationNode](./mpscnnlocalcontrastnormalizationnode.md)
  A representation of a local-contrast normalization kernel.
- [class MPSCNNSpatialNormalizationNode](./mpscnnspatialnormalizationnode.md)
  A representation of a spatial normalization kernel.
- [class MPSCNNBatchNormalizationGradientNode](./mpscnnbatchnormalizationgradientnode.md)
  A representation of a gradient batch normalization kernel.
- [class MPSCNNBatchNormalizationNode](./mpscnnbatchnormalizationnode.md)
  A representation of a batch normalization kernel.
- [protocol MPSCNNBatchNormalizationDataSource](./mpscnnbatchnormalizationdatasource.md)
  A protocol that defines methods that a batch normalization state uses to initialize scale factors, bias terms, and batch statistics.
- [class MPSCNNInstanceNormalizationGradientNode](./mpscnninstancenormalizationgradientnode.md)
  A representation of a gradient instance normalization kernel.
- [class MPSCNNInstanceNormalizationNode](./mpscnninstancenormalizationnode.md)
  A representation of an instance normalization kernel.
- [class MPSCNNLocalContrastNormalizationGradientNode](./mpscnnlocalcontrastnormalizationgradientnode.md)
  A representation of a gradient local-contrast normalization kernel.
- [class MPSCNNSpatialNormalizationGradientNode](./mpscnnspatialnormalizationgradientnode.md)
  A representation of a gradient spatial normalization kernel.
- [class MPSCNNNormalizationNode](./mpscnnnormalizationnode.md)
  Virtual base class for CNN normalization nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnninstancenormalizationdatasource)*