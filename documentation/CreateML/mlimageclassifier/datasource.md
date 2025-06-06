# MLImageClassifier.DataSource

**Framework**: Create ML  
**Kind**: enum

A data source for an image classifier.

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

## Mentions

- [Creating an Image Classifier Model](creating-an-image-classifier-model.md)

#### Overview

Use a data source to provide training or testing data to an image classifier.

To train a model programmatically with an [`MLImageClassifier`](mlimageclassifier.md) instance, initialize a data source with the URL of the directory that contains the data. Use either [`MLImageClassifier.DataSource.labeledDirectories(at:)`](mlimageclassifier/datasource/labeleddirectories(at:).md) or [`MLImageClassifier.DataSource.labeledFiles(at:)`](mlimageclassifier/datasource/labeledfiles(at:).md) to do this, depending on whether your images are grouped by directory or by file name. See the respective creation methods for details about how to arrange your image files in each case.

When you train a model using `MLImageClassifierBuilder`, you don’t initialize a data source directly. Instead, you drag the directory containing your data from a Finder window into the live view. The builder automatically chooses the correct kind of data source based on how your images are arranged inside that directory, looking for either labeled directories or labeled files.

## Topics

### Creating a data source
- [MLImageClassifier.DataSource.labeledDirectories(at:)](mlimageclassifier/datasource/labeleddirectories(at:).md)
  An image classifier data source that uses the directory structure to label images.
- [MLImageClassifier.DataSource.labeledFiles(at:)](mlimageclassifier/datasource/labeledfiles(at:).md)
  An image classifier data source that uses file names to label images.
### Retrieving the data
- [func labeledImages() throws -> [String : [URL]]](mlimageclassifier/datasource/labeledimages.md)
  Returns the labeled images represented by the data source.
- [MLImageClassifier.DataSource.filesByLabel(_:)](mlimageclassifier/datasource/filesbylabel(_:).md)
  Dictionary of labels to file URLs.
### Splitting the data
- [func stratifiedSplit(proportions: [Double], seed: Int) throws -> [[String : [URL]]]](mlimageclassifier/datasource/stratifiedsplit(proportions:seed:).md)
  Generates an array of labeled image dictionaries by splitting the data source into strata.
- [func stratifiedSplit<RNG>(proportions: [Double], generator: inout RNG) throws -> [[String : [URL]]]](mlimageclassifier/datasource/stratifiedsplit(proportions:generator:).md)
  Generates an array of labeled image dictionaries by splitting the data source into strata using the random-number generator.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [MLImageClassifier.ModelParameters](mlimageclassifier/modelparameters-swift.struct.md)
  Parameters that affect the process of training an image classifier model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/datasource)*