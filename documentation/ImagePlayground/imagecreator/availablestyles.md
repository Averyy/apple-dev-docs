# availableStyles

**Framework**: Image Playground  
**Kind**: property  
**Role**: Instance Property

The set of styles you can apply to the images you create.

**Availability**:
- iOS 18.4+ - Deprecated in 27.0
- iPadOS 18.4+ - Deprecated in 27.0
- Mac Catalyst 18.4+ - Deprecated in 27.0
- macOS 15.4+ - Deprecated in 27.0
- visionOS 2.4+ - Deprecated in 27.0

## Declaration

```swift
final let availableStyles: [ImagePlaygroundStyle]
```

#### Discussion

Before requesting any images, make sure the style you want to use is in this property.

## See Also

### Generating images
- [func images(for: [ImagePlaygroundConcept], style: ImagePlaygroundStyle, limit: Int) -> some AsyncSequence<ImageCreator.CreatedImage, any Error>
](./images%28for,style,limit%29.md)
  Starts the creation of images based on the description and style information you provide.
- [ImageCreator.CreatedImage](./createdimage.md)
  A structure that stores a programmatically generated image.
- [ImageCreator.Error](./error.md)
  Errors that can occur during the image generation process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imagecreator/availablestyles)*