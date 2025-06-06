# NSOpenSavePanelDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of methods for managing interactions with an open or save panel.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSOpenSavePanelDelegate : NSObjectProtocol
```

## Topics

### Responding to the User’s Selection
- [func panel(Any, userEnteredFilename: String, confirmed: Bool) -> String?](nsopensavepaneldelegate/panel(_:userenteredfilename:confirmed:).md)
  Tells the delegate that the user confirmed a filename choice by clicking Save in a Save panel.
### Responding to Panel Changes
- [func panelSelectionDidChange(Any?)](nsopensavepaneldelegate/panelselectiondidchange(_:).md)
  Tells the delegate that the user changed the selection in the specified Save panel.
- [func panel(Any, didChangeToDirectoryURL: URL?)](nsopensavepaneldelegate/panel(_:didchangetodirectoryurl:).md)
  Tells the delegate that the user changed the selected directory to the directory located at the specified URL.
- [func panel(Any, willExpand: Bool)](nsopensavepaneldelegate/panel(_:willexpand:).md)
  Tells the delegate that the Save panel is about to expand or collapse because the user clicked the disclosure triangle that displays or hides the file browser.
### Validating the Panel Content
- [func panel(Any, shouldEnable: URL) -> Bool](nsopensavepaneldelegate/panel(_:shouldenable:).md)
  Asks the delegate whether the specified URL should be enabled in the Open panel.
- [func panel(Any, validate: URL) throws](nsopensavepaneldelegate/panel(_:validate:).md)
  Asks the delegate to validate the URL for a file that the user selected.
### Instance Methods
- [func panel(Any, didSelect: UTType?)](nsopensavepaneldelegate/panel(_:didselect:).md)
  `NSSavePanel`: Optional — Sent when the user changes the current type. `NSOpenPanel`: Not sent.
- [func panel(Any, displayNameFor: UTType) -> String?](nsopensavepaneldelegate/panel(_:displaynamefor:).md)
  `NSSavePanel`: Optional — Sent when the content type popup is displayed and the save panel needs the display name for a type. If `nil` is returned, the save panel will display type’s `localizedDescription`. `NSOpenPanel`: Not sent.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSPathCell](nspathcell.md)

## See Also

- [class NSOpenPanel](nsopenpanel.md)
  A panel that prompts the user to select a file to open.
- [class NSSavePanel](nssavepanel.md)
  A panel that prompts the user for information about where to save a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopensavepaneldelegate)*