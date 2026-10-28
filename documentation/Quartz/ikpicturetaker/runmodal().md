# runModal()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Opens a modal picture taker dialog.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func runModal() -> Int
```

```objc
- (NSInteger) runModal;
```

## Return Value

Returns `NSOKButton` if the user edits or chooses an image; `NSCancelButton` if the user cancels or does not change the default image.

## See Also

### Creating And Displaying The Picture Taker
- [class func pictureTaker() -> IKPictureTaker!](./picturetaker%28%29.md)
  Returns a shared `IKPictureTaker` instance, creating it if necessary.
- [func beginSheet(for: NSWindow!, withDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](./beginsheet%28for,withdelegate,didend,contextinfo%29.md)
  Opens a picture taker as a sheet whose parent is the specified window.
- [func begin(withDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](./begin%28withdelegate,didend,contextinfo%29.md)
  Opens a picture taker pane.
- [func popUpRecentsMenu(for: NSView!, withDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](./popuprecentsmenu%28for,withdelegate,didend,contextinfo%29.md)
  Displays the Open Recent popup menu associated with the  picture taker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikpicturetaker/runmodal())*