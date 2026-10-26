# MLReshapeFrequencyHint

**Framework**: Core ML  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```c
enum MLReshapeFrequencyHint : NSInteger;
```

## Topics

### Enumeration Cases
- [MLReshapeFrequencyHintFrequent](./mlreshapefrequencyhint/mlreshapefrequencyhintfrequent.md)
  The input shape is expected to change frequently on each prediction sent to this loaded model instance. Core ML will try to minimize the latency associated with shape changes and avoid expensive shape-specific optimizations prior to prediction computation. While prediction computation may be slower for each specific shape, switching between shapes should be faster. This is the default.
- [MLReshapeFrequencyHintInfrequent](./mlreshapefrequencyhint/mlreshapefrequencyhintinfrequent.md)
  The input shape is expected to be stable and many/all predictions sent to this loaded model instance would use the same input shapes repeatedly. On the shape change, Core ML re-optimizes the internal engine for the new shape if possible. The re-optimization takes some time, but the subsequent predictions for the shape should run faster.

## See Also

### Enumerations
- [MLSpecializationStrategy](./mlspecializationstrategy.md)
  The optimization strategy for the model specialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlreshapefrequencyhint)*