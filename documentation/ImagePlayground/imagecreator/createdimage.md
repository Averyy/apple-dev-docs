# ImageCreator.CreatedImage

**Framework**: Image Playground  
**Kind**: struct  
**Role**: Structure

A structure that stores a programmatically generated image.

**Availability**:
- iOS 18.4+ - Deprecated in 27.0
- iPadOS 18.4+ - Deprecated in 27.0
- Mac Catalyst 18.4+ - Deprecated in 27.0
- macOS 15.4+ - Deprecated in 27.0
- visionOS 2.4+ - Deprecated in 27.0

## Declaration

```swift
struct CreatedImage
```

#### Overview

You receive `CreatedImage` structures from an `ImageCreator` object when you ask that object to generate images for you. You cannot create instances of this structure yourself.

## Topics

### Getting the image
- [let cgImage: CGImage](./createdimage/cgimage.md)
  The programmatically generated image.

## See Also

### Generating images
- [func images(for: [ImagePlaygroundConcept], style: ImagePlaygroundStyle, limit: Int) -> some AsyncSequence<ImageCreator.CreatedImage, any Error>
](./images%28for,style,limit%29.md)
  Starts the creation of images based on the description and style information you provide.
- [let availableStyles: [ImagePlaygroundStyle]](./availablestyles.md)
  The set of styles you can apply to the images you create.
- [ImageCreator.Error](./error.md)
  Errors that can occur during the image generation process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imagecreator/createdimage)*