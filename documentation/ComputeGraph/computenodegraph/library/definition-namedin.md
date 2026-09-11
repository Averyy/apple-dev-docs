# definition(named:in:)

**Framework**: Compute Graph  
**Kind**: method

Returns the first node definition with the given name, or `nil` if none is found.

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
final func definition(named name: String, in bundle: String? = nil) -> ComputeNodeGraph.NodeDefinition?
```

#### Discussion

Pass `nil` for `bundle` to search across all bundles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/library/definition(named:in:))*