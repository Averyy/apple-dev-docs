# OptimizationStrategy.nonSmooth

**Framework**: Create ML Components  
**Kind**: case

An optimization strategy that can handle non-smooth problems.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
case nonSmooth
```

#### Discussion

Select this strategy when using L1 regularization. Using L1 regularization causes the optimization problem to be non-smooth. Other optimization strategies rely on the optimization problem being smooth and will likely fail to converge when using L1 regularization.

## See Also

- [OptimizationStrategy.automatic](optimizationstrategy/automatic.md)
  Chooses the best optimization strategy based on the problem size and configuration.
- [OptimizationStrategy.fast](optimizationstrategy/fast.md)
  An optimization strategy that minimizes computation time.
- [OptimizationStrategy.lowMemory](optimizationstrategy/lowmemory.md)
  An optimization strategy that minimizes memory use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/optimizationstrategy/nonsmooth)*