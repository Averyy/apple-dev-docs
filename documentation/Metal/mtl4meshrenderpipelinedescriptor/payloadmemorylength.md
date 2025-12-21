# payloadMemoryLength

**Framework**: Metal  
**Kind**: property

Reserves storage for the object-to-mesh stage payload.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var payloadMemoryLength: Int { get set }
```

#### Discussion

This property determines the size, in bytes, of the buffer you indicate via the Metal Shading Language `[[payload]]` attribute in the object and mesh shader functions of the mesh render pipeline.

If this value is `0`, Metal derives the size from the (dereferenced) type you declare for the payload in the object shader function. If the type is a pointer, Metal reserves space for a single element.

The default value is `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor/payloadmemorylength)*