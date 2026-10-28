# labeledTexts()

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Fetches the labeled data from the data source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func labeledTexts() throws -> [String : [String]]
```

## Return Value

A dictionary that contains each label with their related text entries.

## See Also

### Retrieving the data
- [func stratifiedSplit(proportions: [Double], seed: Int, labelColumn: String, textColumn: String) throws -> MLDataTable](./stratifiedsplit%28proportions,seed,labelcolumn,textcolumn%29.md)
  Generates a data table by splitting the data source into strata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/datasource/labeledtexts())*