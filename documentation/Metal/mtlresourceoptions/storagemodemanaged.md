# storageModeManaged

**Framework**: Metal  
**Kind**: property

The CPU and GPU may maintain separate copies of the resource, and any changes must be explicitly synchronized.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.11+

## Declaration

```swift
static var storageModeManaged: MTLResourceOptions { get }
```

#### Discussion

On Intel-based Mac computers, this is the default storage mode for [`MTLTexture`](mtltexture.md) objects. In iOS and tvOS, the managed storage mode isn’t available. With managed storage, you synchronize changes between the CPU and GPU manually. For instructions and examples of resource synchronization, see [`Synchronizing a Managed Resource in macOS`](synchronizing-a-managed-resource-in-macos.md).

For more guidance on how to choose storage modes, see [`Setting Resource Storage Modes`](setting-resource-storage-modes.md).

## See Also

- [static var storageModeShared: MTLResourceOptions](mtlresourceoptions/storagemodeshared.md)
  The CPU and GPU share access to the resource, allocated in system memory.
- [static var storageModePrivate: MTLResourceOptions](mtlresourceoptions/storagemodeprivate.md)
  The resource is only available to the GPU.
- [static var storageModeMemoryless: MTLResourceOptions](mtlresourceoptions/storagemodememoryless.md)
  The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourceoptions/storagemodemanaged)*