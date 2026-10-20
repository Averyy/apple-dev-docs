# application(_:willEncodeRestorableState:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the app is about to encode its restorable state.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func application(_ app: NSApplication, willEncodeRestorableState coder: NSCoder)
```

```objc
- (void) application:(NSApplication *) app willEncodeRestorableState:(NSCoder *) coder;
```

## Parameters

- `app`: The application.
- `coder`: The coder extracting the archive.

## See Also

### Restoring Application State
- [func applicationSupportsSecureRestorableState(NSApplication) -> Bool](./applicationsupportssecurerestorablestate%28_%29.md)
  Returns a Boolean value that indicates if the app supports secure state restoration.
- [func applicationProtectedDataDidBecomeAvailable(Notification)](./applicationprotecteddatadidbecomeavailable%28_%29.md)
  Tells the delegate that protected data is now available.
- [func applicationProtectedDataWillBecomeUnavailable(Notification)](./applicationprotecteddatawillbecomeunavailable%28_%29.md)
  Tells the delegate that protected data is about to become unavailable.
- [func application(NSApplication, didDecodeRestorableState: NSCoder)](./application%28_,diddecoderestorablestate%29.md)
  Tells the delegate when the app finished decoding its restorable state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:willencoderestorablestate:))*