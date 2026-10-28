# prediction(from:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

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

## Return Value

An array of prediction tuples.

## Discussion

Each prediction consists of an array of tuples that pair a classification label with the model’s confidence in that label.

## Parameters

- `image`: An image file URL.

## See Also

### Testing a hand pose classifier
- [func predictions(from: [URL]) throws -> [[(label: String, confidence: Double)]]](./predictions%28from%29.md)
  Generates an array of hand pose predictions for each image in a URL array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/prediction(from:))*