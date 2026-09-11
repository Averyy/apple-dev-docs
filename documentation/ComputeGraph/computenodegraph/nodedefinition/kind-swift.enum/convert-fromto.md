# ComputeNodeGraph.NodeDefinition.Kind.convert(from:to:)

**Framework**: Compute Graph  
**Kind**: case

Convert from one primitive MTLDataType to another.

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
case convert(from: ComputeNodeGraph.DataType, to: ComputeNodeGraph.DataType)
```

#### Discussion

Equivalent to calling Metal’s constructor of `to` with a value of type `from`


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/nodedefinition/kind-swift.enum/convert(from:to:))*