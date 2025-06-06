# MLSoundClassifier.DataSource.labeledFiles(at:)

**Framework**: Create ML  
**Kind**: case

Creates a data source from a folder that contains audio files, each named after the sound they represent.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case labeledFiles(at: URL)
```

#### Discussion

Create a sound classifier data source from a directory of audio files with the `labeledFiles` case. You must name each file with a sound classification label, followed by a period and an arbitrary string, ending with the file extension. For example, you can name a sound classifier’s training files as `Laughter.3.png`, `Applause.1.jpg`, `Applause.2.jpg`, and so on.

In this example, these audio file names give a sound classifier at least two class labels:

- `Laughter`
- `Applause`

## Parameters

- `at`: URL: The URL to a folder in the file system that contains audio files. The data source uses the   first component of each audio file’s name as its classification label.

## See Also

- [MLSoundClassifier.DataSource.labeledDirectories(at:)](mlsoundclassifier/datasource/labeleddirectories(at:).md)
  Creates a data source from a folder with subfolders that each contain audio files.
- [MLSoundClassifier.DataSource.filesByLabel(_:)](mlsoundclassifier/datasource/filesbylabel(_:).md)
  Creates a data source from a dictionary.
- [case features(table: MLDataTable, featureColumn: String, labelColumn: String, parameters: MLSoundClassifier.FeatureExtractionParameters)](mlsoundclassifier/datasource/features(table:featurecolumn:labelcolumn:parameters:).md)
  Creates a data source from a data table of audio features.
- [case featuresDataFrame(DataFrame, featureColumn: String, labelColumn: String, parameters: MLSoundClassifier.FeatureExtractionParameters)](mlsoundclassifier/datasource/featuresdataframe(_:featurecolumn:labelcolumn:parameters:).md)
  Creates a data source from a data frame of audio features.
- [MLSoundClassifier.FeatureExtractionParameters](mlsoundclassifier/featureextractionparameters.md)
  Parameters that affect the process of extracting sound features from audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeledfiles(at:))*