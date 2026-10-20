# MLTextClassifier.DataSource

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

A data source for a text classifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
enum DataSource
```

## Topics

### Creating a data source
- [MLTextClassifier.DataSource.labeledDirectories(at:)](./datasource/labeleddirectories%28at%29.md)
  A root directory of labeled directories for your data set.
### Retrieving the data
- [func labeledTexts() throws -> [String : [String]]](./datasource/labeledtexts%28%29.md)
  Fetches the labeled data from the data source.
- [func stratifiedSplit(proportions: [Double], seed: Int, labelColumn: String, textColumn: String) throws -> MLDataTable](./datasource/stratifiedsplit%28proportions,seed,labelcolumn,textcolumn%29.md)
  Generates a data table by splitting the data source into strata.

## See Also

### Creating and training a text classifier
- [init(trainingData:parameters:)](./init%28trainingdata,parameters%29.md)
  Creates a text classifier.
- [init(trainingData:textColumn:labelColumn:parameters:)](./init%28trainingdata,textcolumn,labelcolumn,parameters%29.md)
  Creates a text classifier.
- [MLTextClassifier.ModelParameters](./modelparameters-swift.struct.md)
  Parameters that specify model training parameters and validation data.
- [let modelParameters: MLTextClassifier.ModelParameters](./modelparameters-swift.property.md)
  The configuration parameters that the text classifier used for training during initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/datasource)*