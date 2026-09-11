# sinksTensor

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

An optional attention-sinks tensor of shape `[nHeads]`. Each element seeds the online-softmax accumulator for the corresponding query head with a virtual token logit, causing real-token attention weights to sum to less than one.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var sinksTensor: MPSGraphTensor? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphsdpadescriptor/sinkstensor)*