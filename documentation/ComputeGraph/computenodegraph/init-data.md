# init(data:)

**Framework**: Compute Graph  
**Kind**: init

Creates a graph by decoding a computegraph.

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
init(data: Data) throws
```

#### Discussion

This initializer infers the serialization format from the contents of `data`, so you can pass data produced by [`data(using:)`](computenodegraph/data(using:).md) regardless of the [`ComputeNodeGraph.Format`](computenodegraph/format.md) you chose when encoding.

> **Note**: An error if `data` isn’t a recognized graph format, or if the contents can’t be decoded into a valid graph.

## Parameters

- `data`: The encoded graph data to decode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/init(data:))*