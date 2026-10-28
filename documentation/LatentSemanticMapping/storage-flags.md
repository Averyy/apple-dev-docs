# Storage Flags

**Framework**: Latent Semantic Mapping  
**Role**: API Collection

Options for loading and saving a map to a file.

## Overview

Specify these options for [`LSMMapCreateFromURL(_:_:_:)`](./lsmmapcreatefromurl%28_,_,_%29.md) and [`LSMMapWriteToURL(_:_:_:)`](./lsmmapwritetourl%28_,_,_%29.md).

## Topics

### Constants
- [var kLSMMapDiscardCounts: Int](./klsmmapdiscardcounts.md)
  An option that specifies not to keep counts.
- [var kLSMMapLoadMutable: Int](./klsmmaploadmutable.md)
  An option that specifies to load the map as mutable in training state.
- [var kLSMMapHashText: Int](./klsmmaphashtext.md)
  An option that specifies to transform the text so it’s not human-readable.

## See Also

### Loading and Saving a Map
- [func LSMMapCreateFromURL(CFAllocator?, CFURL, CFOptionFlags) -> Unmanaged<LSMMap>?](./lsmmapcreatefromurl%28_,_,_%29.md)
  Loads a map from the specified file.
- [func LSMMapWriteToURL(LSMMap, CFURL, CFOptionFlags) -> OSStatus](./lsmmapwritetourl%28_,_,_%29.md)
  Compiles the map, if necessary, and stores it into the specified file.
- [func LSMMapWriteToStream(LSMMap, LSMText?, CFWriteStream, CFOptionFlags) -> OSStatus](./lsmmapwritetostream%28_,_,_,_%29.md)
  Writes information about a map or text to a stream in text form.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/storage-flags)*