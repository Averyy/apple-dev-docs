# pathControl(_:shouldDrag:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Implement this method to enable dragging from the control.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func pathControl(_ pathControl: NSPathControl, shouldDrag pathComponentCell: NSPathComponentCell, with pasteboard: NSPasteboard) -> Bool
```

```objc
- (BOOL) pathControl:(NSPathControl *) pathControl shouldDragPathComponentCell:(NSPathComponentCell *) pathComponentCell withPasteboard:(NSPasteboard *) pasteboard;
```

## Discussion

This method is called when a drag is about to begin. You can refuse to allow the drag to happen by returning [`false`](../../Swift/false.md) and allow it by returning [`true`](../../Swift/true.md). By default, the pasteboard automatically has the following types on it: `NSStringPboardType`, `NSURLPboardType` (if there is a URL value for the cell being dragged), and `NSFilenamesPboardType` (if the URL value returns [`true`](../../Swift/true.md) from -[`isFileURL`](../../Foundation/nsurl/isfileurl.md)). You can customize the types placed on the pasteboard at this time, if desired. Implementation of this method is optional.

## Parameters

- `pathControl`: The path control that sent the message.
- `pathComponentCell`: The path component cell from which the drag is beginning.
- `pasteboard`: The pasteboard.

## See Also

### Dragging Support
- [func pathControl(NSPathControl, validateDrop: any NSDraggingInfo) -> NSDragOperation](./pathcontrol%28_,validatedrop%29.md)
  Implement this method to enable dragging onto the control.
- [func pathControl(NSPathControl, acceptDrop: any NSDraggingInfo) -> Bool](./pathcontrol%28_,acceptdrop%29.md)
  Implement this method to accept previously validated contents dropped onto the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcontroldelegate/pathcontrol(_:shoulddrag:with:)-35j1e)*