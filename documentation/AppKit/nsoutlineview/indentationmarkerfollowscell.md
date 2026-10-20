# indentationMarkerFollowsCell

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the indentation marker symbol displayed in the outline column should be indented along with the cell contents.

**Availability**:
- macOS

## Declaration

```swift
var indentationMarkerFollowsCell: Bool { get set }
```

```objc
@property BOOL indentationMarkerFollowsCell;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the indentation marker is indented along with the cell contents. When the value is [`false`](../../Swift/false.md), the marker is always displayed left-justified in the column. The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Working with Indentation
- [func level(forItem: Any?) -> Int](./level%28foritem%29.md)
  Returns the indentation level for a given item.
- [func level(forRow: Int) -> Int](./level%28forrow%29.md)
  Returns the indentation level for a given row.
- [var indentationPerLevel: CGFloat](./indentationperlevel.md)
  The per-level indentation, measured in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/indentationmarkerfollowscell)*