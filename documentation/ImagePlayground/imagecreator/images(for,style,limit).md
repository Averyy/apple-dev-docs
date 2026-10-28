# images(for:style:limit:)

**Framework**: Image Playground  
**Kind**: method  
**Role**: Instance Method

Starts the creation of images based on the description and style information you provide.

**Availability**:
- iOS 18.4+ - Deprecated in 27.0
- iPadOS 18.4+ - Deprecated in 27.0
- Mac Catalyst 18.4+ - Deprecated in 27.0
- macOS 15.4+ - Deprecated in 27.0
- visionOS 2.4+ - Deprecated in 27.0

## Declaration

```swift
final func images(for concepts: [ImagePlaygroundConcept], style: ImagePlaygroundStyle, limit: Int) -> some AsyncSequence<ImageCreator.CreatedImage, any Error>
```

## Return Value

An asynchronous stream you use to receive the images.

## Discussion

Call this method to start the image generation process with the specified parameters. The method executes asynchronously and returns the images on the provided [`AsyncSequence`](../../Swift/asyncsequence.md) object. The following example configures an image creator, starts the creation of the images, and processes the generated images as they arrive.

```swift
do {
    let creator = try await ImageCreator()
    guard let style = creator.availableStyles.first else { return }

    let images = creator.images(
        for: [.text("A cat wearing mittens.")]
        style: style,
        limit: 4)

    // Receive the images.
    for try await image in images {
        let anImage = image.cgImage

        // Do something with the image.
    }
}
catch ImageCreator.Error.notSupported {
    print(“Image creation not supported on the current device.”)
}
```

## Parameters

- `concepts`: The elements that describe the expected contents of the image.
- `style`: The style you want the model to apply to the output image. It is a programmer error to specify a style that’s not in the `availableStyles` property.
- `limit`: The maximum number of images you want the system to create. The system limits the maximum number of images to 4.

## See Also

### Generating images
- [let availableStyles: [ImagePlaygroundStyle]](./availablestyles.md)
  The set of styles you can apply to the images you create.
- [ImageCreator.CreatedImage](./createdimage.md)
  A structure that stores a programmatically generated image.
- [ImageCreator.Error](./error.md)
  Errors that can occur during the image generation process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imagecreator/images(for:style:limit:))*