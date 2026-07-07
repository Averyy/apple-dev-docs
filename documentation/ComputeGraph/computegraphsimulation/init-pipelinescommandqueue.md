# init(pipelines:commandQueue:)

**Framework**: Compute Graph  
**Kind**: init

Initialize a ComputeGraphSimulation for the given pipelines

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro ?+

## Declaration

```swift
convenience init(pipelines: ComputeNodeGraph.Pipelines, commandQueue: any MTLCommandQueue)
```

#### Discussion

The simulation will use the provided command queue for operations such as [`fastForward()`](computegraphsimulation/fastforward().md) and resetting the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/init(pipelines:commandqueue:))*