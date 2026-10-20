# destinationLevel

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The index of the mipmap level in the destination texture.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var destinationLevel: Int
```

```c
NSUInteger destinationLevel;
```

#### Discussion

Provide a value between `0` and the destination texture’s [`firstMipmapInTail`](../mtltexture/firstmipmapintail.md).

When [`sourceLevel`](./sourcelevel.md) is equal to the source texture’s [`firstMipmapInTail`](../mtltexture/firstmipmapintail.md), set [`destinationLevel`](./destinationlevel.md) to the destination texture’s [`firstMipmapInTail`](../mtltexture/firstmipmapintail.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4copysparsetexturemappingoperation/destinationlevel)*