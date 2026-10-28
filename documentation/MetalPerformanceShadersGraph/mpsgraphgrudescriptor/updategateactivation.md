# updateGateActivation

**Framework**: Metal Performance Shaders Graph  
**Kind**: property  
**Role**: Instance Property

A parameter that defines the activation function to use with the update-gate of the GRU operation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var updateGateActivation: MPSGraphRNNActivation { get set }
```

```objc
@property (nonatomic, readwrite) MPSGraphRNNActivation updateGateActivation;
```

## Discussion

Default value: `MPSGraphRNNActivationSigmoid`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphgrudescriptor/updategateactivation)*