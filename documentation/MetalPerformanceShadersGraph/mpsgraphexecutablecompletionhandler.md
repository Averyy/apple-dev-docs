# MPSGraphExecutableCompletionHandler

**Framework**: Metal Performance Shaders Graph  
**Kind**: typealias

A notification when graph executable execution finishes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
typealias MPSGraphExecutableCompletionHandler = ([MPSGraphTensorData], (any Error)?) -> Void
```

## Parameters

- `results`: If no error, the results produced by the graph operation. If Graph hasn’t yet allocated the results, this will be  .
- `error`: If an error occurs, more information might be found here.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutablecompletionhandler)*