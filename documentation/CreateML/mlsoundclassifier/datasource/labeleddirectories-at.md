# MLSoundClassifier.DataSource.labeledDirectories(at:)

**Framework**: Create ML  
**Kind**: case

Creates a data source from a folder with subfolders that each contain audio files.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case labeledDirectories(at: URL)
```

#### Discussion

This data source uses each subdirectory’s name as the label for the audio files contained within them. For example, for a directory that contains a `Laughter` subdirectory, the data source applies the label `"Laughter"` to each audio file in that subdirectory.

```swift
// Build a URL to the directory that contains the labeled directories.
let home = FileManager.default.homeDirectoryForCurrentUser
let documents = home.appendingPathComponent("Documents")
let labeledDirectories = documents.appendingPathComponent("Labeled Audio Directories")

// Labeled Audio Directories/
// ├── Laughter/
// │ ├── Laughter1.m4a
// │ ├── 20190229164259.m4a
// │ ├── .
// │ ├── .
// │ ├── .
// │ └── AudienceLaughing.mp3
// └── Applause
//   ├── misc-clapping.mp3
//   ├── 20190229164211.m4a
//   ├── .
//   ├── .
//   ├── .
//   └── AudienceClapping.m4a

// Create a data source from the labeled directories.
let soundDataSource = MLSoundClassifier.DataSource.labeledDirectories(at: labeledDirectories)

// Train a sound classifier with the data source.
let soundClassifier = try MLSoundClassifier(trainingData: soundDataSource)
```

## Parameters

- `at`: URL : The URL to a folder in the file system that contains folders of audio files. The data source   uses the name of each folder as the classification label for the audio content it contains.

## See Also

- [MLSoundClassifier.DataSource.labeledFiles(at:)](mlsoundclassifier/datasource/labeledfiles(at:).md)
  Creates a data source from a folder that contains audio files, each named after the sound they represent.
- [MLSoundClassifier.DataSource.filesByLabel(_:)](mlsoundclassifier/datasource/filesbylabel(_:).md)
  Creates a data source from a dictionary.
- [case features(table: MLDataTable, featureColumn: String, labelColumn: String, parameters: MLSoundClassifier.FeatureExtractionParameters)](mlsoundclassifier/datasource/features(table:featurecolumn:labelcolumn:parameters:).md)
  Creates a data source from a data table of audio features.
- [case featuresDataFrame(DataFrame, featureColumn: String, labelColumn: String, parameters: MLSoundClassifier.FeatureExtractionParameters)](mlsoundclassifier/datasource/featuresdataframe(_:featurecolumn:labelcolumn:parameters:).md)
  Creates a data source from a data frame of audio features.
- [MLSoundClassifier.FeatureExtractionParameters](mlsoundclassifier/featureextractionparameters.md)
  Parameters that affect the process of extracting sound features from audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/labeleddirectories(at:))*