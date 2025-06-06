# MLSoundClassifier.DataSource

**Framework**: Create ML  
**Kind**: enum

A representation of a sound-classifier dataset located in the file system or in a data table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
enum DataSource
```

#### Overview

Use a data source to represent a dataset for training, validating, or testing a sound classifier.

## Topics

### Creating a data source
- [MLSoundClassifier.DataSource.labeledDirectories(at:)](mlsoundclassifier/datasource/labeleddirectories(at:).md)
  Creates a data source from a folder with subfolders that each contain audio files.
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
### Retrieving the data
- [func labeledSounds() throws -> [String : [URL]]](mlsoundclassifier/datasource/labeledsounds.md)
  Generates a dictionary of the data source’s labeled audio files.
### Partitioning the data
- [func stratifiedSplit(proportions: [Double], seed: Int) throws -> [[String : [URL]]]](mlsoundclassifier/datasource/stratifiedsplit(proportions:seed:).md)
  Generates an array of labeled audio dictionaries by splitting the data source into strata.
- [func stratifiedSplit<RNG>(proportions: [Double], generator: inout RNG) throws -> [[String : [URL]]]](mlsoundclassifier/datasource/stratifiedsplit(proportions:generator:).md)
  Generates an array of labeled audio dictionaries by splitting the data source into strata using the random-number generator.

## See Also

- [MLSoundClassifier.ModelParameters](mlsoundclassifier/modelparameters-swift.struct.md)
  Parameters that affect the process of training a sound-classifier model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource)*