# MPSCNNGroupNormalizationDataSource

**Framework**: Metal Performance Shaders  
**Kind**: protocol

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

## Topics

### Initializers
- [init?(coder: NSCoder)](mpscnngroupnormalizationdatasource/init(coder:).md)
### Instance Properties
- [var numberOfFeatureChannels: Int](mpscnngroupnormalizationdatasource/numberoffeaturechannels.md)
- [var numberOfGroups: Int](mpscnngroupnormalizationdatasource/numberofgroups.md)
### Instance Methods
- [func beta() -> UnsafeMutablePointer<Float>?](mpscnngroupnormalizationdatasource/beta.md)
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpscnngroupnormalizationdatasource/copy(with:device:).md)
- [func encode(with: NSCoder)](mpscnngroupnormalizationdatasource/encode(with:).md)
- [func epsilon() -> Float](mpscnngroupnormalizationdatasource/epsilon.md)
- [func gamma() -> UnsafeMutablePointer<Float>?](mpscnngroupnormalizationdatasource/gamma.md)
- [func label() -> String?](mpscnngroupnormalizationdatasource/label.md)
- [func updateGammaAndBeta(with: any MTLCommandBuffer, groupNormalizationStateBatch: [MPSCNNGroupNormalizationGradientState]) -> MPSCNNNormalizationGammaAndBetaState?](mpscnngroupnormalizationdatasource/updategammaandbeta(with:groupnormalizationstatebatch:).md)
- [func updateGammaAndBeta(withGroupNormalizationStateBatch: [MPSCNNGroupNormalizationGradientState]) -> Bool](mpscnngroupnormalizationdatasource/updategammaandbeta(withgroupnormalizationstatebatch:).md)
### Type Properties
- [static var supportsSecureCoding: Bool](mpscnngroupnormalizationdatasource/supportssecurecoding.md)

## Relationships

### Inherits From
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnngroupnormalizationdatasource)*