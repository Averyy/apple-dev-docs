# frame(ofColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle containing the given column.

**Availability**:
- macOS

## Declaration

```swift
func frame(ofColumn column: Int) -> NSRect
```

```objc
- (NSRect) frameOfColumn:(NSInteger) column;
```

## Return Value

The rectangle containing the specified column.

## Parameters

- `column`: The index of the column for which to retrieve the frame.

## See Also

### Getting Column Frames
- [func frame(ofInsideOfColumn: Int) -> NSRect](./frame%28ofinsideofcolumn%29.md)
  Returns the rectangle containing the specified column, not including borders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/frame(ofcolumn:))*