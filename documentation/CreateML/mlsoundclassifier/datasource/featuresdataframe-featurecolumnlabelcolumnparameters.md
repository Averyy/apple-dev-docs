# MLSoundClassifier.DataSource.featuresDataFrame(_:featureColumn:labelColumn:parameters:)

**Framework**: Create ML  
**Kind**: case

Creates a data source from a data frame of audio features.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
case featuresDataFrame(DataFrame, featureColumn: String = __Defaults.featureColumnName, labelColumn: String = __Defaults.labelColumnName, parameters: MLSoundClassifier.FeatureExtractionParameters = FeatureExtractionParameters())
```

#### Discussion

Use [`extractFeatures(trainingData:parameters:sessionParameters:)`](mlsoundclassifier/extractfeatures(trainingdata:parameters:sessionparameters:).md) to create a [`DataFrame`](https://developer.apple.com/documentation/TabularData/DataFrame) of audio features.

## Parameters

- `dataFrame`: A data frame that contains labeled audio data.
- `featureColumn`: The name of the column that contains the audio features.
- `labelColumn`: The name of the column that contains the audio labels.
- `parameters`: An   instance you use to configure the   feature-extraction phase.

## See Also

- [MLSoundClassifier.DataSource.labeledDirectories(at:)](mlsoundclassifier/datasource/labeleddirectories(at:).md)
  Creates a data source from a folder with subfolders that each contain audio files.
- [MLSoundClassifier.DataSource.labeledFiles(at:)](mlsoundclassifier/datasource/labeledfiles(at:).md)
  Creates a data source from a folder that contains audio files, each named after the sound they represent.
- [MLSoundClassifier.DataSource.filesByLabel(_:)](mlsoundclassifier/datasource/filesbylabel(_:).md)
  Creates a data source from a dictionary.
- [case features(table: MLDataTable, featureColumn: String, labelColumn: String, parameters: MLSoundClassifier.FeatureExtractionParameters)](mlsoundclassifier/datasource/features(table:featurecolumn:labelcolumn:parameters:).md)
  Creates a data source from a data table of audio features.
- [MLSoundClassifier.FeatureExtractionParameters](mlsoundclassifier/featureextractionparameters.md)
  Parameters that affect the process of extracting sound features from audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/featuresdataframe(_:featurecolumn:labelcolumn:parameters:))*