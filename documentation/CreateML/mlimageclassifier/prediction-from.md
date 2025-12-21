# prediction(from:)

**Framework**: Create ML  
**Kind**: method

Generates a prediction for an image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func prediction(from image: CGImage) throws -> String
```

#### Return Value

A prediction label for the image.

## Parameters

- `image`: The image that you want the model to classify.

## See Also

- [func predictions(from: [URL]) throws -> [String]](mlimageclassifier/predictions(from:).md)
  Generates predictions for an array of images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/prediction(from:))*