# texelDataWithBottomLeftOrigin()

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

Returns the texture’s image data, organized such that its first pixel represents the bottom-left corner of the image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func texelDataWithBottomLeftOrigin() -> Data?
```

```objc
- (NSData *) texelDataWithBottomLeftOrigin;
```

## Return Value

The texture’s image data, or `nil` if data is not available.

## Discussion

If the texture was initialized with image data in top-left-origin format, the first call to this method creates and caches image data in bottom-left-origin format.

This method returns `nil` if the texture was not initialized with image data and is not a [`MDLTexture`](../mdltexture.md) subclass capable of loading or generating its own data.

## See Also

### Accessing Texture Data
- [func texelDataWithTopLeftOrigin() -> Data?](./texeldatawithtopleftorigin%28%29.md)
  Returns the texture’s image data, organized such that its first pixel represents the top-left corner of the image.
- [func texelDataWithTopLeftOrigin(atMipLevel: Int, create: Bool) -> Data?](./texeldatawithtopleftorigin%28atmiplevel,create%29.md)
  Returns the texture’s image data for the specified mipmap level, organized such that its first pixel represents the top-left corner of the image.
- [func texelDataWithBottomLeftOrigin(atMipLevel: Int, create: Bool) -> Data?](./texeldatawithbottomleftorigin%28atmiplevel,create%29.md)
  Returns the texture’s image data for the specified mipmap level, organized such that its first pixel represents the bottom-left corner of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexture/texeldatawithbottomleftorigin())*