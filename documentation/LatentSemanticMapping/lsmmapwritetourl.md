# LSMMapWriteToURL(_:_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func

Compiles the map, if necessary, and stores it into the specified file.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func LSMMapWriteToURL(_ mapref: LSMMap, _ file: CFURL, _ flags: CFOptionFlags) -> OSStatus
```

## See Also

- [func LSMMapCreateFromURL(CFAllocator?, CFURL, CFOptionFlags) -> Unmanaged<LSMMap>?](lsmmapcreatefromurl(_:_:_:).md)
  Loads a map from the specified file.
- [func LSMMapWriteToStream(LSMMap, LSMText?, CFWriteStream, CFOptionFlags) -> OSStatus](lsmmapwritetostream(_:_:_:_:).md)
  Writes information about a map or text to a stream in text form.
- [Storage Flags](storage-flags.md)
  Options for loading and saving a map to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmmapwritetourl(_:_:_:))*