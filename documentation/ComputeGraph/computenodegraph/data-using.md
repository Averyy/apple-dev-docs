# data(using:)

**Framework**: ComputeGraph  
**Kind**: method

Returns the graph encoded in the specified format.

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
func data(using format: ComputeNodeGraph.Format) throws -> Data
```

#### Return Value

The graph encoded using the specified format.

#### Discussion

To reconstruct the graph, pass the data to [`init(data:)`](computenodegraph/init(data:).md).

> **Note**: An error if the graph can’t be encoded in the requested format.

## Parameters

- `format`: The serialization format to use when encoding the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/data(using:))*