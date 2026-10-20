# response

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The response with which the user responded to a notification.

**Availability**:
- macOS 10.9+ - Deprecated in 11.0

## Declaration

```swift
@NSCopying
var response: NSAttributedString? { get }
```

```objc
@property (copy, readonly, nullable) NSAttributedString * response;
```

#### Discussion

When the user responds to a notification, the [`NSUserNotificationCenterDelegate`](../nsusernotificationcenterdelegate.md) method [`userNotificationCenter(_:didActivate:)`](../nsusernotificationcenterdelegate/usernotificationcenter%28_,didactivate%29.md) is called with the notification, the [`activationType`](./activationtype-swift.property.md) property set to [`NSUserNotification.ActivationType.replied`](./activationtype-swift.enum/replied.md), and this property is set with the user’s response.

## See Also

### Display Information
- [var title: String?](./title.md)
  Specifies the title of the notification.
- [var subtitle: String?](./subtitle.md)
  Specifies the subtitle of the notification.
- [var informativeText: String?](./informativetext.md)
  The body text of the notification.
- [var contentImage: NSImage?](./contentimage.md)
  Image shown in the content of the notification.
- [var identifier: String?](./identifier.md)
  A string that uniquely identifies a notification.
- [var responsePlaceholder: String?](./responseplaceholder.md)
  Optional placeholder string for inline reply field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/response)*