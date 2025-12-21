# storageModeShared

**Framework**: Metal  
**Kind**: property

The CPU and GPU share access to the resource, allocated in system memory.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static var storageModeShared: MTLResourceOptions { get }
```

#### Discussion

This is the default storage mode for [`MTLBuffer`](mtlbuffer.md) instances on integrated GPUs and both [`MTLBuffer`](mtlbuffer.md) and [`MTLTexture`](mtltexture.md) instances on Apple silicon GPUs. On non-Apple family GPUs, the shared storage mode isn’t available for [`MTLTexture`](mtltexture.md) instances.

When either the CPU or GPU changes the contents of the resource, you’re responsible for synchronizing access to the texture from the other participant. Ensure that all changes you schedule on either the CPU or GPU for a resource that uses shared memory complete before accessing that resource on the other processor.

For more guidance on how to choose storage modes, see [`Setting resource storage modes`](setting-resource-storage-modes.md).

## See Also

- [static var storageModeManaged: MTLResourceOptions](mtlresourceoptions/storagemodemanaged.md)
  The CPU and GPU may maintain separate copies of the resource, and any changes need to be explicitly synchronized.
- [static var storageModePrivate: MTLResourceOptions](mtlresourceoptions/storagemodeprivate.md)
  The resource is only available to the GPU.
- [static var storageModeMemoryless: MTLResourceOptions](mtlresourceoptions/storagemodememoryless.md)
  The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourceoptions/storagemodeshared)*