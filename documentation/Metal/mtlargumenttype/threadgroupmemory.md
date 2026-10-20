# MTLArgumentType.threadgroupMemory

**Framework**: Metal  
**Kind**: case  
**Role**: Case

The argument is a pointer to threadgroup memory.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0 (renamed: MTLBindingType)
- iPadOS 8.0+ - Deprecated in 16.0 (renamed: MTLBindingType)
- Mac Catalyst 13.1+ - Deprecated in 16.0 (renamed: MTLBindingType)
- macOS 10.11+ - Deprecated in 13.0 (renamed: MTLBindingType)
- tvOS - Deprecated in 16.0 (renamed: MTLBindingType)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: MTLBindingType)

## Declaration

```swift
case threadgroupMemory
```

```c
MTLArgumentTypeThreadgroupMemory
```

## See Also

### Argument types
- [MTLArgumentType.buffer](./buffer.md)
  The argument is a buffer.
- [MTLArgumentType.texture](./texture.md)
  The argument is a texture.
- [MTLArgumentType.sampler](./sampler.md)
  The argument is a texture sampler.
- [MTLArgumentType.imageblock](./imageblock.md)
  The argument is an imageblock.
- [MTLArgumentType.imageblockData](./imageblockdata.md)
  The argument is imageblock data.
- [MTLArgumentType.visibleFunctionTable](./visiblefunctiontable.md)
  The argument is a visible function table.
- [MTLArgumentType.intersectionFunctionTable](./intersectionfunctiontable.md)
  The argument is an intersection function table.
- [MTLArgumentType.primitiveAccelerationStructure](./primitiveaccelerationstructure.md)
  The argument is a bottom-level ray tracing acceleraton structure for a set of primitives.
- [MTLArgumentType.instanceAccelerationStructure](./instanceaccelerationstructure.md)
  The argument is a top-level ray tracing acceleration structure for a set of instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumenttype/threadgroupmemory)*