# informativeText

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The body text of the notification.

**Availability**:
- macOS 10.8+ - Deprecated in 11.0

> **Deprecated**: All NSUserNotifications API should be replaced with UserNotifications.frameworks API

## Declaration

```swift
var informativeText: String? { get set }
```

```objc
@property (copy, nullable) NSString * informativeText;
```

## Discussion

This value should be localized as it is presented to the user. The string is truncated to a length appropriate for display and the property is modified to reflect the truncation.

## See Also

### Display Information
- [var title: String?](./title.md)
  Specifies the title of the notification.
- [var subtitle: String?](./subtitle.md)
  Specifies the subtitle of the notification.
- [var contentImage: NSImage?](./contentimage.md)
  Image shown in the content of the notification.
- [var identifier: String?](./identifier.md)
  A string that uniquely identifies a notification.
- [var response: NSAttributedString?](./response.md)
  The response with which the user responded to a notification.
- [var responsePlaceholder: String?](./responseplaceholder.md)
  Optional placeholder string for inline reply field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsusernotification/informativetext)*