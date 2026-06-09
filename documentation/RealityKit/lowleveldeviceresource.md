# LowLevelDeviceResource

**Framework**: RealityKit  
**Kind**: class

Encapsulates a GPU device resource created by the application. On visionOS, resources must be allocated in shared memory that can be used by the renderer process. Once a device resource is in use by the renderer, changing its contents is unsafe and undefined.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class LowLevelDeviceResource
```

## Topics

### Creating a device resource
- [init(textureDescriptor: MTLTextureDescriptor, iosurface: IOSurfaceRef, plane: Int) throws](lowleveldeviceresource/init(texturedescriptor:iosurface:plane:).md)
  Creates a new [`LowLevelDeviceResource`](lowleveldeviceresource.md) from the specified `IOSurface`.
- [init(sharedTextureHandle: MTLSharedTextureHandle) throws](lowleveldeviceresource/init(sharedtexturehandle:).md)
  Creates a new [`LowLevelDeviceResource`](lowleveldeviceresource.md) from the specified Metal shared texture handle. Throws if an MTLTexture cannot be created from the specified handle.
### Initializers
- [init(texture: any MTLTexture)](lowleveldeviceresource/init(texture:).md)
  Creates a new [`LowLevelDeviceResource`](lowleveldeviceresource.md) from the specified Metal texture. This is not available on visionOS; device resources on this platform must be initialized from a shared texture using `init(sharedTextureHandle:)` instead.

## See Also

- [class LowLevelMeshResource](lowlevelmeshresource.md)
  A container for vertex and index data in a custom format.
- [class LowLevelMeshPart](lowlevelmeshpart.md)
  An object that describes a range of primitives to draw from a mesh resource.
- [class LowLevelMeshInstance](lowlevelmeshinstance.md)
  A single drawable object pairing a mesh part with a compiled pipeline state, optional per-draw argument tables, a transform, and a sort category.
- [class LowLevelMeshInstanceArray](lowlevelmeshinstancearray.md)
  A fixed-capacity collection of mesh instances submitted to the renderer.
- [class LowLevelInstanceTransformResource](lowlevelinstancetransformresource.md)
  A GPU-managed buffer that stores an array of per-instance transforms for GPU instancing.
- [class LowLevelBufferResource](lowlevelbufferresource.md)
  A GPU-managed buffer for arbitrary per-draw data such as uniforms and custom parameters.
- [struct LowLevelBufferSlice](lowlevelbufferslice.md)
  A reference to a sub-range of a buffer resource, used to bind a region of a buffer to an argument table slot.
- [class LowLevelTextureResource](lowleveltextureresource.md)
  A container for texture data in a custom format.
- [class LowLevelMaterialResource](lowlevelmaterialresource.md)
  A compiled material composed of three independently-replaceable shader stages.
- [struct BoundingSphereBox](boundingspherebox.md)
  A combined bounding volume consisting of a bounding sphere and an optional axis-aligned bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeviceresource)*