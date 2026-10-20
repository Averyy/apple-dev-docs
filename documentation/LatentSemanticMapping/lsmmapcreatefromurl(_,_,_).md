# LSMMapCreateFromURL(_:_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func  
**Role**: Function

Loads a map from the specified file.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func LSMMapCreateFromURL(_ alloc: CFAllocator?, _ file: CFURL, _ flags: CFOptionFlags) -> Unmanaged<LSMMap>?
```

```c
LSMMapRefLSMMapCreateFromURL(CFAllocatorRef alloc, CFURLRef file, CFOptionFlags flags);
```

## See Also

### Loading and Saving a Map
- [func LSMMapWriteToURL(LSMMap, CFURL, CFOptionFlags) -> OSStatus](./lsmmapwritetourl%28_,_,_%29.md)
  Compiles the map, if necessary, and stores it into the specified file.
- [func LSMMapWriteToStream(LSMMap, LSMText?, CFWriteStream, CFOptionFlags) -> OSStatus](./lsmmapwritetostream%28_,_,_,_%29.md)
  Writes information about a map or text to a stream in text form.
- [Storage Flags](./storage-flags.md)
  Options for loading and saving a map to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmmapcreatefromurl(_:_:_:))*