# applicationProtectedDataDidBecomeAvailable(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that protected data is now available.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
optional func applicationProtectedDataDidBecomeAvailable(_ notification: Notification)
```

```objc
- (void) applicationProtectedDataDidBecomeAvailable:(NSNotification *) notification;
```

## See Also

### Restoring Application State
- [func applicationSupportsSecureRestorableState(NSApplication) -> Bool](./applicationsupportssecurerestorablestate%28_%29.md)
  Returns a Boolean value that indicates if the app supports secure state restoration.
- [func applicationProtectedDataWillBecomeUnavailable(Notification)](./applicationprotecteddatawillbecomeunavailable%28_%29.md)
  Tells the delegate that protected data is about to become unavailable.
- [func application(NSApplication, willEncodeRestorableState: NSCoder)](./application%28_,willencoderestorablestate%29.md)
  Tells the delegate that the app is about to encode its restorable state.
- [func application(NSApplication, didDecodeRestorableState: NSCoder)](./application%28_,diddecoderestorablestate%29.md)
  Tells the delegate when the app finished decoding its restorable state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationprotecteddatadidbecomeavailable(_:))*