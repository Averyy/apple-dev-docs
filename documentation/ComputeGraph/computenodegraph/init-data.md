# init(data:)

**Framework**: Compute Graph  
**Kind**: init

Creates a graph by decoding a computegraph.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro ?+

## Declaration

```swift
init(data: Data) throws
```

#### Discussion

This initializer infers the serialization format from the contents of `data`, so you can pass data produced by [`data(using:)`](computenodegraph/data(using:).md) regardless of the [`ComputeNodeGraph.Format`](computenodegraph/format.md) you chose when encoding.

> **Note**: An error if `data` isn’t a recognized graph format, or if the contents can’t be decoded into a valid graph.

## Parameters

- `data`: The encoded graph data to decode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/init(data:))*