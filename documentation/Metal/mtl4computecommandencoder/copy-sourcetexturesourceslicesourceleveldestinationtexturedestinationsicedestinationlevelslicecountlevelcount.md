# copy(sourceTexture:sourceSlice:sourceLevel:destinationTexture:destinationSice:destinationLevel:sliceCount:levelCount:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that copies slices of a texture to slices of another texture.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func copy(sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, destinationTexture: any MTLTexture, destinationSice destinationSlice: Int, destinationLevel: Int, sliceCount: Int, levelCount: Int)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourcetexture:sourceslice:sourcelevel:destinationtexture:destinationsice:destinationlevel:slicecount:levelcount:))*