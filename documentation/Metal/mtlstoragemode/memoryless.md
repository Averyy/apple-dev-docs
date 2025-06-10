# MTLStorageMode.memoryless

**Framework**: Metal  
**Kind**: case

The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case memoryless
```

## Mentions

- [Choosing a Resource Storage Mode for Apple GPUs](choosing-a-resource-storage-mode-for-apple-gpus.md)
- [Reducing the Memory Footprint of Metal Apps](reducing-the-memory-footprint-of-metal-apps.md)
- [Setting Resource Storage Modes](setting-resource-storage-modes.md)

#### Discussion

The memoryless storage mode uses tile memory, and is only available on Apple family GPUs. Memoryless resources are temporary targets used in a pass and you can’t access their contents with [`MTLLoadAction.load`](mtlloadaction/load.md) or [`MTLStoreAction.store`](mtlstoreaction/store.md).

Use memoryless resources for temporary elements used only within a single pass. For example, most render passes don’t store depth attachments and multisample attachments to memory. You can significantly reduce your memory usage by creating these attachments as memoryless resources.

On Metal devices that support tile rendering, you can use imageblocks to manage transient rendering data more flexibly. For more information about imageblock memory and using it with your shader functions, see the [`Metal Shading Language Specification (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) sections 2.11, 4.5, and 5.6.

For more guidance on how to choose storage modes, see [`Setting Resource Storage Modes`](setting-resource-storage-modes.md).

## See Also

- [MTLStorageMode.shared](mtlstoragemode/shared.md)
  The CPU and GPU share access to the resource, allocated in system memory.
- [MTLStorageMode.managed](mtlstoragemode/managed.md)
  The CPU and GPU may maintain separate copies of the resource, and any changes must be explicitly synchronized.
- [MTLStorageMode.private](mtlstoragemode/private.md)
  The resource is only available to the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstoragemode/memoryless)*