# init(columnSelection:concatenatedColumnName:)

**Framework**: Create ML Components  
**Kind**: init

Creates a concatenator that concatenates numeric columns into a new column of ML shaped array.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
init(columnSelection: ColumnSelection = .all, concatenatedColumnName: String = "features")
```

## Parameters

- `columnSelection`: A selection of columns to concatenate.
- `concatenatedColumnName`: The name of the resulting shaped array column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/columnconcatenator/init(columnselection:concatenatedcolumnname:))*