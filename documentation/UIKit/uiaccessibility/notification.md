# UIAccessibility.Notification

**Framework**: UIKit  
**Kind**: struct

An accessibility notification that an app can send.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 2.0+

## Declaration

```swift
struct Notification
```

## Topics

### Notifications
- [static let announcement: UIAccessibility.Notification](uiaccessibility/notification/announcement.md)
  A notification that an app posts when it needs to convey an announcement to the assistive app.
- [static let layoutChanged: UIAccessibility.Notification](uiaccessibility/notification/layoutchanged.md)
  A notification that an app posts when the layout of a screen changes.
- [static let screenChanged: UIAccessibility.Notification](uiaccessibility/notification/screenchanged.md)
  A notification that an app posts when a new view appears that occupies a major portion of the screen.
- [static let pageScrolled: UIAccessibility.Notification](uiaccessibility/notification/pagescrolled.md)
  A notification that an app posts when a scroll action completes.
- [static let pauseAssistiveTechnology: UIAccessibility.Notification](uiaccessibility/notification/pauseassistivetechnology.md)
  A notification that pauses an assistive app’s operations temporarily.
- [static let resumeAssistiveTechnology: UIAccessibility.Notification](uiaccessibility/notification/resumeassistivetechnology.md)
  A notification that resumes an assistive app’s operations temporarily.
- [UIAccessibility.AssistiveTechnologyIdentifier](uiaccessibility/assistivetechnologyidentifier.md)
  Identifiers for assistive apps.
### Initializer
- [init(rawValue: UInt32)](uiaccessibility/notification/init(rawvalue:).md)
  Creates an accessibility notification with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Notification names](notification-names.md)
  The names of notifications that the accessibility system generates.
- [Notification dictionary keys](notification-dictionary-keys.md)
  Handle notifications with keys in the user info dictionary.
- [static func post(notification: UIAccessibility.Notification, argument: Any?)](uiaccessibility/post(notification:argument:).md)
  Posts a notification to assistive apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/notification)*