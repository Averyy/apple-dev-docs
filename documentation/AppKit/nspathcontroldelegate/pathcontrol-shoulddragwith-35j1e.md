# pathControl(_:shouldDrag:with:)

**Framework**: AppKit  
**Kind**: method

Implement this method to enable dragging from the control.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func pathControl(_ pathControl: NSPathControl, shouldDrag pathComponentCell: NSPathComponentCell, with pasteboard: NSPasteboard) -> Bool
```

#### Discussion

This method is called when a drag is about to begin. You can refuse to allow the drag to happen by returning [`false`](https://developer.apple.com/documentation/Swift/false) and allow it by returning [`true`](https://developer.apple.com/documentation/Swift/true). By default, the pasteboard automatically has the following types on it: `NSStringPboardType`, `NSURLPboardType` (if there is a URL value for the cell being dragged), and `NSFilenamesPboardType` (if the URL value returns [`true`](https://developer.apple.com/documentation/Swift/true) from -[`isFileURL`](https://developer.apple.com/documentation/Foundation/NSURL/isFileURL)). You can customize the types placed on the pasteboard at this time, if desired. Implementation of this method is optional.

## Parameters

- `pathControl`: The path control that sent the message.
- `pathComponentCell`: The path component cell from which the drag is beginning.
- `pasteboard`: The pasteboard.

## See Also

- [func pathControl(NSPathControl, validateDrop: any NSDraggingInfo) -> NSDragOperation](nspathcontroldelegate/pathcontrol(_:validatedrop:).md)
  Implement this method to enable dragging onto the control.
- [func pathControl(NSPathControl, acceptDrop: any NSDraggingInfo) -> Bool](nspathcontroldelegate/pathcontrol(_:acceptdrop:).md)
  Implement this method to accept previously validated contents dropped onto the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcontroldelegate/pathcontrol(_:shoulddrag:with:)-35j1e)*