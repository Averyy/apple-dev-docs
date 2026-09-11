# readOutputs(_:)

**Framework**: RealityKit  
**Kind**: method

Returns all output buffers for the given output node.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func readOutputs(_ node: ComputeNodeGraph.NodeID) -> [any MTLBuffer]?
```

#### Return Value

An array of `MTLBuffer` objects, or `nil` if the node identifier is invalid or no output buffers are found.

## Parameters

- `node`: The node identifier whose output buffers should be read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphruntimecomponent/readoutputs(_:))*