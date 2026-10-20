# init(maximumLineWidth:maximumCellWidth:maximumRowCount:includesColumnTypes:)

**Framework**: TabularData  
**Kind**: init

Creates a formatting options instance.

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
init(maximumLineWidth: Int, maximumCellWidth: Int = 50, maximumRowCount: Int = 20, includesColumnTypes: Bool = true)
```

## Parameters

- `maximumLineWidth`: The largest number of characters a description can generate per line.
- `maximumCellWidth`: The largest number of characters a description can generate per cell.
- `maximumRowCount`: The largest number of rows a description can generate.
- `includesColumnTypes`: A Boolean that indicates whether the description prints a column’s type.

## See Also

- [init()](formattingoptions/init.md)
  Creates a formatting options instance with default parameters.
- [init(locale: Locale)](formattingoptions/init(locale:).md)
  Creates a formatting options instance with a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/formattingoptions/init(maximumlinewidth:maximumcellwidth:maximumrowcount:includescolumntypes:))*