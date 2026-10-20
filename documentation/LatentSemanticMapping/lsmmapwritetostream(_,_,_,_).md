# LSMMapWriteToStream(_:_:_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func  
**Role**: Function

Writes information about a map or text to a stream in text form.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func LSMMapWriteToStream(_ mapref: LSMMap, _ textref: LSMText?, _ stream: CFWriteStream, _ options: CFOptionFlags) -> OSStatus
```

```c
OSStatus LSMMapWriteToStream(LSMMapRef mapref, LSMTextRef textref, CFWriteStreamRef stream, CFOptionFlags options);
```

## See Also

### Loading and Saving a Map
- [func LSMMapCreateFromURL(CFAllocator?, CFURL, CFOptionFlags) -> Unmanaged<LSMMap>?](./lsmmapcreatefromurl%28_,_,_%29.md)
  Loads a map from the specified file.
- [func LSMMapWriteToURL(LSMMap, CFURL, CFOptionFlags) -> OSStatus](./lsmmapwritetourl%28_,_,_%29.md)
  Compiles the map, if necessary, and stores it into the specified file.
- [Storage Flags](./storage-flags.md)
  Options for loading and saving a map to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmmapwritetostream(_:_:_:_:))*