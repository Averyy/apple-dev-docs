# ComputeNodeGraph.NodeDefinition.Kind.reinterpret(from:to:)

**Framework**: ComputeGraph  
**Kind**: case

Reinterpret one type scalar or vector type as another of the same number of size and bytes.

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
case reinterpret(from: ComputeNodeGraph.DataType, to: ComputeNodeGraph.DataType)
```

#### Discussion

Equivalent to calling Metal’s `as_type<>`


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/nodedefinition/kind-swift.enum/reinterpret(from:to:))*