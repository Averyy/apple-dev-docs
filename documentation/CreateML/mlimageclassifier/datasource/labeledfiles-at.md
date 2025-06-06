# MLImageClassifier.DataSource.labeledFiles(at:)

**Framework**: Create ML  
**Kind**: case

An image classifier data source that uses file names to label images.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
case labeledFiles(at: URL)
```

#### Discussion

Use this case to create a data source based on a files on disk that contain your training images. The associated value is a URL that represents a directory containing files with names based on each image’s associated label. The image’s label is taken as the part of the file name up to the first period.

For example, you can initialize a data source with a file URL that indicates a directory called `Training Data` that contains the files `buffalo.1.jpg`, `buffalo.2.jpg`, `cheetah.1.jpg`, and `cheetah.2.jpg`. The first two images receive the label `buffalo`, while the second two images receive the label `cheetah`. The part of the name after the first period can be any arbitrary string.

![Diagram showing a directory called “Training Data” containing images with names that use the label in the](https://docs-assets.developer.apple.com/published/4d24317d8a456b920217ba8bbd8d149a/MLImageClassifier-DataSource-labeledFiles%28at%3A%29-1%402x.png)

If you want to create a data source with labels based on how you sort your images into directories, use [`MLImageClassifier.DataSource.labeledDirectories(at:)`](mlimageclassifier/datasource/labeleddirectories(at:).md) instead.

## See Also

- [MLImageClassifier.DataSource.labeledDirectories(at:)](mlimageclassifier/datasource/labeleddirectories(at:).md)
  An image classifier data source that uses the directory structure to label images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/datasource/labeledfiles(at:))*