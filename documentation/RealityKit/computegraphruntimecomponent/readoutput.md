# readOutput(_:)

**Framework**: RealityKit  
**Kind**: method

Returns the output buffer for the port at the given address.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func readOutput(_ port: ComputeNodeGraph.Port.Address) -> (any MTLBuffer)?
```

#### Return Value

The `MTLBuffer` for that port, or `nil` if not found.

## Parameters

- `port`: The port address of the output to read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphruntimecomponent/readoutput(_:))*