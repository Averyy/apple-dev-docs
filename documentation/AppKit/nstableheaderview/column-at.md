# column(at:)

**Framework**: AppKit  
**Kind**: method

Returns the index of the column whose header lies under `aPoint` in the receiver, or –1 if no such column is found.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func column(at point: NSPoint) -> Int
```

#### Discussion

`aPoint` is expressed in the receiver’s coordinate system.

## See Also

- [func headerRect(ofColumn: Int) -> NSRect](nstableheaderview/headerrect(ofcolumn:).md)
  Returns the rectangle containing the header tile for the column at `columnIndex`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableheaderview/column(at:))*