# MTLArgumentAccess

**Framework**: Metal  
**Kind**: typealias  
**Role**: Type Alias

Function access restrictions to argument data in the shading language code.

**Availability**:
- iOS 8.0+ - Deprecated in 17.0 (renamed: MTLBindingAccess)
- iPadOS 8.0+ - Deprecated in 17.0 (renamed: MTLBindingAccess)
- Mac Catalyst 13.1+ - Deprecated in 17.0 (renamed: MTLBindingAccess)
- macOS 10.11+ - Deprecated in 14.0 (renamed: MTLBindingAccess)
- tvOS - Deprecated in 17.0 (renamed: MTLBindingAccess)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: MTLBindingAccess)

## Declaration

```swift
typealias MTLArgumentAccess = MTLBindingAccess
```

```c
typedef MTLBindingAccess MTLArgumentAccess;
```

## Topics

### Specifying access options
- [MTLArgumentAccessReadOnly](./mtlbindingaccess/mtlargumentaccessreadonly.md)
  The function can only read its argument data.
- [MTLArgumentAccessWriteOnly](./mtlbindingaccess/mtlargumentaccesswriteonly.md)
  The function can only write its argument data.
- [MTLArgumentAccessReadWrite](./mtlbindingaccess/mtlargumentaccessreadwrite.md)
  The function can either read or write its argument data.

## See Also

### Function arguments
- [class MTLAttribute](./mtlattribute.md)
  An object that describes an attribute defined in the stage-in argument for a shader.
- [class MTLVertexAttribute](./mtlvertexattribute.md)
  An instance that represents an attribute of a vertex function.
- [class MTLArgument](./mtlargument.md)
  Information about an argument of a graphics or compute function.
- [typealias MTLAutoreleasedArgument](./mtlautoreleasedargument.md)
  A convenience type alias for an autoreleased argument instance.
- [enum MTLArgumentType](./mtlargumenttype.md)
  The resource type for an argument of a function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentaccess)*