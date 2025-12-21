# runModal(forDirectory:file:)

**Framework**: Security Interface  
**Kind**: method

Displays a panel that allows a user to create a new keychain.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func runModal(forDirectory path: String!, file name: String!) -> Int
```

#### Discussion

This method returns a result code from the [`runModalForDirectory:file:types:`](https://developer.apple.com/documentation/AppKit/NSOpenPanel/runModalForDirectory:file:types:) method of the [`NSSavePanel`](https://developer.apple.com/documentation/AppKit/NSSavePanel) class: [`NSFileHandlingPanelOKButton`](https://developer.apple.com/documentation/AppKit/NSFileHandlingPanelOKButton) if the user clicks the OK button or [`NSFileHandlingPanelCancelButton`](https://developer.apple.com/documentation/AppKit/NSFileHandlingPanelCancelButton) if the user clicks the Cancel button.

Use the [`keychain()`](sfkeychainsavepanel/keychain().md) method to obtain the keychain created by the user.

## Parameters

- `path`: The path to the folder where the keychain is created. Specify   for  .
- `name`: The keychain name to be automatically displayed in the Save As field of the panel.

## See Also

- [func setPassword(String!)](sfkeychainsavepanel/setpassword(_:).md)
  Specifies the password for the keychain that will be created.
- [func beginSheet(forDirectory: String!, file: String!, modalFor: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](sfkeychainsavepanel/beginsheet(fordirectory:file:modalfor:modaldelegate:didend:contextinfo:).md)
  Displays a sheet that allows a user to create a new keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfkeychainsavepanel/runmodal(fordirectory:file:))*