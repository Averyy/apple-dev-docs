# creationVariety

**Framework**: Image Playground  
**Kind**: property

The amount to vary the creation parameters when generating multiple images from the same inputs.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
var creationVariety: ImagePlaygroundOptions.CreationVariety
```

#### Discussion

When creating multiple images from the same inputs, the system adjusts parameters programmatically to create images with different content. Use this property to specify the amount of variability you want in the final images. For example, specify [`ImagePlaygroundOptions.CreationVariety.high`](imageplaygroundoptions/creationvariety-swift.enum/high.md) to generate images with greater numbers of differences, or specify [`ImagePlaygroundOptions.CreationVariety.low`](imageplaygroundoptions/creationvariety-swift.enum/low.md) to generate images that are closer together.

The default value of this property is [`ImagePlaygroundOptions.CreationVariety.automatic`](imageplaygroundoptions/creationvariety-swift.enum/automatic.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundoptions/creationvariety-swift.property)*