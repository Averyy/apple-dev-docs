# UIAccessibility.Notification

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

An accessibility notification that an app can send.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 2.0+

## Declaration

```swift
struct Notification
```

```c
typedef uint32_t UIAccessibilityNotifications;
```

## Topics

### Notifications
- [static let announcement: UIAccessibility.Notification](./notification/announcement.md)
  A notification that an app posts when it needs to convey an announcement to the assistive app.
- [static let layoutChanged: UIAccessibility.Notification](./notification/layoutchanged.md)
  A notification that an app posts when the layout of a screen changes.
- [static let screenChanged: UIAccessibility.Notification](./notification/screenchanged.md)
  A notification that an app posts when a new view appears that occupies a major portion of the screen.
- [static let pageScrolled: UIAccessibility.Notification](./notification/pagescrolled.md)
  A notification that an app posts when a scroll action completes.
- [static let pauseAssistiveTechnology: UIAccessibility.Notification](./notification/pauseassistivetechnology.md)
  A notification that pauses an assistive app’s operations temporarily.
- [static let resumeAssistiveTechnology: UIAccessibility.Notification](./notification/resumeassistivetechnology.md)
  A notification that resumes an assistive app’s operations temporarily.
- [UIAccessibility.AssistiveTechnologyIdentifier](./assistivetechnologyidentifier.md)
  Identifiers for assistive apps.
### Initializer
- [init(rawValue: UInt32)](./notification/init%28rawvalue%29.md)
  Creates an accessibility notification with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling notifications
- [Notification names](../notification-names.md)
  The names of notifications that the accessibility system generates.
- [Notification dictionary keys](../notification-dictionary-keys.md)
  Handle notifications with keys in the user info dictionary.
- [static func post(notification: UIAccessibility.Notification, argument: Any?)](./post%28notification,argument%29.md)
  Posts a notification to assistive apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/notification)*