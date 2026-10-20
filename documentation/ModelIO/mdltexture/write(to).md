# write(to:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) writeToURL:(NSURL *) URL;
```

#### Return Value

[`true`](../../Swift/true.md) if export succeeded; [`false`](../../Swift/false.md) otherwise.

#### Discussion

Model I/O automatically infers the file format in which to export the image from the filename extension of the `url` parameter. This method can export textures in JPEG, TIFF, PNG, or (in macOS only) OpenEXR format.

## Parameters

- `URL`: The file URL at which to write the texture image.

## See Also

### Exporting Textures
- [func write(to: URL, type: CFString) -> Bool](./write%28to,type%29.md)
  Exports the texture data to an image file at the specified URL, of the specified type.
- [func imageFromTexture() -> Unmanaged<CGImage>?](./imagefromtexture%28%29.md)
  Exports the texture data as a CoreGraphics image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexture/write(to:))*