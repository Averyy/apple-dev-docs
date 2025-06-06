# availableStyles

**Framework**: Image Playground  
**Kind**: property

The set of styles you can apply to the images you create.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
final let availableStyles: [ImagePlaygroundStyle]
```

#### Discussion

Before requesting any images, make sure the style you want to use is in this property.

## See Also

- [func images(for: [ImagePlaygroundConcept], style: ImagePlaygroundStyle, limit: Int) -> some AsyncSequence<ImageCreator.CreatedImage, any Error>
](imagecreator/images(for:style:limit:).md)
  Starts the creation of images based on the description and style information you provide.
- [ImageCreator.CreatedImage](imagecreator/createdimage.md)
  A structure that stores a programmatically generated image.
- [ImageCreator.Error](imagecreator/error.md)
  Errors that can occur during the image generation process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imagecreator/availablestyles)*