# targetTensors

**Framework**: Metal Performance Shaders Graph  
**Kind**: property  
**Role**: Instance Property

Tensors targeted by the graph, can be used to order the outputs when executable was created with a graph.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var targetTensors: [MPSGraphTensor]? { get }
```

```objc
@property (atomic, readonly, nullable) NSArray<MPSGraphTensor *> * targetTensors;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutable/targettensors)*