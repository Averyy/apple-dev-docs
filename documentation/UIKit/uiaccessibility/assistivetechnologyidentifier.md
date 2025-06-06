# UIAccessibility.AssistiveTechnologyIdentifier

**Framework**: UIKit  
**Kind**: struct

Identifiers for assistive apps.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 5.0+

## Declaration

```swift
struct AssistiveTechnologyIdentifier
```

#### Overview

Manage pausing and resuming assistive apps with these identifiers.

## Topics

### Identifiers
- [static let notificationSwitchControl: UIAccessibility.AssistiveTechnologyIdentifier](uiaccessibility/assistivetechnologyidentifier/notificationswitchcontrol.md)
  The Switch Control accessibility feature.
- [static let notificationVoiceOver: UIAccessibility.AssistiveTechnologyIdentifier](uiaccessibility/assistivetechnologyidentifier/notificationvoiceover.md)
  The VoiceOver assistive app.
### Initializer
- [init(rawValue: String)](uiaccessibility/assistivetechnologyidentifier/init(rawvalue:).md)
  Creates an assistive app identifier with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static let announcementStringValueUserInfoKey: String](uiaccessibility/announcementstringvalueuserinfokey.md)
  The text of the announcement.
- [static let announcementWasSuccessfulUserInfoKey: String](uiaccessibility/announcementwassuccessfuluserinfokey.md)
  A Boolean value that indicates whether the announcement is successful.
- [static let focusedElementUserInfoKey: String](uiaccessibility/focusedelementuserinfokey.md)
  The element currently in focus by the assistive app.
- [static let unfocusedElementUserInfoKey: String](uiaccessibility/unfocusedelementuserinfokey.md)
  The element previously in focus by the assistive app.
- [static let assistiveTechnologyUserInfoKey: String](uiaccessibility/assistivetechnologyuserinfokey.md)
  The identifier of the assistive app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/assistivetechnologyidentifier)*