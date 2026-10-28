# MLSoundClassifier.DataSource

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

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

## Overview

Use a data source to represent a dataset for training, validating, or testing a sound classifier.

## Topics

### Creating a data source
- [MLSoundClassifier.DataSource.labeledDirectories(at:)](./datasource/labeleddirectories%28at%29.md)
  Creates a data source from a folder with subfolders that each contain audio files.
- [MLSoundClassifier.DataSource.labeledFiles(at:)](./datasource/labeledfiles%28at%29.md)
  Creates a data source from a folder that contains audio files, each named after the sound they represent.
- [MLSoundClassifier.DataSource.filesByLabel(_:)](./datasource/filesbylabel%28_%29.md)
  Creates a data source from a dictionary.
- [case features(table: MLDataTable, featureColumn: String, labelColumn: String, parameters: MLSoundClassifier.FeatureExtractionParameters)](./datasource/features%28table,featurecolumn,labelcolumn,parameters%29.md)
  Creates a data source from a data table of audio features.
- [case featuresDataFrame(DataFrame, featureColumn: String, labelColumn: String, parameters: MLSoundClassifier.FeatureExtractionParameters)](./datasource/featuresdataframe%28_,featurecolumn,labelcolumn,parameters%29.md)
  Creates a data source from a data frame of audio features.
- [MLSoundClassifier.FeatureExtractionParameters](./featureextractionparameters.md)
  Parameters that affect the process of extracting sound features from audio files.
### Retrieving the data
- [func labeledSounds() throws -> [String : [URL]]](./datasource/labeledsounds%28%29.md)
  Generates a dictionary of the data source’s labeled audio files.
### Partitioning the data
- [func stratifiedSplit(proportions: [Double], seed: Int) throws -> [[String : [URL]]]](./datasource/stratifiedsplit%28proportions,seed%29.md)
  Generates an array of labeled audio dictionaries by splitting the data source into strata.
- [func stratifiedSplit<RNG>(proportions: [Double], generator: inout RNG) throws -> [[String : [URL]]]](./datasource/stratifiedsplit%28proportions,generator%29.md)
  Generates an array of labeled audio dictionaries by splitting the data source into strata using the random-number generator.

## See Also

### Supporting types
- [MLSoundClassifier.ModelParameters](./modelparameters-swift.struct.md)
  Parameters that affect the process of training a sound-classifier model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource)*