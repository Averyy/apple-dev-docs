# UIActivityViewController.CollaborationModeRestriction

**Framework**: UIKit  
**Kind**: class

An object that disables the sharing mode and optionally displays an alert.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
class CollaborationModeRestriction
```

## Mentions

- [Collaborating and sharing copies of your data](collaborating-and-sharing-copies-of-your-data.md)

## Topics

### Creating a disabled mode
- [init(disabledMode: UIActivityCollaborationMode)](uiactivityviewcontroller/collaborationmoderestriction/init(disabledmode:).md)
  Copies the provided disabled mode.
- [init(disabledMode: UIActivityCollaborationMode, alertTitle: String, alertMessage: String)](uiactivityviewcontroller/collaborationmoderestriction/init(disabledmode:alerttitle:alertmessage:).md)
  Creates a disabled mode that displays an alert when someone tries to select that mode.
- [init(disabledMode: UIActivityCollaborationMode, alertTitle: String, alertMessage: String, alertDismissButtonTitle: String)](uiactivityviewcontroller/collaborationmoderestriction/init(disabledmode:alerttitle:alertmessage:alertdismissbuttontitle:).md)
  Creates a disabled mode that displays an alert with a customized dismiss button.
- [init(disabledMode: UIActivityCollaborationMode, alertTitle: String, alertMessage: String, alertDismissButtonTitle: String, alertRecoverySuggestionButtonTitle: String, alertRecoverySuggestionButtonLaunch: URL)](uiactivityviewcontroller/collaborationmoderestriction/init(disabledmode:alerttitle:alertmessage:alertdismissbuttontitle:alertrecoverysuggestionbuttontitle:alertrecoverysuggestionbuttonlaunch:).md)
  Creates a disabled mode that displays an alert with a recovery suggestion.
### Accessing the disabled mode’s properties
- [var alertDismissButtonTitle: String?](uiactivityviewcontroller/collaborationmoderestriction/alertdismissbuttontitle.md)
  A title for the alert’s dismiss button.
- [var alertMessage: String?](uiactivityviewcontroller/collaborationmoderestriction/alertmessage.md)
  A message displayed by the alert
- [var alertRecoverySuggestionButtonLaunchURL: URL?](uiactivityviewcontroller/collaborationmoderestriction/alertrecoverysuggestionbuttonlaunchurl.md)
  A launch URL that the system passes to your app when someone taps the recovery suggestion button.
- [var alertRecoverySuggestionButtonTitle: String?](uiactivityviewcontroller/collaborationmoderestriction/alertrecoverysuggestionbuttontitle.md)
  A title for the alert’s recovery suggestion button.
- [var alertTitle: String?](uiactivityviewcontroller/collaborationmoderestriction/alerttitle.md)
  A title for the alert that the system displays when someone selects the disabled mode.
- [var disabledMode: UIActivityCollaborationMode](uiactivityviewcontroller/collaborationmoderestriction/disabledmode.md)
  The mode that is disabled.
- [func description() -> String](uiactivityviewcontroller/collaborationmoderestriction/description.md)
  Returns a description of the disabled mode.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [enum UIActivityCollaborationMode](uiactivitycollaborationmode.md)
  A value that defines how the system shares an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/collaborationmoderestriction)*