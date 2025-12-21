# reshapeFrequency

**Framework**: Core ML  
**Kind**: property

The anticipated reshape frequency

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
var reshapeFrequency: MLOptimizationHints.ReshapeFrequency
```

#### Discussion

CoreML framework needs to reshape the model with new shapes for models with flexible input. Specify the anticipated reshape frequency (frequent or infrequent), so that the framework can optimize for fast shape switching or fast prediction on seen shapes.

The default value is frequent, which means CoreML tries to switch to new shapes as fast as possible

## See Also

- [MLOptimizationHints.ReshapeFrequency](mloptimizationhints-swift.struct/reshapefrequency-swift.enum.md)
  The anticipated frequency of changing input shapes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mloptimizationhints-swift.struct/reshapefrequency-swift.property)*