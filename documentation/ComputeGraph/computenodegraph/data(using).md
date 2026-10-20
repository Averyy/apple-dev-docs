# data(using:)

**Framework**: Compute Graph  
**Kind**: method  
**Role**: Instance Method

Returns the graph encoded in the specified format.

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
func data(using format: ComputeNodeGraph.Format) throws -> Data
```

#### Return Value

The graph encoded using the specified format.

#### Discussion

To reconstruct the graph, pass the data to [`init(data:)`](./init%28data%29.md).

> **Throws**: An error if the graph can’t be encoded in the requested format.

## Parameters

- `format`: The serialization format to use when encoding the graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/data(using:))*