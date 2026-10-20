# applicationSupportsSecureRestorableState(_:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates if the app supports secure state restoration.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
optional func applicationSupportsSecureRestorableState(_ app: NSApplication) -> Bool
```

#### Return Value

`true` when the app supports secure state restoration; otherwise, `false`.

## Parameters

- `app`: The app object associated with the delegate.

## See Also

- [func applicationProtectedDataDidBecomeAvailable(Notification)](nsapplicationdelegate/applicationprotecteddatadidbecomeavailable(_:).md)
  Tells the delegate that protected data is now available.
- [func applicationProtectedDataWillBecomeUnavailable(Notification)](nsapplicationdelegate/applicationprotecteddatawillbecomeunavailable(_:).md)
  Tells the delegate that protected data is about to become unavailable.
- [func application(NSApplication, willEncodeRestorableState: NSCoder)](nsapplicationdelegate/application(_:willencoderestorablestate:).md)
  Tells the delegate that the app is about to encode its restorable state.
- [func application(NSApplication, didDecodeRestorableState: NSCoder)](nsapplicationdelegate/application(_:diddecoderestorablestate:).md)
  Tells the delegate when the app finished decoding its restorable state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationsupportssecurerestorablestate(_:))*