# blockFactors

**Framework**: Metal  
**Kind**: property

A [`MTLTensorExtents`](mtltensorextents.md) instance that describes how many data plane elements correspond to one element in this plane.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@NSCopying
var blockFactors: MTLTensorExtents { get set }
```

#### Discussion

The rank of the block factors must match the rank of the tensor’s dimensions.

The first element of the block factors must be 32. All remaining elements must be 1.

The default value is a 1D block size of width 32.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorauxiliaryplanedescriptor/blockfactors)*