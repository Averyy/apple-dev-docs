# MLSoundClassifier.DataSource.features(table:featureColumn:labelColumn:parameters:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

Creates a data source from a data table of audio features.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0
- iPadOS 15.0+ - Deprecated in 17.0
- Mac Catalyst 15.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- visionOS 1.0+

## Declaration

```swift
case features(table: MLDataTable, featureColumn: String = __Defaults.featureColumnName, labelColumn: String = __Defaults.labelColumnName, parameters: MLSoundClassifier.FeatureExtractionParameters = FeatureExtractionParameters())
```

## Discussion

Use [`extractFeatures(trainingData:parameters:sessionParameters:)`](../extractfeatures%28trainingdata,parameters,sessionparameters%29.md) to create an [`MLDataTable`](../../mldatatable.md) of audio features.

## Parameters

- `table`: An [`MLDataTable`](../../mldatatable.md) instance that contains labeled audio data.
- `featureColumn`: The name of the column that contains the audio features.
- `labelColumn`: The name of the column that contains the audio labels.
- `parameters`: An [`MLSoundClassifier.FeatureExtractionParameters`](../featureextractionparameters.md) instance you use to configure the feature-extraction phase.

## See Also

### Creating a data source
- [MLSoundClassifier.DataSource.labeledDirectories(at:)](./labeleddirectories%28at%29.md)
  Creates a data source from a folder with subfolders that each contain audio files.
- [MLSoundClassifier.DataSource.labeledFiles(at:)](./labeledfiles%28at%29.md)
  Creates a data source from a folder that contains audio files, each named after the sound they represent.
- [MLSoundClassifier.DataSource.filesByLabel(_:)](./filesbylabel%28_%29.md)
  Creates a data source from a dictionary.
- [case featuresDataFrame(DataFrame, featureColumn: String, labelColumn: String, parameters: MLSoundClassifier.FeatureExtractionParameters)](./featuresdataframe%28_,featurecolumn,labelcolumn,parameters%29.md)
  Creates a data source from a data frame of audio features.
- [MLSoundClassifier.FeatureExtractionParameters](../featureextractionparameters.md)
  Parameters that affect the process of extracting sound features from audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/features(table:featurecolumn:labelcolumn:parameters:))*