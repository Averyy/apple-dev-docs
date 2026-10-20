# cellGateActivation

**Framework**: Metal Performance Shaders Graph  
**Kind**: property  
**Role**: Instance Property

A parameter that defines the activation function used with the cell gate of the LSTM operation.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
var cellGateActivation: MPSGraphRNNActivation { get set }
```

```objc
@property (nonatomic, readwrite) MPSGraphRNNActivation cellGateActivation;
```

#### Discussion

Default value: `MPSGraphRNNActivationTanh`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphlstmdescriptor/cellgateactivation)*