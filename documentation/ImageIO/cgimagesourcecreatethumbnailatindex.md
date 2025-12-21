# CGImageSourceCreateThumbnailAtIndex(_:_:_:)

**Framework**: Image I/O  
**Kind**: func

Creates a thumbnail version of the image at the specified index in an image source.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGImageSourceCreateThumbnailAtIndex(_ isrc: CGImageSource, _ index: Int, _ options: CFDictionary?) -> CGImage?
```

#### Return Value

The image at the specified index, or `NULL` if an error occurs. You are responsible for releasing the returned object using [`CGImageRelease`](https://developer.apple.com/documentation/CoreGraphics/CGImageRelease).

#### Discussion

If the image source is a PDF, this function creates a 72 dpi image of the PDF page specified by the index that you pass. You must, however, pass an options dictionary that contains either the [`kCGImageSourceCreateThumbnailFromImageIfAbsent`](kcgimagesourcecreatethumbnailfromimageifabsent.md) or [`kCGImageSourceCreateThumbnailFromImageAlways`](kcgimagesourcecreatethumbnailfromimagealways.md) keys, with the value of the key set to `true`.

## Parameters

- `isrc`: The image source that contains the image data.
- `index`: The zero-based index of the image you want. If the index is invalid, this method returns  .
- `options`: A dictionary that specifies additional creation options. For a list of possible values, see  .

## See Also

- [func CGImageSourceCreateImageAtIndex(CGImageSource, Int, CFDictionary?) -> CGImage?](cgimagesourcecreateimageatindex(_:_:_:).md)
  Creates an image object from the data at the specified index in an image source.
- [func CGImageSourceGetPrimaryImageIndex(CGImageSource) -> Int](cgimagesourcegetprimaryimageindex(_:).md)
  Returns the index of the primary image for an High Efficiency Image File Format (HEIF) image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagesourcecreatethumbnailatindex(_:_:_:))*