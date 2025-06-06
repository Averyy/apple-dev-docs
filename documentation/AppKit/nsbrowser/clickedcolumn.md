# clickedColumn

**Framework**: AppKit  
**Kind**: property

The column number of the cell that the user clicked to display a context menu.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var clickedColumn: Int { get }
```

#### Discussion

The value of this property is `-1` if no context menu is active.

## See Also

- [func doClick(Any?)](nsbrowser/doclick(_:).md)
  Responds to (single) mouse clicks in a column of the browser.
- [func doDoubleClick(Any?)](nsbrowser/dodoubleclick(_:).md)
  Responds to double clicks in a column of the browser.
- [var clickedRow: Int](nsbrowser/clickedrow.md)
  The row number of the cell that the user clicked to display a context menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/clickedcolumn)*