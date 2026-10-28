# synchronize(texture:slice:level:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a command that synchronizes a part of the CPU’s copy of a texture so that it matches the GPU’s copy.

**Availability**:
- Mac Catalyst 13.0+ - Deprecated in 27.0
- macOS 10.11+ - Deprecated in 27.0

> **Deprecated**: Managed storage has no effect on Apple Silicon, use Shared storage instead

## Declaration

```swift
func synchronize(texture: any MTLTexture, slice: Int, level: Int)
```

```objc
- (void) synchronizeTexture:(id<MTLTexture>) texture slice:(NSUInteger) slice level:(NSUInteger) level;
```

## Mentions

- [Synchronizing a managed resource in macOS](../synchronizing-a-managed-resource-in-macos.md)

## Discussion

This method ensures the CPU can correctly read the changes a GPU makes to a slice of a texture that uses the managed storage mode. For the resources you create with [`MTLStorageMode.managed`](../mtlstoragemode/managed.md), the CPU and GPU each have a copy of that resource. As the GPU modifies its copy, the CPU’s copy remains unchanged until you synchronize with a command, such as this one.

The CPU can access the updated content from its copy of the texture after the synchronization command completes.

> **Note**:  The command this method encodes behaves similarly to the command that [`synchronize(resource:)`](./synchronize%28resource%29.md) encodes, except that it flushes only the applicable slice and mipmap level.

## Parameters

- `texture`: An [`MTLTexture`](../mtltexture.md) instance with a [`storageMode`](../mtlresource/storagemode.md) property that’s equal to [`MTLStorageMode.managed`](../mtlstoragemode/managed.md).
- `slice`: A slice within `texture`.
- `level`: A mipmap level within `texture`.

## See Also

### Synchronizing managed resources
- [func synchronize(resource: any MTLResource)](./synchronize%28resource%29.md)
  Encodes a command that synchronizes the CPU’s copy of a managed resource, such as a buffer or texture, so that it matches the GPU’s copy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/synchronize(texture:slice:level:))*