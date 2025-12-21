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

- `sourceTexture`: A   texture that the command copies data from. To read the source   texture contents, you need to set its   property   to   prior to drawing into it.
- `sourceSlice`: A slice within   the command uses as a starting point to copy   data from. Set this to   if   isn’t a texture array or a   cube texture.
- `sourceLevel`: A mipmap level within  .
- `destinationTexture`: Another   the command copies the data to that has the same    and   as  .   To write the contents into this texture, you need to set its    property to  .
- `destinationSlice`: A slice within   the command uses as its starting point   for copying data to. Set this to   if   isn’t a texture   array or a cube texture.
- `destinationLevel`: A mipmap level within  . The mipmap level you reference needs to   have the same size as the   slice’s mipmap at  .
- `sliceCount`: The number of slices the command copies so that it satisfies the conditions   that the sum of   and   doesn’t exceed the number of   slices in   and the sum of   and    doesn’t exceed the number of slices in  .
- `levelCount`: The number of mipmap levels the command copies so that it satisfies the   conditions that the sum of   and   doesn’t exceed the   number of mipmap levels in   and the sum of    and   doesn’t exceed the number of mipmap levels in  .

## See Also

- [func copy(sourceTensor: any MTLTensor, sourceOrigin: MTLTensorExtents, sourceDimensions: MTLTensorExtents, destinationTensor: any MTLTensor, destinationOrigin: MTLTensorExtents, destinationDimensions: MTLTensorExtents)](mtl4computecommandencoder/copy(sourcetensor:sourceorigin:sourcedimensions:destinationtensor:destinationorigin:destinationdimensions:).md)
  Encodes a command to copy data from a tensor instance into another.
- [func copy(sourceTexture: any MTLTexture, destinationTexture: any MTLTexture)](mtl4computecommandencoder/copy(sourcetexture:destinationtexture:).md)
  Encodes a command that copies data from a texture to another.
- [func copy(sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)](mtl4computecommandencoder/copy(sourcetexture:sourceslice:sourcelevel:sourceorigin:sourcesize:destinationtexture:destinationslice:destinationlevel:destinationorigin:).md)
  Encodes a command that copies image data from a slice of a texture into a slice of another texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourcetexture:sourceslice:sourcelevel:destinationtexture:destinationslice:destinationlevel:slicecount:levelcount:))*