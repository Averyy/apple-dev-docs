# copy(sourceTexture:sourceSlice:sourceLevel:destinationTexture:destinationSlice:destinationLevel:sliceCount:levelCount:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that copies slices of a texture to slices of another texture.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func copy(sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, sliceCount: Int, levelCount: Int)
```

## Parameters

- `sourceTexture`: A [`MTLTexture`](mtltexture.md) texture that the command copies data from. To read the source texture contents, you need to set its [`isFramebufferOnly`](mtltexture/isframebufferonly.md) property to [`false`](https://developer.apple.com/documentation/swift/false) prior to drawing into it.
- `sourceSlice`: A slice within `sourceTexture` the command uses as a starting point to copy data from. Set this to `0` if `sourceTexture` isn’t a texture array or a cube texture.
- `sourceLevel`: A mipmap level within `sourceTexture`.
- `destinationTexture`: Another [`MTLTexture`](mtltexture.md) the command copies the data to that has the same [`pixelFormat`](mtltexture/pixelformat.md) and [`sampleCount`](mtltexture/samplecount.md) as `sourceTexture`. To write the contents into this texture, you need to set its [`isFramebufferOnly`](mtltexture/isframebufferonly.md) property to [`false`](https://developer.apple.com/documentation/swift/false).
- `destinationSlice`: A slice within `destinationTexture` the command uses as its starting point for copying data to. Set this to `0` if `destinationTexture` isn’t a texture array or a cube texture.
- `destinationLevel`: A mipmap level within `destinationTexture`. The mipmap level you reference needs to have the same size as the `sourceTexture` slice’s mipmap at `sourceLevel`.
- `sliceCount`: The number of slices the command copies so that it satisfies the conditions that the sum of `sourceSlice` and `sliceCount` doesn’t exceed the number of slices in `sourceTexture` and the sum of `destinationSlice` and `sliceCount` doesn’t exceed the number of slices in `destinationTexture`.
- `levelCount`: The number of mipmap levels the command copies so that it satisfies the conditions that the sum of `sourceLevel` and `levelCount` doesn’t exceed the number of mipmap levels in `sourceTexture` and the sum of `destinationLevel` and `levelCount` doesn’t exceed the number of mipmap levels in `destinationTexture`.

## See Also

- [func copy(sourceTensor: any MTLTensor, sourceOrigin: MTLTensorExtents, sourceDimensions: MTLTensorExtents, destinationTensor: any MTLTensor, destinationOrigin: MTLTensorExtents, destinationDimensions: MTLTensorExtents)](mtl4computecommandencoder/copy(sourcetensor:sourceorigin:sourcedimensions:destinationtensor:destinationorigin:destinationdimensions:).md)
  Encodes a command to copy data from a slice of the data plane of a tensor into a slice of the data plane of another tensor.
- [func copy(sourceTexture: any MTLTexture, destinationTexture: any MTLTexture)](mtl4computecommandencoder/copy(sourcetexture:destinationtexture:).md)
  Encodes a command that copies data from a texture to another.
- [func copy(sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)](mtl4computecommandencoder/copy(sourcetexture:sourceslice:sourcelevel:sourceorigin:sourcesize:destinationtexture:destinationslice:destinationlevel:destinationorigin:).md)
  Encodes a command that copies image data from a slice of a texture into a slice of another texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourcetexture:sourceslice:sourcelevel:destinationtexture:destinationslice:destinationlevel:slicecount:levelcount:))*