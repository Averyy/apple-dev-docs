# MLSoundClassifier.DataSource.featuresDataFrame(_:featureColumn:labelColumn:parameters:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

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

## Discussion

Use [`extractFeatures(trainingData:parameters:sessionParameters:)`](../extractfeatures%28trainingdata,parameters,sessionparameters%29.md) to create a [`DataFrame`](../../../TabularData/dataframe.md) of audio features.

## Parameters

- `dataFrame`: A data frame that contains labeled audio data.
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
- [case features(table: MLDataTable, featureColumn: String, labelColumn: String, parameters: MLSoundClassifier.FeatureExtractionParameters)](./features%28table,featurecolumn,labelcolumn,parameters%29.md)
  Creates a data source from a data table of audio features.
- [MLSoundClassifier.FeatureExtractionParameters](../featureextractionparameters.md)
  Parameters that affect the process of extracting sound features from audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/featuresdataframe(_:featurecolumn:labelcolumn:parameters:))*