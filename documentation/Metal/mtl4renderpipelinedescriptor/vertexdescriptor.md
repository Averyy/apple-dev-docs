# vertexDescriptor

**Framework**: Metal  
**Kind**: property

Configures an optional vertex descriptor for the vertex input.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@NSCopying
var vertexDescriptor: MTLVertexDescriptor? { get set }
```

#### Discussion

A vertex descriptor specifies the layout of your vertex data, allowing your vertex shaders to access the content in your vertex arrays via the `[[stage_in]]` attribute in Metal Shading Language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpipelinedescriptor/vertexdescriptor)*