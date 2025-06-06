# Storage Flags

**Framework**: Latent Semantic Mapping

Options for loading and saving a map to a file.

#### Overview

Specify these options for [`LSMMapCreateFromURL(_:_:_:)`](lsmmapcreatefromurl(_:_:_:).md) and [`LSMMapWriteToURL(_:_:_:)`](lsmmapwritetourl(_:_:_:).md).

## Topics

### Constants
- [var kLSMMapDiscardCounts: Int](klsmmapdiscardcounts.md)
  An option that specifies not to keep counts.
- [var kLSMMapLoadMutable: Int](klsmmaploadmutable.md)
  An option that specifies to load the map as mutable in training state.
- [var kLSMMapHashText: Int](klsmmaphashtext.md)
  An option that specifies to transform the text so it’s not human-readable.

## See Also

- [func LSMMapCreateFromURL(CFAllocator?, CFURL, CFOptionFlags) -> Unmanaged<LSMMap>?](lsmmapcreatefromurl(_:_:_:).md)
  Loads a map from the specified file.
- [func LSMMapWriteToURL(LSMMap, CFURL, CFOptionFlags) -> OSStatus](lsmmapwritetourl(_:_:_:).md)
  Compiles the map, if necessary, and stores it into the specified file.
- [func LSMMapWriteToStream(LSMMap, LSMText?, CFWriteStream, CFOptionFlags) -> OSStatus](lsmmapwritetostream(_:_:_:_:).md)
  Writes information about a map or text to a stream in text form.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/storage-flags)*