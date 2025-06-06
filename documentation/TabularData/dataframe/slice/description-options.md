# description(options:)

**Framework**: TabularData  
**Kind**: method

Generates a text representation of the data frame type.

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
func description(options: FormattingOptions) -> String
```

#### Discussion

`FormattingOptions.maximumLineWidth` needs to be wide enough to print at least the index column, the truncation column, and one data column (at least two characters, one for initial of the content, and one for “…”).

## Parameters

- `options`: A set of formatting options that affect the description string,   including the maximum width of a column and the maximum number of rows.

## See Also

- [var description: String](dataframe/slice/description.md)
  A text representation of the data frame slice.
- [var debugDescription: String](dataframe/slice/debugdescription.md)
  A text representation of the data frame slice suitable for debugging.
- [var customMirror: Mirror](dataframe/slice/custommirror.md)
  A mirror that reflects the data frame slice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/slice/description(options:))*