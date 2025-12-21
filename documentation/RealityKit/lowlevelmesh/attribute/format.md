# format

**Framework**: RealityKit  
**Kind**: property

The format of the vertex attribute.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var format: MTLVertexFormat
```

#### Discussion

When reading from a geometry modifier or surface shader, the value converts to its runtime representation using Metal’s standard rules.

For details about Metal’s standard rules, see [`format`](https://developer.apple.com/documentation/Metal/MTLVertexAttributeDescriptor/format).

## See Also

- [var offset: Int](lowlevelmesh/attribute/offset.md)
  The location of an attribute in vertex data, determined by the byte offset from the start of the vertex data.
- [var layoutIndex: Int](lowlevelmesh/attribute/layoutindex.md)
  The index of the layout that contains this attribute.
- [var semantic: LowLevelMesh.VertexSemantic](lowlevelmesh/attribute/semantic.md)
  The semantic of the vertex attribute, which describes how you want RealityKit to interpret the attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/attribute/format)*