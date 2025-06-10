# init(contentsOfSFrameDirectory:columns:rows:)

**Framework**: TabularData  
**Kind**: init

Creates a data frame from a Turi Create scalable data frame.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(contentsOfSFrameDirectory url: URL, columns: [String]? = nil, rows: Range<Int>? = nil) throws
```

#### Discussion

> **Note**: An `SFrameReadingError` instance.

## Parameters

- `url`: A URL to an   directory.
- `columns`: An array of column names; Set to   to use every column in the  .
- `rows`: A range of indices; Set to   to use every row in the  .

## See Also

- [struct ShapedData](shapeddata.md)
  A collection type that represents multidimensional data in a data frame element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/init(contentsofsframedirectory:columns:rows:))*