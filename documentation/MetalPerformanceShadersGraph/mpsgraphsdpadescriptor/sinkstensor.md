# sinksTensor

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

An optional attention-sinks tensor of shape `[nHeads]`. Each element seeds the online-softmax accumulator for the corresponding query head with a virtual token logit, causing real-token attention weights to sum to less than one.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var sinksTensor: MPSGraphTensor? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphsdpadescriptor/sinkstensor)*