# synchronize(resource:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that synchronizes the CPU’s copy of a managed resource, such as a buffer or texture, so that it matches the GPU’s copy.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.11+

## Declaration

```swift
func synchronize(resource: any MTLResource)
```

## Mentions

- [Synchronizing a Managed Resource in macOS](synchronizing-a-managed-resource-in-macos.md)

#### Discussion

This method ensures the CPU can correctly read all the changes a GPU makes to a resource that uses the managed storage mode. For the resources you create with [`MTLStorageMode.managed`](mtlstoragemode/managed.md), the CPU and GPU each have a copy of that resource. As the GPU modifies its copy, the CPU’s copy remains unchanged until you synchronize with a command, such as this one.

The CPU can access the updated content from its copy of the resources after the synchronization command completes.

> **Note**:  You can encode a command that selectively synchronizes parts of an [`MTLTexture`](mtltexture.md) by calling the [`synchronize(texture:slice:level:)`](mtlblitcommandencoder/synchronize(texture:slice:level:).md) method.

## Parameters

- `resource`: An   instance — such as an   or   — with a   property that’s equal to  .

## See Also

- [func synchronize(texture: any MTLTexture, slice: Int, level: Int)](mtlblitcommandencoder/synchronize(texture:slice:level:).md)
  Encodes a command that synchronizes a part of the CPU’s copy of a texture so that it matches the GPU’s copy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/synchronize(resource:))*