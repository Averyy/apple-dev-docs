# indexOfColumn(_:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Returns the index of a column.

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
func indexOfColumn(_ columnName: String) -> Int?
```

## Return Value

An integer if the column name or alias exists in the data frame; otherwise, `nil`.

This method’s complexity is O(*1*).

## Parameters

- `columnName`: The name or an alias of the column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/indexofcolumn(_:))*