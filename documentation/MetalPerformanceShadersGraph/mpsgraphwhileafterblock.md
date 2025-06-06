# MPSGraphWhileAfterBlock

**Framework**: Metal Performance Shaders Graph  
**Kind**: typealias

The block that executes after the condition evaluates for each iteration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
typealias MPSGraphWhileAfterBlock = ([MPSGraphTensor]) -> [MPSGraphTensor]
```

#### Return Value

A valid `MPSGraphTensor` array with results forwarded to the condition block.

## Parameters

- `bodyBlockArguments`: Inputs to the body of the while loop passed by the condition block return, and should be the same element types as the return of the while loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphwhileafterblock)*