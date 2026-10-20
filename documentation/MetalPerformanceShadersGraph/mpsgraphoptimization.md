# MPSGraphOptimization

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum  
**Role**: Enumeration

The optimization levels to trade compilation time for even more runtime performance by running more passes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSGraphOptimization
```

```c
enum MPSGraphOptimization : uint64_t;
```

## Topics

### Enumeration Cases
- [MPSGraphOptimization.level0](./mpsgraphoptimization/level0.md)
  Graph performs core optimizations only.
- [MPSGraphOptimization.level1](./mpsgraphoptimization/level1.md)
  Graph performs additional Optimizations, like using the placement pass to dispatch across different HW blocks like the NeuralEngine and CPU along with the GPU.
### Initializers
- [init?(rawValue: UInt64)](./mpsgraphoptimization/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphoptimization)*