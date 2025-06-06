# NSPathControlDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of methods that can be implemented by the delegate of a path control object to support dragging to and from the control.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSPathControlDelegate : NSObjectProtocol
```

## Topics

### Dragging Support
- [func pathControl(NSPathControl, shouldDrag: NSPathComponentCell, with: NSPasteboard) -> Bool](nspathcontroldelegate/pathcontrol(_:shoulddrag:with:)-35j1e.md)
  Implement this method to enable dragging from the control.
- [func pathControl(NSPathControl, validateDrop: any NSDraggingInfo) -> NSDragOperation](nspathcontroldelegate/pathcontrol(_:validatedrop:).md)
  Implement this method to enable dragging onto the control.
- [func pathControl(NSPathControl, acceptDrop: any NSDraggingInfo) -> Bool](nspathcontroldelegate/pathcontrol(_:acceptdrop:).md)
  Implement this method to accept previously validated contents dropped onto the control.
### Customizing a Pop-Up–Style Path
- [func pathControl(NSPathControl, willDisplay: NSOpenPanel)](nspathcontroldelegate/pathcontrol(_:willdisplay:).md)
  Implement this method to customize the Open panel shown by a pop-up–style path.
- [func pathControl(NSPathControl, willPopUp: NSMenu)](nspathcontroldelegate/pathcontrol(_:willpopup:).md)
  Implement this method to customize the menu of a pop-up–style path.
### Instance Methods
- [func pathControl(NSPathControl, shouldDrag: NSPathControlItem, with: NSPasteboard) -> Bool](nspathcontroldelegate/pathcontrol(_:shoulddrag:with:)-5ciyd.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcontroldelegate)*