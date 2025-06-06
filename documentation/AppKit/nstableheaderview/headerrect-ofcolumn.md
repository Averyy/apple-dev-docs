# headerRect(ofColumn:)

**Framework**: AppKit  
**Kind**: method

Returns the rectangle containing the header tile for the column at `columnIndex`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func headerRect(ofColumn column: Int) -> NSRect
```

#### Discussion

Raises an `NSInternalInconsistencyException` if `columnIndex` is out of bounds.

## See Also

- [func rect(ofColumn: Int) -> NSRect](nstableview/rect(ofcolumn:).md)
  Returns the rectangle containing the column at the specified index.
- [func column(at: NSPoint) -> Int](nstableheaderview/column(at:).md)
  Returns the index of the column whose header lies under `aPoint` in the receiver, or –1 if no such column is found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableheaderview/headerrect(ofcolumn:))*