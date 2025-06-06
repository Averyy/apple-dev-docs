# LSMMapWriteToStream(_:_:_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func

Writes information about a map or text to a stream in text form.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func LSMMapWriteToStream(_ mapref: LSMMap, _ textref: LSMText?, _ stream: CFWriteStream, _ options: CFOptionFlags) -> OSStatus
```

## See Also

- [func LSMMapCreateFromURL(CFAllocator?, CFURL, CFOptionFlags) -> Unmanaged<LSMMap>?](lsmmapcreatefromurl(_:_:_:).md)
  Loads a map from the specified file.
- [func LSMMapWriteToURL(LSMMap, CFURL, CFOptionFlags) -> OSStatus](lsmmapwritetourl(_:_:_:).md)
  Compiles the map, if necessary, and stores it into the specified file.
- [Storage Flags](storage-flags.md)
  Options for loading and saving a map to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmmapwritetostream(_:_:_:_:))*