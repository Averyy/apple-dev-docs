# beginSheet(forDirectory:file:modalFor:modalDelegate:didEnd:contextInfo:)

**Framework**: Security Interface  
**Kind**: method

Displays a sheet that allows a user to create a new keychain.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func beginSheet(forDirectory path: String!, file name: String!, modalFor docWindow: NSWindow!, modalDelegate delegate: Any!, didEnd didEndSelector: Selector!, contextInfo: UnsafeMutableRawPointer!)
```

#### Discussion

The delegate method has the following signature:

```objc
- (void)createPanelDidEnd:(NSWindow *)sheet
        returnCode:(int)returnCode
        contextInfo:(void *)contextInfo
```

The parameters for the delegate method are:

The delegate method may dismiss the keychain settings sheet itself; if it does not, the sheet is dismissed on return from the `beginSheetForDirectory:...` method.

Use the [`keychain()`](sfkeychainsavepanel/keychain().md) method to obtain the keychain created by the user.

## Parameters

- `path`: The path to the folder where the keychain is created. Specify   for  .
- `name`: The keychain name to be automatically displayed in the Save As field of the sheet.
- `docWindow`: The parent window to which the sheet is attached. If this parameter is  , the behavior defaults to a standalone modal window.
- `delegate`: The delegate object in which the method specified in the   parameter is implemented.
- `didEndSelector`: A method selector for a delegate method called after the modal session has ended, but before the sheet has been dismissed. Implementation of this delegate method is optional.
- `contextInfo`: A pointer to data that is passed to the delegate method. You can use this data pointer for any purpose you wish.

## See Also

- [func keychain() -> Unmanaged<SecKeychain>!](sfkeychainsavepanel/keychain.md)
  Returns the keychain created by the keychain save panel.
- [func runModal(forDirectory: String!, file: String!) -> Int](sfkeychainsavepanel/runmodal(fordirectory:file:).md)
  Displays a panel that allows a user to create a new keychain.
- [func setPassword(String!)](sfkeychainsavepanel/setpassword(_:).md)
  Specifies the password for the keychain that will be created.
- [func runModal(forDirectory: String!, file: String!) -> Int](sfkeychainsavepanel/runmodal(fordirectory:file:).md)
  Displays a panel that allows a user to create a new keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfkeychainsavepanel/beginsheet(fordirectory:file:modalfor:modaldelegate:didend:contextinfo:))*