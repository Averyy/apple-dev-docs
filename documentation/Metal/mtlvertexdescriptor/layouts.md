# layouts

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

An array of state data that describes how data are fetched by a vertex shader function when rendering primitives.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var layouts: MTLVertexBufferLayoutDescriptorArray { get }
```

```objc
@property (readonly) MTLVertexBufferLayoutDescriptorArray * layouts;
```

## See Also

### Accessing the vertex buffer layouts and vertex attributes
- [var attributes: MTLVertexAttributeDescriptorArray](./attributes.md)
  An array of state data that describes how vertex attribute data is stored in memory and is mapped to arguments for a vertex shader function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexdescriptor/layouts)*