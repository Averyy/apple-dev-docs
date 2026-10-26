# MLSpecializationStrategy

**Framework**: Core ML  
**Kind**: enum  
**Role**: Enumeration

The optimization strategy for the model specialization.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```c
enum MLSpecializationStrategy : NSInteger;
```

## Topics

### Strategies
- [MLSpecializationStrategyDefault](./mlspecializationstrategy/mlspecializationstrategydefault.md)
  The strategy that works well for most applications.
- [MLSpecializationStrategyFastPrediction](./mlspecializationstrategy/mlspecializationstrategyfastprediction.md)
  Prefer the prediction latency at the potential cost of specialization time, memory footprint, and the disk space usage of specialized artifacts.

## See Also

### Enumerations
- [MLReshapeFrequencyHint](./mlreshapefrequencyhint.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlspecializationstrategy)*