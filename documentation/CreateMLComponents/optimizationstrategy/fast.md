# OptimizationStrategy.fast

**Framework**: Create ML Components  
**Kind**: case

An optimization strategy that minimizes computation time.

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
case fast
```

#### Discussion

Select this strategy for smooth problems that fit in memory.

## See Also

- [OptimizationStrategy.automatic](optimizationstrategy/automatic.md)
  Chooses the best optimization strategy based on the problem size and configuration.
- [OptimizationStrategy.lowMemory](optimizationstrategy/lowmemory.md)
  An optimization strategy that minimizes memory use.
- [OptimizationStrategy.nonSmooth](optimizationstrategy/nonsmooth.md)
  An optimization strategy that can handle non-smooth problems.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/optimizationstrategy/fast)*