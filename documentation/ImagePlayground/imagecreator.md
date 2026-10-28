# ImageCreator

**Framework**: Image Playground  
**Kind**: class  
**Role**: Class

Generates images programmatically from the description and style information you specify.

**Availability**:
- iOS 18.4+ - Deprecated in 27.0
- iPadOS 18.4+ - Deprecated in 27.0
- Mac Catalyst 18.4+ - Deprecated in 27.0
- macOS 15.4+ - Deprecated in 27.0
- visionOS 2.4+ - Deprecated in 27.0

> **Deprecated**: Use ImagePlaygroundViewController or imagePlaygroundSheet.

## Declaration

```swift
final class ImageCreator
```

## Overview

Use an `ImageCreator` object to generate images programmatically from your app on devices that support the capability. You provide a description of the image content, as a text string or as a combination of text and images. The system’s generative models use that information to generate one or more images and return them to your code.

Create an `ImageCreator` object and use its [`images(for:style:limit:)`](./imagecreator/images%28for,style,limit%29.md) method to start the image generation process. Image generation occurs asynchronously, delivering results back to your code using an [`AsyncSequence`](../Swift/asyncsequence.md) object.

## Topics

### Creating the object
- [init() async throws](./imagecreator/init%28%29.md)
  Creates a new image creator object for you to use in your app.
### Generating images
- [func images(for: [ImagePlaygroundConcept], style: ImagePlaygroundStyle, limit: Int) -> some AsyncSequence<ImageCreator.CreatedImage, any Error>
](./imagecreator/images%28for,style,limit%29.md)
  Starts the creation of images based on the description and style information you provide.
- [let availableStyles: [ImagePlaygroundStyle]](./imagecreator/availablestyles.md)
  The set of styles you can apply to the images you create.
- [ImageCreator.CreatedImage](./imagecreator/createdimage.md)
  A structure that stores a programmatically generated image.
- [ImageCreator.Error](./imagecreator/error.md)
  Errors that can occur during the image generation process.
### Instance Methods
- [func images(for: [ImagePlaygroundConcept], style: ImagePlaygroundStyle, options: ImagePlaygroundOptions, limit: Int) -> some AsyncSequence<ImageCreator.CreatedImage, any Error>
](./imagecreator/images%28for,style,options,limit%29.md)
  Creates one or more images from the provided description and style information and returns the results asynchronously.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imagecreator)*