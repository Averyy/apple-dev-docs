# readOutput(_:)

**Framework**: RealityKit  
**Kind**: method

Returns the output buffer for the port at the given address.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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