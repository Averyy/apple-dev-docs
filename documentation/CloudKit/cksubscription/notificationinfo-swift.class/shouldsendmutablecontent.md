# shouldSendMutableContent

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the push notification sets the mutable content flag.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var shouldSendMutableContent: Bool { get set }
```

```objc
@property (assign) BOOL shouldSendMutableContent;
```

## Discussion

When this property is [`true`](../../../Swift/true.md), the server includes the `mutable-content` flag with a value of `1` in the push notification’s payload. When the value is `1`, the system passes the notification to your app extension for modification before delivery.

See [Generating a remote notification](../../../UserNotifications/generating-a-remote-notification.md) for more information about the `mutable-content` flag, and [Modifying content in newly delivered notifications](../../../UserNotifications/modifying-content-in-newly-delivered-notifications.md) for information about how to modify push notification content in your app extension prior to delivery.

The default value of this property is [`false`](../../../Swift/false.md).

## See Also

### Accessing the Notification Info
- [var shouldSendContentAvailable: Bool](./shouldsendcontentavailable.md)
  A Boolean value that indicates whether the push notification includes the content available flag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo-swift.class/shouldsendmutablecontent)*