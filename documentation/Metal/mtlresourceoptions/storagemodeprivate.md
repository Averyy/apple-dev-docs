# storageModePrivate

**Framework**: Metal  
**Kind**: property

The resource is only available to the GPU.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static var storageModePrivate: MTLResourceOptions { get }
```

#### Discussion

Metal may apply additional optimizations to private resources that aren’t allowed on shared or managed resources.

For more guidance on how to choose storage modes, see [`Setting resource storage modes`](setting-resource-storage-modes.md).

## See Also

- [static var storageModeShared: MTLResourceOptions](mtlresourceoptions/storagemodeshared.md)
  The CPU and GPU share access to the resource, allocated in system memory.
- [static var storageModeManaged: MTLResourceOptions](mtlresourceoptions/storagemodemanaged.md)
  The CPU and GPU may maintain separate copies of the resource, and any changes need to be explicitly synchronized.
- [static var storageModeMemoryless: MTLResourceOptions](mtlresourceoptions/storagemodememoryless.md)
  The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourceoptions/storagemodeprivate)*