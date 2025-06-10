# sourceImage

**Framework**: Image Playground  
**Kind**: property

An image to use as source input for generating the new image.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@objc @preconcurrency var sourceImage: UIImage? { get set }
```

#### Discussion

If you have an existing image that you want to use as a starting point for the new image, add it to this property. If you don’t supply a source image, the system creates the new image from the prompt text you provide.

Typically, you provide an image big enough to fit the device’s display. The expected minimum size is 384 x 384 pixels, and the recommended maximum size is 4096 x 4096 pixels.

## See Also

- [var concepts: [ImagePlaygroundConcept]](imageplaygroundviewcontroller/concepts.md)
  An array of elements that describes the expected contents of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller/sourceimage)*