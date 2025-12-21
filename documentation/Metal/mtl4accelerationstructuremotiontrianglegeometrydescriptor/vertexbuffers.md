# vertexBuffers

**Framework**: Metal  
**Kind**: property

Assigns a buffer where each entry contains a reference to a vertex buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var vertexBuffers: MTL4BufferRange { get set }
```

#### Discussion

This property references a buffer that conceptually represents an array with one entry for each keyframe in the motion animation. Each one of these entries consists of a [`MTL4BufferRange`](mtl4bufferrange.md) that, in turn, references a vertex buffer containing the vertex data for the keyframe.

You are responsible for ensuring the buffer address is not zero for the top-level buffer, as well as for all the vertex buffers it references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotiontrianglegeometrydescriptor/vertexbuffers)*