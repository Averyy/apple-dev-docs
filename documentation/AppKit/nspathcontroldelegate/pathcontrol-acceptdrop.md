# pathControl(_:acceptDrop:)

**Framework**: AppKit  
**Kind**: method

Implement this method to accept previously validated contents dropped onto the control.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func pathControl(_ pathControl: NSPathControl, acceptDrop info: any NSDraggingInfo) -> Bool
```

#### Discussion

In order to accept the dropped contents previously accepted from [`pathControl(_:validateDrop:)`](nspathcontroldelegate/pathcontrol(_:validatedrop:).md), you must implement this method. This method is called from performDragOperation:. You should change the URL value based on the dragged information.

If not implemented, and the control’s cell is editable, the drop is accepted if it contains an `NSURLPboardType` or `NSFilenamesPboardType` that conforms to the cell’s allowed types. The cell’s URL value is automatically changed, and the action is invoked. Implementation of this method is optional.

## Parameters

- `pathControl`: The path control that sent the message.
- `info`: An object containing details about this dragging operation.

## See Also

- [func pathControl(NSPathControl, shouldDrag: NSPathComponentCell, with: NSPasteboard) -> Bool](nspathcontroldelegate/pathcontrol(_:shoulddrag:with:)-35j1e.md)
  Implement this method to enable dragging from the control.
- [func pathControl(NSPathControl, validateDrop: any NSDraggingInfo) -> NSDragOperation](nspathcontroldelegate/pathcontrol(_:validatedrop:).md)
  Implement this method to enable dragging onto the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcontroldelegate/pathcontrol(_:acceptdrop:))*