# prediction(from:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

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

**Other overloads**:

```swift
func prediction(from image: URL) throws -> String
```

## Return Value

A prediction label for the image.

## Parameters

- `image`: The image that you want the model to classify.

## See Also

### Testing an image classifier
- [func predictions(from: [URL]) throws -> [String]](./predictions%28from%29.md)
  Generates predictions for an array of images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/prediction(from:))*