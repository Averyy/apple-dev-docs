# GLKMesh

**Framework**: GLKit  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 9.0+ - Deprecated in 12.0
- iPadOS 9.0+ - Deprecated in 12.0
- macOS 10.11+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class GLKMesh
```

```objc
@interface GLKMesh : NSObject
```

## Topics

### Initializers
- [init(mesh: MDLMesh) throws](./glkmesh/init%28mesh%29.md)
### Instance Properties
- [var name: String](./glkmesh/name.md)
- [var submeshes: [GLKSubmesh]](./glkmesh/submeshes.md)
- [var vertexBuffers: [GLKMeshBuffer]](./glkmesh/vertexbuffers.md)
- [var vertexCount: Int](./glkmesh/vertexcount.md)
- [var vertexDescriptor: MDLVertexDescriptor](./glkmesh/vertexdescriptor.md)
### Type Methods
- [class func newMeshes(from: MDLAsset, sourceMeshes: AutoreleasingUnsafeMutablePointer<NSArray?>?) throws -> [GLKMesh]](./glkmesh/newmeshes%28from,sourcemeshes%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Mesh Data Management
- [class GLKMeshBuffer](./glkmeshbuffer.md)
- [class GLKMeshBufferAllocator](./glkmeshbufferallocator.md)
- [class GLKSubmesh](./glksubmesh.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmesh)*