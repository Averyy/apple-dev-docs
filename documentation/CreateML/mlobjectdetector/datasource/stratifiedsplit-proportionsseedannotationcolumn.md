# stratifiedSplit(proportions:seed:annotationColumn:)

**Framework**: Create ML  
**Kind**: method

Generates a new data table by splitting the data source using the specified proportions.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func stratifiedSplit(proportions: [Double], seed: Int = timestampSeed(), annotationColumn: String) throws -> MLDataTable
```

#### Return Value

An [`MLDataTable`](mldatatable.md) containing the data source’s split contents.

## Parameters

- `proportions`: An array of doubles, each representing a portion of the data source. If these values don’t   add up to  , the method normalizes the numbers so that they do.
- `seed`: The value the method uses to initialize the random-number generator, which affects how the method   splits the data.
- `annotationColumn`: The name of the column the method uses to split the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/datasource/stratifiedsplit(proportions:seed:annotationcolumn:))*