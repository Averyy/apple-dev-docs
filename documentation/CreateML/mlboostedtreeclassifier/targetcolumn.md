# targetColumn

**Framework**: Create ML  
**Kind**: property

The name of the column you selected at initialization to define which categories the classifier predicts.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var targetColumn: String
```

#### Discussion

Changing the value of this property doesn’t retrain the model or affect its behavior.

## See Also

- [init(trainingData:targetColumn:featureColumns:parameters:)](mlboostedtreeclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:).md)
  Creates a boosted tree classifier.
- [var featureColumns: [String]](mlboostedtreeclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeclassifier/targetcolumn)*