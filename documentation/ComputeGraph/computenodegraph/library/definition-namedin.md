# definition(named:in:)

**Framework**: Compute Graph  
**Kind**: method

Returns the first node definition with the given name, or `nil` if none is found.

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
final func definition(named name: String, in bundle: String? = nil) -> ComputeNodeGraph.NodeDefinition?
```

#### Discussion

Pass `nil` for `bundle` to search across all bundles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/library/definition(named:in:))*