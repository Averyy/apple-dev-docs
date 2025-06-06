# write(to:)

**Framework**: Model I/O  
**Kind**: method

Exports the texture data to an image file at the specified URL.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func write(to URL: URL) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if export succeeded; [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

Model I/O automatically infers the file format in which to export the image from the filename extension of the `url` parameter. This method can export textures in JPEG, TIFF, PNG, or (in macOS only) OpenEXR format.

## Parameters

- `URL`: The file URL at which to write the texture image.

## See Also

- [func write(to: URL, type: CFString) -> Bool](mdltexture/write(to:type:).md)
  Exports the texture data to an image file at the specified URL, of the specified type.
- [func imageFromTexture() -> Unmanaged<CGImage>?](mdltexture/imagefromtexture.md)
  Exports the texture data as a CoreGraphics image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexture/write(to:))*