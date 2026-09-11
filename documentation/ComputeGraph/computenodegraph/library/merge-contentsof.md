# merge(contentsOf:)

**Framework**: Compute Graph  
**Kind**: method

Merges nodes from specified library into this library.

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
final func merge(contentsOf library: ComputeNodeGraph.Library)
```

#### Discussion

Use this method to merge libraries. If two nodes have the same name and bundle, the nodes in `library` will replace ones in `self`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/library/merge(contentsof:))*