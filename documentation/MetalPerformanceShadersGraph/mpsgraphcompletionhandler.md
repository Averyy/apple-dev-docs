# MPSGraphCompletionHandler

**Framework**: Metal Performance Shaders Graph  
**Kind**: typealias

A notification that appears when graph execution finishes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
typealias MPSGraphCompletionHandler = ([MPSGraphTensor : MPSGraphTensorData], (any Error)?) -> Void
```

## Parameters

- `resultsDictionary`: If no error, the results dictionary produced by the graph operation.
- `error`: If an error occurs, more information might be found here.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphcompletionhandler)*