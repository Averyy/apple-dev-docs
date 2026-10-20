# init(pipelines:commandQueue:)

**Framework**: Compute Graph  
**Kind**: init  
**Role**: Initializer

Initialize a ComputeGraphSimulation for the given pipelines

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro

## Declaration

```swift
convenience init(pipelines: ComputeNodeGraph.Pipelines, commandQueue: any MTLCommandQueue)
```

#### Discussion

The simulation will use the provided command queue for operations such as [`fastForward()`](./fastforward%28%29.md) and resetting the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/init(pipelines:commandqueue:))*