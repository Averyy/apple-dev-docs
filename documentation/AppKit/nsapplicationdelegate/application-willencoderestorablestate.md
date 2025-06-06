# application(_:willEncodeRestorableState:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the app is about to encode its restorable state.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func application(_ app: NSApplication, willEncodeRestorableState coder: NSCoder)
```

## Parameters

- `app`: The application.
- `coder`: The coder extracting the archive.

## See Also

- [func applicationSupportsSecureRestorableState(NSApplication) -> Bool](nsapplicationdelegate/applicationsupportssecurerestorablestate(_:).md)
  Returns a Boolean value that indicates if the app supports secure state restoration.
- [func applicationProtectedDataDidBecomeAvailable(Notification)](nsapplicationdelegate/applicationprotecteddatadidbecomeavailable(_:).md)
  Tells the delegate that protected data is now available.
- [func applicationProtectedDataWillBecomeUnavailable(Notification)](nsapplicationdelegate/applicationprotecteddatawillbecomeunavailable(_:).md)
  Tells the delegate that protected data is about to become unavailable.
- [func application(NSApplication, didDecodeRestorableState: NSCoder)](nsapplicationdelegate/application(_:diddecoderestorablestate:).md)
  Tells the delegate when the app finished decoding its restorable state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:willencoderestorablestate:))*