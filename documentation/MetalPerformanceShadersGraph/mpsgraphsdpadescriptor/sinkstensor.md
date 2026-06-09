# sinksTensor

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

An optional attention-sinks tensor of shape `[nHeads]`. Each element seeds the online-softmax accumulator for the corresponding query head with a virtual token logit, causing real-token attention weights to sum to less than one.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var sinksTensor: MPSGraphTensor? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphsdpadescriptor/sinkstensor)*