# clickedRow

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The row number of the cell that the user clicked to display a context menu.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var clickedRow: Int { get }
```

```objc
@property (readonly) NSInteger clickedRow;
```

## Discussion

The value of this property is `-1` if no context menu is active.

## See Also

### Handling Mouse-Click Events
- [func doClick(Any?)](./doclick%28_%29.md)
  Responds to (single) mouse clicks in a column of the browser.
- [func doDoubleClick(Any?)](./dodoubleclick%28_%29.md)
  Responds to double clicks in a column of the browser.
- [var clickedColumn: Int](./clickedcolumn.md)
  The column number of the cell that the user clicked to display a context menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/clickedrow)*