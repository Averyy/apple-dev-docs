# featureColumns

**Framework**: Create ML  
**Kind**: property

The names of the columns you selected at initialization to train the classifier.

**Availability**:
- macOS 10.14+

## Declaration

```swift
var featureColumns: [String]
```

#### Discussion

Changing the value of this property doesn’t retrain the model or affect its behavior.

## See Also

- [init(trainingData:targetColumn:featureColumns:parameters:)](mlsupportvectorclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:).md)
  Creates a support vector classifier.
- [MLSupportVectorClassifier.ModelParameters](mlsupportvectorclassifier/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLSupportVectorClassifier.ModelParameters](mlsupportvectorclassifier/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mlsupportvectorclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier/featurecolumns)*