# stratifiedSplit(proportions:seed:labelColumn:)

**Framework**: Create ML  
**Kind**: method

Generates a data table by splitting the data source into strata.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func stratifiedSplit(proportions: [Double], seed: Int = timestampSeed(), labelColumn: String) throws -> MLDataTable
```

#### Discussion

- proportions: An array of stratum proportions, each in the range `[0.0, 1.0]`. - seed: A seed number for the random-number generator.
- labelColumn: The name of the column or category the method uses to stratify the contents of the data source.

## See Also

- [func labeledMedia() throws -> [String : [URL]]](mlhandposeclassifier/datasource/labeledmedia.md)
  Generates a dictionary that contains the data source’s classification labels paired with an array of URLs to the label’s image files.
- [func imagesWithAnnotations() throws -> MLDataTable](mlhandposeclassifier/datasource/imageswithannotations.md)
  Generates a data table that contains a column for the data source’s image file URLs and a column of annotations.
- [func keypointsWithAnnotations() throws -> MLDataTable](mlhandposeclassifier/datasource/keypointswithannotations.md)
  Generates a data table that contains a column for hand joint locations and hand pose annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/datasource/stratifiedsplit(proportions:seed:labelcolumn:))*