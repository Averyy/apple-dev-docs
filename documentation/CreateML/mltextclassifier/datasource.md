# MLTextClassifier.DataSource

**Framework**: Create ML  
**Kind**: enum

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
- [MLTextClassifier.DataSource.labeledDirectories(at:)](mltextclassifier/datasource/labeleddirectories(at:).md)
  A root directory of labeled directories for your data set.
### Retrieving the data
- [func labeledTexts() throws -> [String : [String]]](mltextclassifier/datasource/labeledtexts.md)
  Fetches the labeled data from the data source.
- [func stratifiedSplit(proportions: [Double], seed: Int, labelColumn: String, textColumn: String) throws -> MLDataTable](mltextclassifier/datasource/stratifiedsplit(proportions:seed:labelcolumn:textcolumn:).md)
  Generates a data table by splitting the data source into strata.

## See Also

- [init(trainingData:parameters:)](mltextclassifier/init(trainingdata:parameters:).md)
  Creates a text classifier.
- [init(trainingData:textColumn:labelColumn:parameters:)](mltextclassifier/init(trainingdata:textcolumn:labelcolumn:parameters:).md)
  Creates a text classifier.
- [MLTextClassifier.ModelParameters](mltextclassifier/modelparameters-swift.struct.md)
  Parameters that specify model training parameters and validation data.
- [let modelParameters: MLTextClassifier.ModelParameters](mltextclassifier/modelparameters-swift.property.md)
  The configuration parameters that the text classifier used for training during initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/datasource)*