# frame(ofInsideOfColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle containing the specified column, not including borders.

**Availability**:
- macOS

## Declaration

```swift
func frame(ofInsideOfColumn column: Int) -> NSRect
```

```objc
- (NSRect) frameOfInsideOfColumn:(NSInteger) column;
```

#### Return Value

The rectangle containing the column, not including the column borders.

## Parameters

- `column`: The index of the column for which to retrieve the inside frame.

## See Also

### Getting Column Frames
- [func frame(ofColumn: Int) -> NSRect](./frame%28ofcolumn%29.md)
  Returns the rectangle containing the given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/frame(ofinsideofcolumn:))*