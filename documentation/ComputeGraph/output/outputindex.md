# output::outputIndex

**Framework**: ComputeGraph  
**Kind**: func

Returns the index of the current output element being processed.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
uint output::outputIndex()
```

#### Return Value

The zero-based index of the current output element.

#### Discussion

This function provides the zero-based index of the output element within the current output range, useful for per-element computations and indexing operations. If sorting is active, this corresponds to the post-sorting ordering.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/626df9bd64141a722fb48fd6e0895b14/output__outputIndex.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/output/outputindex)*