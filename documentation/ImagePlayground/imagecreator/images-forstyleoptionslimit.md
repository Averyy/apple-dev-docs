# images(for:style:options:limit:)

**Framework**: Image Playground  
**Kind**: method

Starts the creation of images based on the description and style information you provide.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
final func images(for concepts: [ImagePlaygroundConcept], style: ImagePlaygroundStyle, options: ImagePlaygroundOptions, limit: Int) -> some AsyncSequence<ImageCreator.CreatedImage, any Error>
```

#### Return Value

An asynchronous stream you use to receive the images.

#### Discussion

Call this method to start the image generation process with the specified parameters. The method executes asynchronously and returns the images on the provided [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) object. The following example configures an image creator, starts the creation of the images, and processes the generated images as they arrive.

```swift
do {
    let creator = try await ImageCreator()
    guard let style = creator.availableStyles.first else { return }
    var options = ImagePlaygroundOptions()
    options.creationVariety = .high
    options.personalization = .enabled

    let images = creator.images(
        for: [.text("A cat wearing mittens.")]
        style: style,
        options: options,
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
- `options`: A set of options influencing image creation.
- `limit`: The maximum number of images you want the system to create. The system limits the maximum number of images to 4.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imagecreator/images(for:style:options:limit:))*