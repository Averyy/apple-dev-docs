# setPassword(_:)

**Framework**: Security Interface  
**Kind**: method

Specifies the password for the keychain that will be created.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func setPassword(_ password: String!)
```

#### Discussion

This method is optional. If you don’t call this method, the keychain save panel displays a password-entry dialog.

## Parameters

- `password`: The password to be used for the new keychain.

## See Also

- [func beginSheet(forDirectory: String!, file: String!, modalFor: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](sfkeychainsavepanel/beginsheet(fordirectory:file:modalfor:modaldelegate:didend:contextinfo:).md)
  Displays a sheet that allows a user to create a new keychain.
- [func runModal(forDirectory: String!, file: String!) -> Int](sfkeychainsavepanel/runmodal(fordirectory:file:).md)
  Displays a panel that allows a user to create a new keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfkeychainsavepanel/setpassword(_:))*