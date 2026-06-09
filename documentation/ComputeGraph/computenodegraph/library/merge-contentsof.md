# merge(contentsOf:)

**Framework**: ComputeGraph  
**Kind**: method

Merges nodes from specified library into this library.

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
final func merge(contentsOf library: ComputeNodeGraph.Library)
```

#### Discussion

Use this method to merge libraries. If two nodes have the same name and bundle, the nodes in `library` will replace ones in `self`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/library/merge(contentsof:))*