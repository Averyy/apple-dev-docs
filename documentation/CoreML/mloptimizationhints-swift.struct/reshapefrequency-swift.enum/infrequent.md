# MLOptimizationHints.ReshapeFrequency.infrequent

**Framework**: Core ML  
**Kind**: case

The input shape is expected to be stable and many/all predictions sent to this loaded model instance would use the same input shapes repeatedly. On the shape change, Core ML re-optimizes the internal engine for the new shape if possible. The re-optimization takes some time, but the subsequent predictions for the shape should run faster.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.0+
- watchOS 10.4+

## Declaration

```swift
case infrequent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mloptimizationhints-swift.struct/reshapefrequency-swift.enum/infrequent)*