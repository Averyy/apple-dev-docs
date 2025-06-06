# synchronize(texture:slice:level:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that synchronizes a part of the CPU’s copy of a texture so that it matches the GPU’s copy.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.11+

## Declaration

```swift
func synchronize(texture: any MTLTexture, slice: Int, level: Int)
```

## Mentions

- [Synchronizing a Managed Resource in macOS](synchronizing-a-managed-resource-in-macos.md)

#### Discussion

This method ensures the CPU can correctly read the changes a GPU makes to a slice of a texture that uses the managed storage mode. For the resources you create with [`MTLStorageMode.managed`](mtlstoragemode/managed.md), the CPU and GPU each have a copy of that resource. As the GPU modifies its copy, the CPU’s copy remains unchanged until you synchronize with a command, such as this one.

The CPU can access the updated content from its copy of the texture after the synchronization command completes.

> **Note**:  The command this method encodes behaves similarly to the command that [`synchronize(resource:)`](mtlblitcommandencoder/synchronize(resource:).md) encodes, except that it flushes only the applicable slice and mipmap level.

 The command this method encodes behaves similarly to the command that [`synchronize(resource:)`](mtlblitcommandencoder/synchronize(resource:).md) encodes, except that it flushes only the applicable slice and mipmap level.

## Parameters

- `texture`: An   instance with a   property that’s equal to  .
- `slice`: A slice within  .
- `level`: A mipmap level within  .

## See Also

- [func synchronize(resource: any MTLResource)](mtlblitcommandencoder/synchronize(resource:).md)
  Encodes a command that synchronizes the CPU’s copy of a managed resource, such as a buffer or texture, so that it matches the GPU’s copy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/synchronize(texture:slice:level:))*