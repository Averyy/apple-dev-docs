# begin(withDelegate:didEnd:contextInfo:)

**Framework**: Quartz  
**Kind**: method

Opens a picture taker pane.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func begin(withDelegate delegate: Any!, didEnd didEndSelector: Selector!, contextInfo: UnsafeMutableRawPointer!)
```

#### Discussion

The `didEndSelector` method should have the following signature:

`- (void)pictureTakerDidEnd:(IKPictureTaker *)sheet returnCode:(NSInteger)returnCode contextInfo:(void *)contextInfo;`

The `returnCode` value is set to `NSOKButton` if the user validates, or to `NSCancelButton` if the user cancels.

## Parameters

- `delegate`: The object that will invoke the selector    when the picture taker session terminates.
- `didEndSelector`: The selector to invoke when the picture taker session terminates.
- `contextInfo`: Any data that must be passed as an argument to the delegate through   after the picture taker session terminates.

## See Also

- [class func pictureTaker() -> IKPictureTaker!](ikpicturetaker/picturetaker.md)
  Returns a shared `IKPictureTaker` instance, creating it if necessary.
- [func beginSheet(for: NSWindow!, withDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](ikpicturetaker/beginsheet(for:withdelegate:didend:contextinfo:).md)
  Opens a picture taker as a sheet whose parent is the specified window.
- [func popUpRecentsMenu(for: NSView!, withDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](ikpicturetaker/popuprecentsmenu(for:withdelegate:didend:contextinfo:).md)
  Displays the Open Recent popup menu associated with the  picture taker.
- [func runModal() -> Int](ikpicturetaker/runmodal.md)
  Opens a modal picture taker dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikpicturetaker/begin(withdelegate:didend:contextinfo:))*