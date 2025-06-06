# response

**Framework**: Foundation  
**Kind**: property

The response with which the user responded to a notification.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@NSCopying
var response: NSAttributedString? { get }
```

#### Discussion

When the user responds to a notification, the [`NSUserNotificationCenterDelegate`](nsusernotificationcenterdelegate.md) method [`userNotificationCenter(_:didActivate:)`](nsusernotificationcenterdelegate/usernotificationcenter(_:didactivate:).md) is called with the notification, the [`activationType`](nsusernotification/activationtype-swift.property.md) property set to [`NSUserNotification.ActivationType.replied`](nsusernotification/activationtype-swift.enum/replied.md), and this property is set with the user’s response.

## See Also

- [var title: String?](nsusernotification/title.md)
  Specifies the title of the notification.
- [var subtitle: String?](nsusernotification/subtitle.md)
  Specifies the subtitle of the notification.
- [var informativeText: String?](nsusernotification/informativetext.md)
  The body text of the notification.
- [var contentImage: NSImage?](nsusernotification/contentimage.md)
  Image shown in the content of the notification.
- [var identifier: String?](nsusernotification/identifier.md)
  A string that uniquely identifies a notification.
- [var responsePlaceholder: String?](nsusernotification/responseplaceholder.md)
  Optional placeholder string for inline reply field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/response)*