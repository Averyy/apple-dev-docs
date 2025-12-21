# compute

**Framework**: Metal  
**Kind**: property

A tensor context that applies to compute encoders.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static var compute: MTLTensorUsage { get }
```

#### Discussion

You can use tensors with this context in [`MTL4ComputeCommandEncoder`](mtl4computecommandencoder.md) or [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorusage/compute)*