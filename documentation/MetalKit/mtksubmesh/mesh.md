# mesh

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

The parent mesh containing the vertex data of this submesh.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
weak var mesh: MTKMesh? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) MTKMesh * mesh;
```

#### Discussion

The buffer of this parent mesh should be set in the encoder before a call to [`drawIndexedPrimitives(type:indexCount:indexType:indexBuffer:indexBufferOffset:)`](../../Metal/mtlrendercommandencoder/drawindexedprimitives%28type,indexcount,indextype,indexbuffer,indexbufferoffset%29.md) is made.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtksubmesh/mesh)*