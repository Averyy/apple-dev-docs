# ImageCreator.CreatedImage

**Framework**: Image Playground  
**Kind**: struct

A structure that stores a programmatically generated image.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
struct CreatedImage
```

#### Overview

You receive `CreatedImage` structures from an `ImageCreator` object when you ask that object to generate images for you. You cannot create instances of this structure yourself.

## Topics

### Getting the image
- [let cgImage: CGImage](imagecreator/createdimage/cgimage.md)
  The programmatically generated image.

## See Also

- [func images(for: [ImagePlaygroundConcept], style: ImagePlaygroundStyle, limit: Int) -> some AsyncSequence<ImageCreator.CreatedImage, any Error>
](imagecreator/images(for:style:limit:).md)
  Starts the creation of images based on the description and style information you provide.
- [let availableStyles: [ImagePlaygroundStyle]](imagecreator/availablestyles.md)
  The set of styles you can apply to the images you create.
- [ImageCreator.Error](imagecreator/error.md)
  Errors that can occur during the image generation process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imagecreator/createdimage)*