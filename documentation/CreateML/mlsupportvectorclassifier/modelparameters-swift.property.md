# modelParameters

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The underlying parameters used when training the model.

**Availability**:
- macOS 10.14+ - Deprecated in 14.0

## Declaration

```swift
let modelParameters: MLSupportVectorClassifier.ModelParameters
```

## See Also

### Creating and training a support vector classifier
- [init(trainingData:targetColumn:featureColumns:parameters:)](./init%28trainingdata,targetcolumn,featurecolumns,parameters%29.md)
  Creates a support vector classifier.
- [MLSupportVectorClassifier.ModelParameters](./modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [var targetColumn: String](./targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](./featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier/modelparameters-swift.property)*