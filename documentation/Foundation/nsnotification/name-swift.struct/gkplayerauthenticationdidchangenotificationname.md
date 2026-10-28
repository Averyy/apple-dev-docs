# GKPlayerAuthenticationDidChangeNotificationName

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A notification that posts after GameKit authenticates the local player.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static let GKPlayerAuthenticationDidChangeNotificationName: NSNotification.Name
```

## Discussion

The object property for this notification is a `GKLocalPlayer` object. Passing `nil` provides standard Notification Center behavior, which is to receive the notification for any object.

## See Also

### GameKit
- [static let GKPlayerDidChangeNotificationName: NSNotification.Name](./gkplayerdidchangenotificationname.md)
  A notification that posts when a player object’s data changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/gkplayerauthenticationdidchangenotificationname)*