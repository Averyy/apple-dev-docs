# predictions(from:)

**Framework**: Create ML  
**Kind**: method

Generates an array of hand pose predictions for each image in a URL array.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func predictions(from images: [URL]) throws -> [[(label: String, confidence: Double)]]
```

#### Return Value

An array of a prediction tuple arrays.

#### Discussion

Each prediction consists of an array of tuples that pair a classification label with the model’s confidence for that label. The method returns an array of prediction arrays, where each element of the outer array is the prediction for the corresponding URL element in `images`.

## Parameters

- `images`: An array of image file URLs.

## See Also

- [func prediction(from: URL) throws -> [(label: String, confidence: Double)]](mlhandposeclassifier/prediction(from:).md)
  Generates a hand pose prediction for an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/predictions(from:))*