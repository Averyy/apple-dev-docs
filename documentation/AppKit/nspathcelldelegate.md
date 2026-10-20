# NSPathCellDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods that enable the delegate of a path cell object to customize the Open panel or pop-up menu of a path whose style is set to [`NSPathControl.Style.popUp`](./nspathcontrol/style/popup.md).

**Availability**:
- macOS

## Declaration

```swift
protocol NSPathCellDelegate : NSObjectProtocol
```

```objc
@protocol NSPathCellDelegate <NSObject>
```

## Topics

### Customizing the Open Panel
- [func pathCell(NSPathCell, willDisplay: NSOpenPanel)](./nspathcelldelegate/pathcell%28_,willdisplay%29.md)
  Implement this method to customize the Open panel shown by a pop-up–style path.
### Customizing the Menu
- [func pathCell(NSPathCell, willPopUp: NSMenu)](./nspathcelldelegate/pathcell%28_,willpopup%29.md)
  Implement this method to customize the menu of a pop-up–style path.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Cells
- [class NSPathCell](./nspathcell.md)
  The user interface of a path control object.
- [class NSPathComponentCell](./nspathcomponentcell.md)
  A component of a path.
- [class NSPathControlItem](./nspathcontrolitem.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcelldelegate)*