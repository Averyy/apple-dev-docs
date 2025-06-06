# MPSGraphCompilationCompletionHandler

**Framework**: Metal Performance Shaders Graph  
**Kind**: typealias

A notification that appears when compilation finishes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
typealias MPSGraphCompilationCompletionHandler = (MPSGraphExecutable, (any Error)?) -> Void
```

## Parameters

- `executable`: If no error, the executable produced by the compilation.
- `error`: If an error occurs, more information might be found here.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphcompilationcompletionhandler)*