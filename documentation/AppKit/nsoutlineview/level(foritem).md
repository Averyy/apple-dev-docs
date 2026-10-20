# level(forItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the indentation level for a given item.

**Availability**:
- macOS

## Declaration

```swift
func level(forItem item: Any?) -> Int
```

```objc
- (NSInteger) levelForItem:(id) item;
```

#### Return Value

The indentation level for `item`. If `item` is `nil` (which is the root item), returns `–1`.

#### Discussion

The levels are zero-based—that is, the first level of displayed items is level `0`.

## Parameters

- `item`: An item in the receiver.

## See Also

### Working with Indentation
- [func level(forRow: Int) -> Int](./level%28forrow%29.md)
  Returns the indentation level for a given row.
- [var indentationPerLevel: CGFloat](./indentationperlevel.md)
  The per-level indentation, measured in points.
- [var indentationMarkerFollowsCell: Bool](./indentationmarkerfollowscell.md)
  A Boolean value indicating whether the indentation marker symbol displayed in the outline column should be indented along with the cell contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/level(foritem:))*