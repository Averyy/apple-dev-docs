# MPSGraphWhileBeforeBlock

**Framework**: Metal Performance Shaders Graph  
**Kind**: typealias

The block that executes before the condition evaluates for each iteration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
typealias MPSGraphWhileBeforeBlock = ([MPSGraphTensor], NSMutableArray) -> MPSGraphTensor
```

#### Return Value

Tensor MUST be set and have a single scalar value, used to decide between executing the body block or returning from the while loop.

## Parameters

- `inputTensors`: Input tensors to the  , for the first iteration will be same as initialInputs passed to the while loop.
- `resultTensors`: A valid   array with results forwarded to after block or returned from the while loop depending on the predicate tensor. It will be empty and the caller block should fill it up before returning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphwhilebeforeblock)*