# level(forRow:)

**Framework**: AppKit  
**Kind**: method

Returns the indentation level for a given row.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func level(forRow row: Int) -> Int
```

#### Return Value

The indentation level for `row`. For an invalid row, returns `–1`.

#### Discussion

The levels are zero-based—that is, the first level of displayed items is level `0`.

## Parameters

- `row`: The index of a row in the receiver.

## See Also

- [func level(forItem: Any?) -> Int](nsoutlineview/level(foritem:).md)
  Returns the indentation level for a given item.
- [var indentationPerLevel: CGFloat](nsoutlineview/indentationperlevel.md)
  The per-level indentation, measured in points.
- [var indentationMarkerFollowsCell: Bool](nsoutlineview/indentationmarkerfollowscell.md)
  A Boolean value indicating whether the indentation marker symbol displayed in the outline column should be indented along with the cell contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/level(forrow:))*