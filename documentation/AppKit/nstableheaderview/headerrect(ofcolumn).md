# headerRect(ofColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle containing the header tile for the column at `columnIndex`.

**Availability**:
- macOS

## Declaration

```swift
func headerRect(ofColumn column: Int) -> NSRect
```

```objc
- (NSRect) headerRectOfColumn:(NSInteger) column;
```

#### Discussion

Raises an `NSInternalInconsistencyException` if `columnIndex` is out of bounds.

## See Also

### Related Documentation
- [func rect(ofColumn: Int) -> NSRect](../nstableview/rect%28ofcolumn%29.md)
  Returns the rectangle containing the column at the specified index.
### Utility methods
- [func column(at: NSPoint) -> Int](./column%28at%29.md)
  Returns the index of the column whose header lies under `aPoint` in the receiver, or –1 if no such column is found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableheaderview/headerrect(ofcolumn:))*