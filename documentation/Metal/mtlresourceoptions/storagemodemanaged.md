# storageModeManaged

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

The CPU and GPU may maintain separate copies of the resource, and any changes need to be explicitly synchronized.

**Availability**:
- Mac Catalyst 13.0+ - Deprecated in 27.0
- macOS 10.11+ - Deprecated in 27.0

> **Deprecated**: Managed storage has no effect on Apple Silicon, use Shared storage instead

## Declaration

```swift
static var storageModeManaged: MTLResourceOptions { get }
```

```c
MTLResourceStorageModeManaged
```

#### Discussion

On Intel-based Mac computers, this is the default storage mode for [`MTLTexture`](../mtltexture.md) objects. In iOS and tvOS, the managed storage mode isn’t available. With managed storage, you synchronize changes between the CPU and GPU manually. For instructions and examples of resource synchronization, see [Synchronizing a managed resource in macOS](../synchronizing-a-managed-resource-in-macos.md).

For more guidance on how to choose storage modes, see [Setting resource storage modes](../setting-resource-storage-modes.md).

## See Also

### Specifying storage modes
- [static var storageModeShared: MTLResourceOptions](./storagemodeshared.md)
  The CPU and GPU share access to the resource, allocated in system memory.
- [static var storageModePrivate: MTLResourceOptions](./storagemodeprivate.md)
  The resource is only available to the GPU.
- [static var storageModeMemoryless: MTLResourceOptions](./storagemodememoryless.md)
  The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourceoptions/storagemodemanaged)*