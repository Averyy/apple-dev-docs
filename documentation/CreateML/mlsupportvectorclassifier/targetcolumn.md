# targetColumn

**Framework**: Create ML  
**Kind**: property

The name of the column you selected at initialization to define which categories the classifier predicts.

**Availability**:
- macOS 10.14+

## Declaration

```swift
var targetColumn: String
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
- [var featureColumns: [String]](mlsupportvectorclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier/targetcolumn)*