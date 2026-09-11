# format

**Framework**: RealityKit  
**Kind**: property

The format of the vertex attribute.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var format: MTLVertexFormat { get set }
```

#### Discussion

When reading from a geometry modifier or surface shader, the value converts to its runtime representation using Metal’s standard rules. See `MTLVertexAttributeDescriptor.format` for details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/attribute/format)*