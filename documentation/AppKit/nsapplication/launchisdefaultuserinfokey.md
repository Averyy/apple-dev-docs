# launchIsDefaultUserInfoKey

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates if the app launch is a default launch.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class let launchIsDefaultUserInfoKey: String
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) containing a Boolean value. The value is [`false`](https://developer.apple.com/documentation/Swift/false) if the app was launched to open or print a file, to perform a Service action, if the app had saved state that will be restored, or if the app launch was in some other sense not a default launch. Otherwise its value will be [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [class let launchUserNotificationUserInfoKey: String](nsapplication/launchusernotificationuserinfokey.md)
  A key that indicates your app was launched because a user activated a notification in the Notification Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/launchisdefaultuserinfokey)*