# MTLAutoreleasedArgument

**Framework**: Metal  
**Kind**: typealias  
**Role**: Type Alias

A convenience type alias for an autoreleased argument instance.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.11+ - Deprecated in 13.0
- tvOS - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`MTLBinding`](./mtlbinding.md) instead, and cast it to specific binding type, such as [`MTLTextureBinding`](./mtltexturebinding.md), [`MTLBufferBinding`](./mtlbufferbinding.md), and so on.

## Declaration

```swift
typealias MTLAutoreleasedArgument = MTLArgument
```

```c
typedef MTLArgument * MTLAutoreleasedArgument;
```

## See Also

### Function arguments
- [class MTLAttribute](./mtlattribute.md)
  An object that describes an attribute defined in the stage-in argument for a shader.
- [class MTLVertexAttribute](./mtlvertexattribute.md)
  An instance that represents an attribute of a vertex function.
- [class MTLArgument](./mtlargument.md)
  Information about an argument of a graphics or compute function.
- [enum MTLArgumentType](./mtlargumenttype.md)
  The resource type for an argument of a function.
- [typealias MTLArgumentAccess](./mtlargumentaccess.md)
  Function access restrictions to argument data in the shading language code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlautoreleasedargument)*