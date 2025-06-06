# Accessibility Functions

**Framework**: AppKit

Global accessibility functions for custom views and controls.

#### Overview

Use these [`NSAccessibility`](nsaccessibility-swift.struct.md) functions to enhance the accessibility experience of your custom view or control. Standard AppKit elements handle this behavior for you.

##### Notifications

Your custom view or control may need to let the assistive app know when changes occur. For example, if your control’s value changes, you need to send a [`valueChanged`](nsaccessibility-swift.struct/notification/valuechanged.md) notification.

[`NSAccessibility.Notification`](nsaccessibility-swift.struct/notification.md) defines a number of notifications that you can send using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) method. You typically need to send your own notifications only when you’re creating a custom control or when you’re using a standard control in a nonstandard way. Make sure you’re posting any relevant notifications as your control’s state changes.

## Topics

### Notifications
- [static func post(element: Any, notification: NSAccessibility.Notification)](nsaccessibility-swift.struct/post(element:notification:).md)
  Sends a notification to any observing assistive apps.
- [static func post(element: Any, notification: NSAccessibility.Notification, userInfo: [NSAccessibility.NotificationUserInfoKey : Any]?)](nsaccessibility-swift.struct/post(element:notification:userinfo:).md)
  Sends a notification and an optional user info dictionary to any observing assistive apps.
- [NSAccessibility.Notification](nsaccessibility-swift.struct/notification.md)
  The name of the notification.
- [NSAccessibility.NotificationUserInfoKey](nsaccessibility-swift.struct/notificationuserinfokey.md)
  The key in the user info dictionary for a notification.
### Screen Coordinates
- [static func screenRect(fromView: NSView, rect: NSRect) -> NSRect](nsaccessibility-swift.struct/screenrect(fromview:rect:).md)
  Returns the frame in screen coordinates.
- [static func screenPoint(fromView: NSView, point: NSPoint) -> NSPoint](nsaccessibility-swift.struct/screenpoint(fromview:point:).md)
  Returns the point in screen coordinates.
### Accessibility Objects
- [static func unignoredChildren(from: [Any]) -> [Any]](nsaccessibility-swift.struct/unignoredchildren(from:).md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [static func unignoredChildrenForOnlyChild(from: Any) -> [Any]](nsaccessibility-swift.struct/unignoredchildrenforonlychild(from:).md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [static func unignoredDescendant(of: Any) -> Any?](nsaccessibility-swift.struct/unignoreddescendant(of:).md)
  Returns an unignored accessibility object, descending the hierarchy, if necessary.
- [static func unignoredAncestor(of: Any) -> Any?](nsaccessibility-swift.struct/unignoredancestor(of:).md)
  Returns an unignored accessibility object, ascending the hierarchy, if necessary.
### Protected Content
- [static func setMayContainProtectedContent(Bool) -> Bool](nsaccessibility-swift.struct/setmaycontainprotectedcontent(_:).md)
  Sets whether the app may have protected content.
### Descriptions
- [var description: String?](nsaccessibility-swift.struct/action/description.md)
  Returns a standard description for an action.
- [func description(with: NSAccessibility.Subrole?) -> String?](nsaccessibility-swift.struct/role/description(with:).md)
  Returns a standard description for a role and subrole.
- [static func description(for: Any) -> String?](nsaccessibility-swift.struct/role/description(for:).md)
  Returns a standard role description for a user interface element.

## See Also

- [Custom Controls](custom-controls.md)
  Support accessibility for custom user interface elements by adopting a role-specific protocol and implementing its methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/accessibility-functions)*