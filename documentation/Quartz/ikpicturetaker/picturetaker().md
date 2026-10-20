# pictureTaker()

**Framework**: Quartz  
**Kind**: method  
**Role**: Type Method

Returns a shared `IKPictureTaker` instance, creating it if necessary.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func pictureTaker() -> IKPictureTaker!
```

```objc
+ (IKPictureTaker *) pictureTaker;
```

#### Return Value

An `IKPictureTaker` object.

## See Also

### Creating And Displaying The Picture Taker
- [func beginSheet(for: NSWindow!, withDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](./beginsheet%28for,withdelegate,didend,contextinfo%29.md)
  Opens a picture taker as a sheet whose parent is the specified window.
- [func begin(withDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](./begin%28withdelegate,didend,contextinfo%29.md)
  Opens a picture taker pane.
- [func popUpRecentsMenu(for: NSView!, withDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](./popuprecentsmenu%28for,withdelegate,didend,contextinfo%29.md)
  Displays the Open Recent popup menu associated with the  picture taker.
- [func runModal() -> Int](./runmodal%28%29.md)
  Opens a modal picture taker dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikpicturetaker/picturetaker())*