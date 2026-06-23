# readOutputs(_:)

**Framework**: RealityKit  
**Kind**: method

Returns all output buffers for the given output node.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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