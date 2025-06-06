# stratifiedSplit(proportions:seed:labelColumn:textColumn:)

**Framework**: Create ML  
**Kind**: method

Generates a data table by splitting the data source into strata.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func stratifiedSplit(proportions: [Double], seed: Int = timestampSeed(), labelColumn: String, textColumn: String) throws -> MLDataTable
```

#### Return Value

A new data table.

## Parameters

- `proportions`: An array of proportions, each in the range  .
- `seed`: A seed number for the random-number generator. The default value is the current epoch time in milliseconds.
- `labelColumn`: The name of the column with the labels.
- `textColumn`: The name of the column with the text data.

## See Also

- [func labeledTexts() throws -> [String : [String]]](mltextclassifier/datasource/labeledtexts.md)
  Fetches the labeled data from the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/datasource/stratifiedsplit(proportions:seed:labelcolumn:textcolumn:))*