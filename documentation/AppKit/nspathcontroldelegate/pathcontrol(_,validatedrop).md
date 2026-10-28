# pathControl(_:validateDrop:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Implement this method to enable dragging onto the control.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func pathControl(_ pathControl: NSPathControl, validateDrop info: any NSDraggingInfo) -> NSDragOperation
```

```objc
- (NSDragOperation) pathControl:(NSPathControl *) pathControl validateDrop:(id<NSDraggingInfo>) info;
```

## Discussion

This method is called when something is dragged over the control. Return `NSDragOperationNone` to refuse the drop, or return anything else to accept it.

If not implemented, and the control’s cell is editable, the drop is accepted if it contains an `NSURLPboardType` or `NSFilenamesPboardType` that conforms to the cell’s allowed types. Implementation of this method is optional.

## Parameters

- `pathControl`: The path control that sent the message.
- `info`: An object containing details about this dragging operation.

## See Also

### Dragging Support
- [func pathControl(NSPathControl, shouldDrag: NSPathComponentCell, with: NSPasteboard) -> Bool](./pathcontrol%28_,shoulddrag,with%29-35j1e.md)
  Implement this method to enable dragging from the control.
- [func pathControl(NSPathControl, acceptDrop: any NSDraggingInfo) -> Bool](./pathcontrol%28_,acceptdrop%29.md)
  Implement this method to accept previously validated contents dropped onto the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcontroldelegate/pathcontrol(_:validatedrop:))*