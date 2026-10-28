# UIAccessibility.AssistiveTechnologyIdentifier

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Identifiers for assistive apps.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 5.0+

## Declaration

```swift
struct AssistiveTechnologyIdentifier
```

```c
typedef NSString * UIAccessibilityAssistiveTechnologyIdentifier;
```

## Overview

Manage pausing and resuming assistive apps with these identifiers.

## Topics

### Identifiers
- [static let notificationSwitchControl: UIAccessibility.AssistiveTechnologyIdentifier](./assistivetechnologyidentifier/notificationswitchcontrol.md)
  The Switch Control accessibility feature.
- [static let notificationVoiceOver: UIAccessibility.AssistiveTechnologyIdentifier](./assistivetechnologyidentifier/notificationvoiceover.md)
  The VoiceOver assistive app.
### Initializer
- [init(rawValue: String)](./assistivetechnologyidentifier/init%28rawvalue%29.md)
  Creates an assistive app identifier with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Notification keys
- [static let announcementStringValueUserInfoKey: String](./announcementstringvalueuserinfokey.md)
  The text of the announcement.
- [static let announcementWasSuccessfulUserInfoKey: String](./announcementwassuccessfuluserinfokey.md)
  A Boolean value that indicates whether the announcement is successful.
- [static let focusedElementUserInfoKey: String](./focusedelementuserinfokey.md)
  The element currently in focus by the assistive app.
- [static let unfocusedElementUserInfoKey: String](./unfocusedelementuserinfokey.md)
  The element previously in focus by the assistive app.
- [static let assistiveTechnologyUserInfoKey: String](./assistivetechnologyuserinfokey.md)
  The identifier of the assistive app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/assistivetechnologyidentifier)*