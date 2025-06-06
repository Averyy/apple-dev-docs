# pictureTaker()

**Framework**: Quartz  
**Kind**: method

Returns a shared `IKPictureTaker` instance, creating it if necessary.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
class func pictureTaker() -> IKPictureTaker!
```

#### Return Value

An `IKPictureTaker` object.

## See Also

- [func beginSheet(for: NSWindow!, withDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](ikpicturetaker/beginsheet(for:withdelegate:didend:contextinfo:).md)
  Opens a picture taker as a sheet whose parent is the specified window.
- [func begin(withDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](ikpicturetaker/begin(withdelegate:didend:contextinfo:).md)
  Opens a picture taker pane.
- [func popUpRecentsMenu(for: NSView!, withDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](ikpicturetaker/popuprecentsmenu(for:withdelegate:didend:contextinfo:).md)
  Displays the Open Recent popup menu associated with the  picture taker.
- [func runModal() -> Int](ikpicturetaker/runmodal.md)
  Opens a modal picture taker dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikpicturetaker/picturetaker())*