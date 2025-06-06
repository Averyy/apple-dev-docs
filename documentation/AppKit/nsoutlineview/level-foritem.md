# level(forItem:)

**Framework**: AppKit  
**Kind**: method

Returns the indentation level for a given item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func level(forItem item: Any?) -> Int
```

#### Return Value

The indentation level for `item`. If `item` is `nil` (which is the root item), returns `–1`.

#### Discussion

The levels are zero-based—that is, the first level of displayed items is level `0`.

## Parameters

- `item`: An item in the receiver.

## See Also

- [func level(forRow: Int) -> Int](nsoutlineview/level(forrow:).md)
  Returns the indentation level for a given row.
- [var indentationPerLevel: CGFloat](nsoutlineview/indentationperlevel.md)
  The per-level indentation, measured in points.
- [var indentationMarkerFollowsCell: Bool](nsoutlineview/indentationmarkerfollowscell.md)
  A Boolean value indicating whether the indentation marker symbol displayed in the outline column should be indented along with the cell contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/level(foritem:))*