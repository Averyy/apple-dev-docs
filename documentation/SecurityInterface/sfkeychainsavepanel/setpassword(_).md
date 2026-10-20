# setPassword(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Specifies the password for the keychain that will be created.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func setPassword(_ password: String!)
```

```objc
- (void) setPassword:(NSString *) password;
```

#### Discussion

This method is optional. If you don’t call this method, the keychain save panel displays a password-entry dialog.

## Parameters

- `password`: The password to be used for the new keychain.

## See Also

### Displaying a Sheet or Panel
- [func beginSheet(forDirectory: String!, file: String!, modalFor: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](./beginsheet%28fordirectory,file,modalfor,modaldelegate,didend,contextinfo%29.md)
  Displays a sheet that allows a user to create a new keychain.
- [func runModal(forDirectory: String!, file: String!) -> Int](./runmodal%28fordirectory,file%29.md)
  Displays a panel that allows a user to create a new keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfkeychainsavepanel/setpassword(_:))*