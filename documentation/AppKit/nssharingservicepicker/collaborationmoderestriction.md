# NSSharingServicePicker.CollaborationModeRestriction

**Framework**: AppKit  
**Kind**: class

**Availability**:
- macOS 15.0+

## Declaration

```swift
class CollaborationModeRestriction
```

## Topics

### Initializers
- [init(disabledMode: NSSharingCollaborationMode)](nssharingservicepicker/collaborationmoderestriction/init(disabledmode:).md)
- [init(disabledMode: NSSharingCollaborationMode, alertTitle: String, alertMessage: String)](nssharingservicepicker/collaborationmoderestriction/init(disabledmode:alerttitle:alertmessage:).md)
- [init(disabledMode: NSSharingCollaborationMode, alertTitle: String, alertMessage: String, alertDismissButtonTitle: String)](nssharingservicepicker/collaborationmoderestriction/init(disabledmode:alerttitle:alertmessage:alertdismissbuttontitle:).md)
- [init(disabledMode: NSSharingCollaborationMode, alertTitle: String, alertMessage: String, alertDismissButtonTitle: String, alertRecoverySuggestionButtonTitle: String, alertRecoverySuggestionButtonLaunch: URL)](nssharingservicepicker/collaborationmoderestriction/init(disabledmode:alerttitle:alertmessage:alertdismissbuttontitle:alertrecoverysuggestionbuttontitle:alertrecoverysuggestionbuttonlaunch:).md)
### Instance Properties
- [var alertDismissButtonTitle: String?](nssharingservicepicker/collaborationmoderestriction/alertdismissbuttontitle.md)
  The label on the alert button which will simply confirm that the alert was viewed and dismiss it Defaults to “OK”
- [var alertMessage: String?](nssharingservicepicker/collaborationmoderestriction/alertmessage.md)
  The message of the alert if a reason for disabling is provided
- [var alertRecoverySuggestionButtonLaunchURL: URL?](nssharingservicepicker/collaborationmoderestriction/alertrecoverysuggestionbuttonlaunchurl.md)
  The URL that is opened when the user selects the recovery suggestion, if any
- [var alertRecoverySuggestionButtonTitle: String?](nssharingservicepicker/collaborationmoderestriction/alertrecoverysuggestionbuttontitle.md)
  The label on the recovery suggestion button if it is provided
- [var alertTitle: String?](nssharingservicepicker/collaborationmoderestriction/alerttitle.md)
  The title of the alert if a reason for disabling is provided
- [var disabledMode: NSSharingCollaborationMode](nssharingservicepicker/collaborationmoderestriction/disabledmode.md)
  The type of sharing which should be disabled

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepicker/collaborationmoderestriction)*