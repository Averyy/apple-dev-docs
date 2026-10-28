# announcementRequested

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

This notification posts when an app needs to make an announcement to the user. If VoiceOver is enabled, it’s presented via speech and/or braille. Otherwise, it does nothing.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static let announcementRequested: NSAccessibility.Notification
```

```c
extern NSAccessibilityNotificationName const NSAccessibilityAnnouncementRequestedNotification;
```

## Discussion

This notification requires a `userInfo` dictionary with the key [`announcement`](../notificationuserinfokey/announcement.md) and a localized string containing the announcement. To help an assistive app determine the importance of the announcement, add the appropriate [`priority`](../notificationuserinfokey/priority.md) to the `userInfo` dictionary.

**Swift**:

```swift
let announcement = "The input was invalid."
NSAccessibility.post(
    element: NSApp.mainWindow as Any,
    notification: .announcementRequested,
    userInfo: [
        .announcement: announcement,
        .priority: NSAccessibilityPriorityLevel.medium.rawValue
    ])
```

**Objective-C**:

```objc
NSString *announcement = @"The input was invalid.";
NSAccessibilityPostNotificationWithUserInfo(NSApp, NSAccessibilityAnnouncementRequestedNotification, @{
    NSAccessibilityAnnouncementKey : announcement,
    NSAccessibilityPriorityKey : @(NSAccessibilityPriorityMedium) 
});
```

If you need more control over how your announcements are pronounced, such as including punctuation or setting the spoken language, you can use [`NSAttributedString`](../../../Foundation/nsattributedstring.md). For a list of available string attributes, see [`NSAttributedString.Key`](../../../Foundation/nsattributedstring/key.md).

**Swift**:

```swift
let announcement = NSAttributedString(
    string: "pain",
    attributes: [.accessibilityLanguage: "fr"]
)
NSAccessibility.post(
    element: NSApp.mainWindow as Any,
    notification: .announcementRequested,
    userInfo: [
        .announcement: announcement,
        .priority: NSAccessibilityPriorityLevel.medium.rawValue
    ])
```

**Objective-C**:

```objc
NSAttributedString *announcement =
    [[NSAttributedString alloc] initWithString:@"pain" attributes: @{
    NSAccessibilityLanguageTextAttribute : @"fr"
}];
NSAccessibilityPostNotificationWithUserInfo(NSApp, NSAccessibilityAnnouncementRequestedNotification, @{
    NSAccessibilityAnnouncementKey : announcement,
    NSAccessibilityPriorityKey : @(NSAccessibilityPriorityMedium)
});
```

## See Also

### Notification names
- [static let applicationActivated: NSAccessibility.Notification](./applicationactivated.md)
  This notification is posted after the app has been activated. Post this notification using the [`post(element:notification:)`](../post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let applicationDeactivated: NSAccessibility.Notification](./applicationdeactivated.md)
  This notification is posted after the app has been deactivated.  Post this notification using the [`post(element:notification:)`](../post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let applicationHidden: NSAccessibility.Notification](./applicationhidden.md)
  This notification is posted after the app is hidden. Post this notification using the [`post(element:notification:)`](../post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let applicationShown: NSAccessibility.Notification](./applicationshown.md)
  This notification is posted after the app is shown. Post this notification using the [`post(element:notification:)`](../post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let created: NSAccessibility.Notification](./created.md)
  This notification is posted after an accessibility element is created. Post this notification using the [`post(element:notification:)`](../post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let drawerCreated: NSAccessibility.Notification](./drawercreated.md)
  This notification is posted after a drawer appears. Post this notification using the [`post(element:notification:)`](../post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let focusedUIElementChanged: NSAccessibility.Notification](./focuseduielementchanged.md)
  This notification is posted after an accessibility element gains focus. Post this notification using the [`post(element:notification:)`](../post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let focusedWindowChanged: NSAccessibility.Notification](./focusedwindowchanged.md)
  This notification is posted after the key window changes. Post this notification using the [`post(element:notification:)`](../post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let helpTagCreated: NSAccessibility.Notification](./helptagcreated.md)
  This notification is posted after a help tag appears. Post this notification using the [`post(element:notification:)`](../post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let layoutChanged: NSAccessibility.Notification](./layoutchanged.md)
  This notification is posted after the UI changes in a way that requires the attention of an accessibility client. This notification should be accompanied by a `userInfo` dictionary with the key [`uiElements`](../notificationuserinfokey/uielements.md) and an array containing the UI elements that have been added or changed. Post this notification using the [`post(element:notification:)`](../post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let mainWindowChanged: NSAccessibility.Notification](./mainwindowchanged.md)
  This notification is posted after the main window changes. Post this notification using the [`post(element:notification:)`](../post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let moved: NSAccessibility.Notification](./moved.md)
  This notification is posted after an accessibility element moves. Post this notification using the [`post(element:notification:)`](../post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let resized: NSAccessibility.Notification](./resized.md)
  This notification is posted after an accessibility element’s size changes. Post this notification using the [`post(element:notification:)`](../post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let rowCollapsed: NSAccessibility.Notification](./rowcollapsed.md)
  This notification is posted after a row collapses. Post this notification using the [`post(element:notification:)`](../post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.
- [static let rowCountChanged: NSAccessibility.Notification](./rowcountchanged.md)
  This notification is posted after a row is added or deleted. Post this notification using the [`post(element:notification:)`](../post%28element,notification%29.md) function instead of an `NSNotificationCenter` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/notification/announcementrequested)*