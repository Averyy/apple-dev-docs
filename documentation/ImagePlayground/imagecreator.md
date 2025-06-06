# ImageCreator

**Framework**: Image Playground  
**Kind**: class

Generates images programmatically from the description and style information you specify.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
final class ImageCreator
```

#### Overview

Use an `ImageCreator` object to generate images programmatically from your app on devices that support the capability. You provide a description of the image content, as a text string or as a combination of text and images. The system’s generative models use that information to generate one or more images and return them to your code.

Create an `ImageCreator` object and use its [`images(for:style:limit:)`](imagecreator/images(for:style:limit:).md) method to start the image generation process. Image generation occurs asynchronously, delivering results back to your code using an [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) object.

## Topics

### Creating the object
- [init() async throws](imagecreator/init.md)
  Creates a new image creator object for you to use in your app.
### Generating images
- [func images(for: [ImagePlaygroundConcept], style: ImagePlaygroundStyle, limit: Int) -> some AsyncSequence<ImageCreator.CreatedImage, any Error>
](imagecreator/images(for:style:limit:).md)
  Starts the creation of images based on the description and style information you provide.
- [let availableStyles: [ImagePlaygroundStyle]](imagecreator/availablestyles.md)
  The set of styles you can apply to the images you create.
- [ImageCreator.CreatedImage](imagecreator/createdimage.md)
  A structure that stores a programmatically generated image.
- [ImageCreator.Error](imagecreator/error.md)
  Errors that can occur during the image generation process.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imagecreator)*