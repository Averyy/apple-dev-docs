# indentationMarkerFollowsCell

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the indentation marker symbol displayed in the outline column should be indented along with the cell contents.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var indentationMarkerFollowsCell: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the indentation marker is indented along with the cell contents. When the value is [`false`](https://developer.apple.com/documentation/Swift/false), the marker is always displayed left-justified in the column. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [func level(forItem: Any?) -> Int](nsoutlineview/level(foritem:).md)
  Returns the indentation level for a given item.
- [func level(forRow: Int) -> Int](nsoutlineview/level(forrow:).md)
  Returns the indentation level for a given row.
- [var indentationPerLevel: CGFloat](nsoutlineview/indentationperlevel.md)
  The per-level indentation, measured in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/indentationmarkerfollowscell)*