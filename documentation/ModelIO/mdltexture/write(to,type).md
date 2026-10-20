# write(to:type:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

Exports the texture data to an image file at the specified URL, of the specified type.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func write(to nsurl: URL, type: CFString) -> Bool
```

```objc
- (BOOL) writeToURL:(NSURL *) nsurl type:(CFStringRef) type;
```

#### Return Value

[`true`](../../Swift/true.md) if export succeeded; [`false`](../../Swift/false.md) otherwise.

#### Discussion

For the `type` parameter, pass the Uniform Type Identifier for any output format supported by the Image I/O framework, such as the JPEG, TIFF, PNG, or (in macOS only) OpenEXR format. For details, see [Uniform Type Identifiers Reference](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/UTIRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009257).

## Parameters

- `nsurl`: The file URL at which to write the texture image.
- `type`: A Uniform Type Identifier declaring the image file format to use for export.

## See Also

### Exporting Textures
- [func write(to: URL) -> Bool](./write%28to%29.md)
  Exports the texture data to an image file at the specified URL.
- [func imageFromTexture() -> Unmanaged<CGImage>?](./imagefromtexture%28%29.md)
  Exports the texture data as a CoreGraphics image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexture/write(to:type:))*