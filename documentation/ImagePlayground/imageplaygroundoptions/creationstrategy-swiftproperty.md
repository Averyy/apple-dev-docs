# creationStrategy

**Framework**: Image Playground  
**Kind**: property

The options that specify how to interpret the content in the provided input image.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var creationStrategy: ImagePlaygroundOptions.CreationStrategy
```

#### Discussion

If one of the inputs to the image generation process is an image, this property determines how the system uses that image to generate new images. You can specify an image programmatically, but people can also select images from the system interface. Creation strategies include generating new images that closely resemble the original or using the original only for inspiration.

The default value of this property is [`ImagePlaygroundOptions.CreationStrategy.automatic`](imageplaygroundoptions/creationstrategy-swift.enum/automatic.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundoptions/creationstrategy-swift.property)*