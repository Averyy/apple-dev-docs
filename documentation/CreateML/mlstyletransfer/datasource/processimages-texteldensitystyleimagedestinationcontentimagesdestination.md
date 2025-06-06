# processImages(textelDensity:styleImageDestination:contentImagesDestination:)

**Framework**: Create ML  
**Kind**: method

Converts the content images to square images and saves them to a destination directory.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func processImages(textelDensity: Int, styleImageDestination: URL? = nil, contentImagesDestination: URL? = nil) throws -> (processedStyleImage: URL, processedContentImages: URL)
```

#### Return Value

A tuple of two URLs:

#### Discussion

- textelDensity: The length of a side, in pixels, of the destination image. The value must be a multiple of `4` in the range `[64, 1024]`.
- styleImageDestination: A location in the file system to save the converted style image to. If `nil`, Create ML saves the image to a temporary file location.
- contentImagesDestination: A location in the file system to save the converted content image to. If `nil`, Create ML saves the image to a temporary file location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/datasource/processimages(texteldensity:styleimagedestination:contentimagesdestination:))*