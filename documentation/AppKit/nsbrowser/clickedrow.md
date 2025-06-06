# clickedRow

**Framework**: AppKit  
**Kind**: property

The row number of the cell that the user clicked to display a context menu.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var clickedRow: Int { get }
```

#### Discussion

The value of this property is `-1` if no context menu is active.

## See Also

- [func doClick(Any?)](nsbrowser/doclick(_:).md)
  Responds to (single) mouse clicks in a column of the browser.
- [func doDoubleClick(Any?)](nsbrowser/dodoubleclick(_:).md)
  Responds to double clicks in a column of the browser.
- [var clickedColumn: Int](nsbrowser/clickedcolumn.md)
  The column number of the cell that the user clicked to display a context menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/clickedrow)*