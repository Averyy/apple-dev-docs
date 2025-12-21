# vertexDescriptor

**Framework**: Metal  
**Kind**: property

Configures an optional vertex descriptor for the vertex input.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@NSCopying
var vertexDescriptor: MTLVertexDescriptor? { get set }
```

#### Discussion

A vertex descriptor specifies the layout of your vertex data, allowing your vertex shaders to access the content in your vertex arrays via the `[[stage_in]]` attribute in Metal Shading Language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpipelinedescriptor/vertexdescriptor)*