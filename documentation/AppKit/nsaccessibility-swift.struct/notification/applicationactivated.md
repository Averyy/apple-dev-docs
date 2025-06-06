# applicationActivated

**Framework**: AppKit  
**Kind**: property

This notification is posted after the app has been activated. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.

**Availability**:
- macOS ?+

## Declaration

```swift
static let applicationActivated: NSAccessibility.Notification
```

## See Also

- [static let announcementRequested: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/announcementrequested.md)
  This notification is posted whenever an accessibility element needs to make an announcement to the user. This notification requires a `userInfo` dictionary with the key [`announcement`](nsaccessibility-swift.struct/notificationuserinfokey/announcement.md) and a localized string containing the announcement. To help an assistive app determine the importance of the announcement, add the appropriate [`priority`](nsaccessibility-swift.struct/notificationuserinfokey/priority.md) to the `userInfo` dictionary.
- [static let applicationDeactivated: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/applicationdeactivated.md)
  This notification is posted after the app has been deactivated.  Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let applicationHidden: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/applicationhidden.md)
  This notification is posted after the app is hidden. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let applicationShown: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/applicationshown.md)
  This notification is posted after the app is shown. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let created: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/created.md)
  This notification is posted after an accessibility element is created. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let drawerCreated: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/drawercreated.md)
  This notification is posted after a drawer appears. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let focusedUIElementChanged: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/focuseduielementchanged.md)
  This notification is posted after an accessibility element gains focus. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let focusedWindowChanged: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/focusedwindowchanged.md)
  This notification is posted after the key window changes. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let helpTagCreated: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/helptagcreated.md)
  This notification is posted after a help tag appears. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let layoutChanged: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/layoutchanged.md)
  This notification is posted after the UI changes in a way that requires the attention of an accessibility client. This notification should be accompanied by a `userInfo` dictionary with the key [`uiElements`](nsaccessibility-swift.struct/notificationuserinfokey/uielements.md) and an array containing the UI elements that have been added or changed. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let mainWindowChanged: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/mainwindowchanged.md)
  This notification is posted after the main window changes. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let moved: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/moved.md)
  This notification is posted after an accessibility element moves. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let resized: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/resized.md)
  This notification is posted after an accessibility element’s size changes. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let rowCollapsed: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/rowcollapsed.md)
  This notification is posted after a row collapses. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.
- [static let rowCountChanged: NSAccessibility.Notification](nsaccessibility-swift.struct/notification/rowcountchanged.md)
  This notification is posted after a row is added or deleted. Post this notification using the [`post(element:notification:)`](nsaccessibility-swift.struct/post(element:notification:).md) function instead of an `NSNotificationCenter` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/notification/applicationactivated)*