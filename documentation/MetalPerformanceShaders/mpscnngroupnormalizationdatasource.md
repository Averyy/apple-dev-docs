# MPSCNNGroupNormalizationDataSource

**Framework**: Metal Performance Shaders  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol MPSCNNGroupNormalizationDataSource : NSCopying, NSObjectProtocol
```

```objc
@protocol MPSCNNGroupNormalizationDataSource <NSObject, NSCopying>
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./mpscnngroupnormalizationdatasource/init%28coder%29.md)
### Instance Properties
- [var numberOfFeatureChannels: Int](./mpscnngroupnormalizationdatasource/numberoffeaturechannels.md)
- [var numberOfGroups: Int](./mpscnngroupnormalizationdatasource/numberofgroups.md)
### Instance Methods
- [func beta() -> UnsafeMutablePointer<Float>?](./mpscnngroupnormalizationdatasource/beta%28%29.md)
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpscnngroupnormalizationdatasource/copy%28with,device%29.md)
- [func encode(with: NSCoder)](./mpscnngroupnormalizationdatasource/encode%28with%29.md)
- [func epsilon() -> Float](./mpscnngroupnormalizationdatasource/epsilon%28%29.md)
- [func gamma() -> UnsafeMutablePointer<Float>?](./mpscnngroupnormalizationdatasource/gamma%28%29.md)
- [func label() -> String?](./mpscnngroupnormalizationdatasource/label%28%29.md)
- [func updateGammaAndBeta(with: any MTLCommandBuffer, groupNormalizationStateBatch: [MPSCNNGroupNormalizationGradientState]) -> MPSCNNNormalizationGammaAndBetaState?](./mpscnngroupnormalizationdatasource/updategammaandbeta%28with,groupnormalizationstatebatch%29.md)
- [func updateGammaAndBeta(withGroupNormalizationStateBatch: [MPSCNNGroupNormalizationGradientState]) -> Bool](./mpscnngroupnormalizationdatasource/updategammaandbeta%28withgroupnormalizationstatebatch%29.md)
### Type Properties
- [static var supportsSecureCoding: Bool](./mpscnngroupnormalizationdatasource/supportssecurecoding.md)

## Relationships

### Inherits From
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnngroupnormalizationdatasource)*