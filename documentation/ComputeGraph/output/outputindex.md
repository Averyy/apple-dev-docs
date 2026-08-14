# output::outputIndex

**Framework**: Compute Graph  
**Kind**: func

Returns the index of the current output element being processed.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
uint output::outputIndex()
```

#### Return Value

The zero-based index of the current output element.

#### Discussion

This function provides the zero-based index of the output element within the current output range, useful for per-element computations and indexing operations. If sorting is active, this corresponds to the post-sorting ordering.

> **Note**: ![Graph](/images/com.apple.computegraph/output__outputIndex.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/output/outputindex)*