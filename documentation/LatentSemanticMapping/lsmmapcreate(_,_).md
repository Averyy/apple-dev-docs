# LSMMapCreate(_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func  
**Role**: Function

Creates a new Latent Semantic Mapping map.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func LSMMapCreate(_ alloc: CFAllocator?, _ flags: CFOptionFlags) -> Unmanaged<LSMMap>
```

```c
LSMMapRefLSMMapCreate(CFAllocatorRef alloc, CFOptionFlags flags);
```

## Discussion

Call [`CFRelease`](../CoreFoundation/cfrelease.md) to dispose of the map.

## See Also

### Creating a Map
- [Map Flags](./map-flags.md)
  Options for creating a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmmapcreate(_:_:))*