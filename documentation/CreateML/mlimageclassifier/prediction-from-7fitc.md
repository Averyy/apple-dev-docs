# prediction(from:)

**Framework**: Create ML  
**Kind**: method

Generates a prediction for an image at the URL.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func prediction(from image: URL) throws -> String
```

#### Return Value

A prediction label for the image.

## Parameters

- `image`: The URL of the image you want the model to classify.

## See Also

- [func prediction(from: CGImage) throws -> String](mlimageclassifier/prediction(from:)-97cll.md)
  Generates a prediction for an image.
- [func predictions(from: [URL]) throws -> [String]](mlimageclassifier/predictions(from:).md)
  Generates predictions for an array of images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/prediction(from:)-7fitc)*