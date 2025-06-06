# imageFromTexture()

**Framework**: Model I/O  
**Kind**: method

Exports the texture data as a CoreGraphics image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func imageFromTexture() -> Unmanaged<CGImage>?
```

#### Return Value

A CoreGraphics image object containing the texture’s pixel data, or `nil` if the texture data cannot be represented using CoreGraphics.

## See Also

- [func write(to: URL) -> Bool](mdltexture/write(to:).md)
  Exports the texture data to an image file at the specified URL.
- [func write(to: URL, type: CFString) -> Bool](mdltexture/write(to:type:).md)
  Exports the texture data to an image file at the specified URL, of the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexture/imagefromtexture())*