# applicationSupportsSecureRestorableState(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates if the app supports secure state restoration.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
optional func applicationSupportsSecureRestorableState(_ app: NSApplication) -> Bool
```

```objc
- (BOOL) applicationSupportsSecureRestorableState:(NSApplication *) app;
```

## Return Value

`true` when the app supports secure state restoration; otherwise, `false`.

## Parameters

- `app`: The app object associated with the delegate.

## See Also

### Restoring Application State
- [func applicationProtectedDataDidBecomeAvailable(Notification)](./applicationprotecteddatadidbecomeavailable%28_%29.md)
  Tells the delegate that protected data is now available.
- [func applicationProtectedDataWillBecomeUnavailable(Notification)](./applicationprotecteddatawillbecomeunavailable%28_%29.md)
  Tells the delegate that protected data is about to become unavailable.
- [func application(NSApplication, willEncodeRestorableState: NSCoder)](./application%28_,willencoderestorablestate%29.md)
  Tells the delegate that the app is about to encode its restorable state.
- [func application(NSApplication, didDecodeRestorableState: NSCoder)](./application%28_,diddecoderestorablestate%29.md)
  Tells the delegate when the app finished decoding its restorable state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationsupportssecurerestorablestate(_:))*