# labeledImages()

**Framework**: Create ML  
**Kind**: method

Returns the labeled images represented by the data source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func labeledImages() throws -> [String : [URL]]
```

#### Return Value

The labeled images that the data source represents, as a dictionary. The dictionary keys are the labels, while the dictionary values are arrays of images, represented as URLs, that correspond to the label.

## See Also

- [MLImageClassifier.DataSource.filesByLabel(_:)](mlimageclassifier/datasource/filesbylabel(_:).md)
  Dictionary of labels to file URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/datasource/labeledimages())*