# setOutputEnabled(_:enabled:)

**Framework**: RealityKit  
**Kind**: method

Sets the enable state of an output identified by ID

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
mutating func setOutputEnabled(_ outputID: ComputeNodeGraph.NodeID, enabled: Bool)
```

#### Discussion

This will cause the output mesh to disappear, and output stages to stop executing. The simulation, however, will continue to execute. See [`pause()`](computegraphcomponent/pause().md), [`play()`](computegraphcomponent/play().md), and `RealityKit.Entity.isEnabled` to control the simulation as a whole


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent/setoutputenabled(_:enabled:))*