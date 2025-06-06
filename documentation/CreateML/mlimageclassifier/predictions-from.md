# predictions(from:)

**Framework**: Create ML  
**Kind**: method

Generates predictions for an array of images.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func predictions(from images: [URL]) throws -> [String]
```

#### Return Value

An array of prediction labels for the images. Each label’s index corresponds to the image’s index in the input array.

## Parameters

- `images`: An array of images you want the model to classify.

## See Also

- [func prediction(from: CGImage) throws -> String](mlimageclassifier/prediction(from:)-97cll.md)
  Generates a prediction for an image.
- [func prediction(from: URL) throws -> String](mlimageclassifier/prediction(from:)-7fitc.md)
  Generates a prediction for an image at the URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/predictions(from:))*