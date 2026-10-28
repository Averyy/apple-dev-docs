# init(pipelines:)

**Framework**: Compute Graph  
**Kind**: init  
**Role**: Initializer

Initialize a ComputeGraphSimulation for the given pipelines, or a default pipeline if not specified.

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
convenience init(pipelines: ComputeNodeGraph.Pipelines?)
```

## Discussion

The simulation will use the ComputeGraphFramework’s default queue for operations such as [`fastForward()`](./fastforward%28%29.md) and resetting after setting the pipeline.

Prefer `init(pipeline:commandQueue:)` to this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/init(pipelines:))*