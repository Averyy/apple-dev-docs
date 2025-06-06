# labeledMedia()

**Framework**: Create ML  
**Kind**: method

Generates a dictionary that contains the data source’s classification labels paired with an array of URLs to the label’s image files.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func labeledMedia() throws -> [String : [URL]]
```

## See Also

- [func imagesWithAnnotations() throws -> MLDataTable](mlhandposeclassifier/datasource/imageswithannotations.md)
  Generates a data table that contains a column for the data source’s image file URLs and a column of annotations.
- [func keypointsWithAnnotations() throws -> MLDataTable](mlhandposeclassifier/datasource/keypointswithannotations.md)
  Generates a data table that contains a column for hand joint locations and hand pose annotations.
- [func stratifiedSplit(proportions: [Double], seed: Int, labelColumn: String) throws -> MLDataTable](mlhandposeclassifier/datasource/stratifiedsplit(proportions:seed:labelcolumn:).md)
  Generates a data table by splitting the data source into strata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/datasource/labeledmedia())*