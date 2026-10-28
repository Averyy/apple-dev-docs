# featureColumns

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The names of the columns you selected at initialization to train the classifier.

**Availability**:
- macOS 10.14+ - Deprecated in 14.0

## Declaration

```swift
var featureColumns: [String]
```

## Discussion

Changing the value of this property doesn’t retrain the model or affect its behavior.

## See Also

### Creating and training a support vector classifier
- [init(trainingData:targetColumn:featureColumns:parameters:)](./init%28trainingdata,targetcolumn,featurecolumns,parameters%29.md)
  Creates a support vector classifier.
- [MLSupportVectorClassifier.ModelParameters](./modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLSupportVectorClassifier.ModelParameters](./modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](./targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier/featurecolumns)*