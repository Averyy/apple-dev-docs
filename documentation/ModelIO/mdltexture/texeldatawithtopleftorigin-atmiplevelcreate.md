# texelDataWithTopLeftOrigin(atMipLevel:create:)

**Framework**: Model I/O  
**Kind**: method

Returns the texture’s image data for the specified mipmap level, organized such that its first pixel represents the top-left corner of the image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func texelDataWithTopLeftOrigin(atMipLevel level: Int, create: Bool) -> Data?
```

#### Return Value

The texture’s image data, or `nil` if data is not available.

#### Discussion

Mipmapping is a technique that uses multiple sizes of a texture image to increase rendering performance. The image for mipmap level zero matches the size in the [`dimensions`](mdltexture/dimensions.md) property. Mipmap level 1 is an image at half the original dimensions; level 2 is at quarter size; and so on.

If the texture was initialized with image data in bottom-left-origin format, the first call to this method creates and caches image data in top-left-origin format.

This method returns `nil` if the texture was not initialized with image data and is not a [`MDLTexture`](mdltexture.md) subclass capable of loading or generating its own data.

## Parameters

- `level`: The mipmap level for which to access image data.
- `create`: If   and the texture does not contain image data for the specified mipmap level (that is, the level parameter is greater than the texture’s   value) Model I/O generates image data for that mipmap level. If  , this method returns   for mipmap levels where no image data exists.

## See Also

- [func texelDataWithTopLeftOrigin() -> Data?](mdltexture/texeldatawithtopleftorigin.md)
  Returns the texture’s image data, organized such that its first pixel represents the top-left corner of the image.
- [func texelDataWithBottomLeftOrigin() -> Data?](mdltexture/texeldatawithbottomleftorigin.md)
  Returns the texture’s image data, organized such that its first pixel represents the bottom-left corner of the image.
- [func texelDataWithBottomLeftOrigin(atMipLevel: Int, create: Bool) -> Data?](mdltexture/texeldatawithbottomleftorigin(atmiplevel:create:).md)
  Returns the texture’s image data for the specified mipmap level, organized such that its first pixel represents the bottom-left corner of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexture/texeldatawithtopleftorigin(atmiplevel:create:))*