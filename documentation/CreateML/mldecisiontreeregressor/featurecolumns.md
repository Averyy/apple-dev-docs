# featureColumns

**Framework**: Create ML  
**Kind**: property

The names of the columns you selected at initialization to train the regressor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var featureColumns: [String]
```

#### Discussion

Changing the value of this property doesn’t retrain the model or affect its behavior.

## See Also

- [init(trainingData:targetColumn:featureColumns:parameters:)](mldecisiontreeregressor/init(trainingdata:targetcolumn:featurecolumns:parameters:).md)
  Creates a decision tree regressor.
- [var targetColumn: String](mldecisiontreeregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeregressor/featurecolumns)*