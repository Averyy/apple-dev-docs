# LSMMapCreate(_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func

Creates a new Latent Semantic Mapping map.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func LSMMapCreate(_ alloc: CFAllocator?, _ flags: CFOptionFlags) -> Unmanaged<LSMMap>
```

#### Discussion

Call [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) to dispose of the map.

## See Also

- [Map Flags](map-flags.md)
  Options for creating a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmmapcreate(_:_:))*