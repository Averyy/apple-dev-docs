# featureColumns

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

Changing the value of this property doesn’t retrain the model or affect its behavior.

## See Also

### Training a linear regressor synchronously
- [init(trainingData:targetColumn:featureColumns:parameters:)](./init%28trainingdata,targetcolumn,featurecolumns,parameters%29.md)
  Creates a linear regressor.
- [var targetColumn: String](./targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllinearregressor/featurecolumns)*