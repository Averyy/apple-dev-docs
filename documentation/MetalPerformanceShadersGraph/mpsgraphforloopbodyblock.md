# MPSGraphForLoopBodyBlock

**Framework**: Metal Performance Shaders Graph  
**Kind**: typealias

A block for the body in the for loop.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
typealias MPSGraphForLoopBodyBlock = (MPSGraphTensor, [MPSGraphTensor]) -> [MPSGraphTensor]
```

#### Return Value

A valid MPSGraphTensor array with same count and corresponding element types as `initialIterationArguments` and return types of the `for` loop.

## Parameters

- `index`: The for loop index per iteration, it is a scalar tensor.
- `iterationArguments`: Arguments for this iteration, with the same count and corresponding element types as   and return types of the   loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphforloopbodyblock)*