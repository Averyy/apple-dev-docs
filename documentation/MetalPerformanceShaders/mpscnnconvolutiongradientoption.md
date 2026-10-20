# MPSCNNConvolutionGradientOption

**Framework**: Metal Performance Shaders  
**Kind**: struct  
**Role**: Structure

Options that control which gradient to compute during backward propagation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct MPSCNNConvolutionGradientOption
```

```c
enum MPSCNNConvolutionGradientOption : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./mpscnnconvolutiongradientoption/init%28rawvalue%29.md)
### Type Properties
- [static var all: MPSCNNConvolutionGradientOption](./mpscnnconvolutiongradientoption/all.md)
- [static var gradientWithData: MPSCNNConvolutionGradientOption](./mpscnnconvolutiongradientoption/gradientwithdata.md)
- [static var gradientWithWeightsAndBias: MPSCNNConvolutionGradientOption](./mpscnnconvolutiongradientoption/gradientwithweightsandbias.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiongradientoption)*