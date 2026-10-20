# NSPathControlDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods that can be implemented by the delegate of a path control object to support dragging to and from the control.

**Availability**:
- macOS

## Declaration

```swift
protocol NSPathControlDelegate : NSObjectProtocol
```

```objc
@protocol NSPathControlDelegate <NSObject>
```

## Topics

### Dragging Support
- [func pathControl(NSPathControl, shouldDrag: NSPathComponentCell, with: NSPasteboard) -> Bool](./nspathcontroldelegate/pathcontrol%28_,shoulddrag,with%29-35j1e.md)
  Implement this method to enable dragging from the control.
- [func pathControl(NSPathControl, validateDrop: any NSDraggingInfo) -> NSDragOperation](./nspathcontroldelegate/pathcontrol%28_,validatedrop%29.md)
  Implement this method to enable dragging onto the control.
- [func pathControl(NSPathControl, acceptDrop: any NSDraggingInfo) -> Bool](./nspathcontroldelegate/pathcontrol%28_,acceptdrop%29.md)
  Implement this method to accept previously validated contents dropped onto the control.
### Customizing a Pop-Up–Style Path
- [func pathControl(NSPathControl, willDisplay: NSOpenPanel)](./nspathcontroldelegate/pathcontrol%28_,willdisplay%29.md)
  Implement this method to customize the Open panel shown by a pop-up–style path.
- [func pathControl(NSPathControl, willPopUp: NSMenu)](./nspathcontroldelegate/pathcontrol%28_,willpopup%29.md)
  Implement this method to customize the menu of a pop-up–style path.
### Instance Methods
- [func pathControl(NSPathControl, shouldDrag: NSPathControlItem, with: NSPasteboard) -> Bool](./nspathcontroldelegate/pathcontrol%28_,shoulddrag,with%29-5ciyd.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcontroldelegate)*