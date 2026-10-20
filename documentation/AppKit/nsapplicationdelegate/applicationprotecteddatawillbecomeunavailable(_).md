# applicationProtectedDataWillBecomeUnavailable(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that protected data is about to become unavailable.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
optional func applicationProtectedDataWillBecomeUnavailable(_ notification: Notification)
```

## See Also

- [func applicationSupportsSecureRestorableState(NSApplication) -> Bool](nsapplicationdelegate/applicationsupportssecurerestorablestate(_:).md)
  Returns a Boolean value that indicates if the app supports secure state restoration.
- [func applicationProtectedDataDidBecomeAvailable(Notification)](nsapplicationdelegate/applicationprotecteddatadidbecomeavailable(_:).md)
  Tells the delegate that protected data is now available.
- [func application(NSApplication, willEncodeRestorableState: NSCoder)](nsapplicationdelegate/application(_:willencoderestorablestate:).md)
  Tells the delegate that the app is about to encode its restorable state.
- [func application(NSApplication, didDecodeRestorableState: NSCoder)](nsapplicationdelegate/application(_:diddecoderestorablestate:).md)
  Tells the delegate when the app finished decoding its restorable state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationprotecteddatawillbecomeunavailable(_:))*