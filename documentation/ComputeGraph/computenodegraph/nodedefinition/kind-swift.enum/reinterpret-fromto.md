# ComputeNodeGraph.NodeDefinition.Kind.reinterpret(from:to:)

**Framework**: Compute Graph  
**Kind**: case

Reinterpret one type scalar or vector type as another of the same number of size and bytes.

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
case reinterpret(from: ComputeNodeGraph.DataType, to: ComputeNodeGraph.DataType)
```

#### Discussion

Equivalent to calling Metal’s `as_type<>`


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/nodedefinition/kind-swift.enum/reinterpret(from:to:))*