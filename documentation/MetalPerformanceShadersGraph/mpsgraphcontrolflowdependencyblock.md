# MPSGraphControlFlowDependencyBlock

**Framework**: Metal Performance Shaders Graph  
**Kind**: typealias

The scope where all the operations defined in this block get control-dependency operations.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
typealias MPSGraphControlFlowDependencyBlock = () -> [MPSGraphTensor]
```

#### Return Value

A valid tensor with the results forwarded to the return of `controlDependency` call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphcontrolflowdependencyblock)*