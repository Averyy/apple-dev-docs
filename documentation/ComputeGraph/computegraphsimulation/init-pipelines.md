# init(pipelines:)

**Framework**: ComputeGraph  
**Kind**: init

Initialize a ComputeGraphSimulation for the given pipelines, or a default pipeline if not specified.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
convenience init(pipelines: ComputeNodeGraph.Pipelines?)
```

#### Discussion

The simulation will use the ComputeGraphFramework’s default queue for operations such as [`fastForward()`](computegraphsimulation/fastforward().md) and resetting after setting the pipeline.

Prefer `init(pipeline:commandQueue:)` to this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/init(pipelines:))*