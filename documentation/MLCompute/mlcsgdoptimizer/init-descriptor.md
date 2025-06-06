# init(descriptor:)

**Framework**: ML Compute  
**Kind**: init

Creates an SGD optimizer with the descriptor you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(descriptor optimizerDescriptor: MLCOptimizerDescriptor)
```

#### Return Value

An SGD optimizer.

#### Discussion

Sets [`momentumScale`](mlcsgdoptimizer/momentumscale.md) to `0.0` and [`usesNesterovMomentum`](mlcsgdoptimizer/usesnesterovmomentum.md) to `false` by default.

## Parameters

- `optimizerDescriptor`: An object you use to configure the optimizer.

## See Also

- [convenience init(descriptor: MLCOptimizerDescriptor, momentumScale: Float, usesNesterovMomentum: Bool)](mlcsgdoptimizer/init(descriptor:momentumscale:usesnesterovmomentum:).md)
  Create an SGD optimizer with the descriptor, momentum scale, and option to enable Nesterov momentum that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsgdoptimizer/init(descriptor:))*