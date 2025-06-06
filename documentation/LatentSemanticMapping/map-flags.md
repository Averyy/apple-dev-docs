# Map Flags

**Framework**: Latent Semantic Mapping

Options for creating a map.

#### Overview

Specify these options for [`LSMMapCreate(_:_:)`](lsmmapcreate(_:_:).md). These options can improve mapping accuracy, but may result in a potentially significant increase in memory use.

## Topics

### Constants
- [var kLSMMapPairs: Int](klsmmappairs.md)
  An option that specifies to use pairs in addition to single words.
- [var kLSMMapTriplets: Int](klsmmaptriplets.md)
  An option that specifies to use triplets and pairs in addition to single words.
- [var kLSMMapHashText: Int](klsmmaphashtext.md)
  An option that specifies to transform the text so it’s not human-readable.

## See Also

- [func LSMMapCreate(CFAllocator?, CFOptionFlags) -> Unmanaged<LSMMap>](lsmmapcreate(_:_:).md)
  Creates a new Latent Semantic Mapping map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/map-flags)*