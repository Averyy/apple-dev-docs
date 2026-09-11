# blockFactors

**Framework**: Metal  
**Kind**: property

An extents instance that represents the number of data plane elements which correspond to one element in a plane you create with this descriptor.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@NSCopying
var blockFactors: MTLTensorExtents { get set }
```

#### Discussion

The number of dimensions in the extents needs to match the number of the tensor’s dimensions.

The first element of the block factors needs to be `32`. All remaining elements need to be `1`.

The default value is a 1D block size of width `32`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorauxiliaryplanedescriptor/blockfactors)*