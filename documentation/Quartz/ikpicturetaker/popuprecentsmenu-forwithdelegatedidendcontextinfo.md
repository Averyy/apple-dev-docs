# popUpRecentsMenu(for:withDelegate:didEnd:contextInfo:)

**Framework**: Quartz  
**Kind**: method

Displays the Open Recent popup menu associated with the  picture taker.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func popUpRecentsMenu(for aView: NSView!, withDelegate delegate: Any!, didEnd didEndSelector: Selector!, contextInfo: UnsafeMutableRawPointer!)
```

#### Discussion

The `didEndSelector` method should have the following signature:

`- (void)pictureTakerDidEnd:(IKPictureTaker *)sheet returnCode:(NSInteger)returnCode contextInfo:(void *)contextInfo;`

The `returnCode` value is set to `NSOKButton` if the user validates, or to `NSCancelButton` if the user cancels.

## Parameters

- `aView`: The object that will invoke the selector    when the picture taker session terminates.
- `delegate`: The selector to invoke when the picture taker session terminates.
- `didEndSelector`: Any data that must be passed as an argument to the delegate through   after the picture taker session terminates.
- `contextInfo`: An optional context object available to delegates when called.

## See Also

- [class func pictureTaker() -> IKPictureTaker!](ikpicturetaker/picturetaker.md)
  Returns a shared `IKPictureTaker` instance, creating it if necessary.
- [func beginSheet(for: NSWindow!, withDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](ikpicturetaker/beginsheet(for:withdelegate:didend:contextinfo:).md)
  Opens a picture taker as a sheet whose parent is the specified window.
- [func begin(withDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](ikpicturetaker/begin(withdelegate:didend:contextinfo:).md)
  Opens a picture taker pane.
- [func runModal() -> Int](ikpicturetaker/runmodal.md)
  Opens a modal picture taker dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikpicturetaker/popuprecentsmenu(for:withdelegate:didend:contextinfo:))*