# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

## Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated properties
- [var cell: NSCell?](./nscontrol/cell.md)
  The receiver’s cell object.
- [class var cellClass: AnyClass?](./nscontrol/cellclass.md)
  Returns the type of cell used by the receiver.
### Deprecated methods
- [func selectedCell() -> NSCell?](./nscontrol/selectedcell%28%29.md)
  Returns the receiver’s selected cell.
- [func selectedTag() -> Int](./nscontrol/selectedtag%28%29.md)
  Returns the tag of the receiver’s selected cell.
- [func setNeedsDisplay()](./nscontrol/setneedsdisplay%28%29.md)
  Marks the receiver as needing redisplay (assuming automatic display is enabled).
- [func calcSize()](./nscontrol/calcsize%28%29.md)
  Recomputes any internal sizing information for the receiver, if necessary.
- [func selectCell(NSCell)](./nscontrol/selectcell%28_%29.md)
  Selects the specified cell and redraws the control as needed.
- [func drawCell(NSCell)](./nscontrol/drawcell%28_%29.md)
  Draws the specified cell, as long as it belongs to the receiver.
- [func drawCellInside(NSCell)](./nscontrol/drawcellinside%28_%29.md)
  Draws the inside of the receiver’s cell (the area within the bezel or border)
- [func updateCell(NSCell)](./nscontrol/updatecell%28_%29.md)
  Marks the specified cell as in need of redrawing.
- [func updateCellInside(NSCell)](./nscontrol/updatecellinside%28_%29.md)
  Marks the inside of the specified cell as in need of redrawing.
- [- controlTextDidBeginEditing:](../ObjectiveC/nsobject-swift.class/controltextdidbeginediting_.md)
  Sent when a control with editable text begins an editing session.
- [- controlTextDidChange:](../ObjectiveC/nsobject-swift.class/controltextdidchange_.md)
  Sent when the text in the receiving control changes.
- [- controlTextDidEndEditing:](../ObjectiveC/nsobject-swift.class/controltextdidendediting_.md)
  Sent when a control with editable text ends an editing session.

## See Also

### Deprecated
- [- setFloatingPointFormat:left:right:](./nscontrol/setfloatingpointformat_left_right_.md)
  Sets the auto-ranging and floating point number format of the receiver’s cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol-deprecated-symbols)*