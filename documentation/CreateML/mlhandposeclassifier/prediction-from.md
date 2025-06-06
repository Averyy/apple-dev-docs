# prediction(from:)

**Framework**: Create ML  
**Kind**: method

Generates a hand pose prediction for an image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func prediction(from image: URL) throws -> [(label: String, confidence: Double)]
```

#### Return Value

An array of prediction tuples.

#### Discussion

Each prediction consists of an array of tuples that pair a classification label with the model’s confidence in that label.

## See Also

- [func predictions(from: [URL]) throws -> [[(label: String, confidence: Double)]]](mlhandposeclassifier/predictions(from:).md)
  Generates an array of hand pose predictions for each image in a URL array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/prediction(from:))*