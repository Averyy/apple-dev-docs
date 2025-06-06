# frame(ofInsideOfColumn:)

**Framework**: AppKit  
**Kind**: method

Returns the rectangle containing the specified column, not including borders.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func frame(ofInsideOfColumn column: Int) -> NSRect
```

#### Return Value

The rectangle containing the column, not including the column borders.

## Parameters

- `column`: The index of the column for which to retrieve the inside frame.

## See Also

- [func frame(ofColumn: Int) -> NSRect](nsbrowser/frame(ofcolumn:).md)
  Returns the rectangle containing the given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/frame(ofinsideofcolumn:))*