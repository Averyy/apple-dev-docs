# UIActivityViewController.CollaborationModeRestriction

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UIActivityCollaborationModeRestriction : NSObject
```

## Mentions

- [Collaborating and sharing copies of your data](../collaborating-and-sharing-copies-of-your-data.md)

## Topics

### Creating a disabled mode
- [init(disabledMode: UIActivityCollaborationMode)](./collaborationmoderestriction/init%28disabledmode%29.md)
  Copies the provided disabled mode.
- [init(disabledMode: UIActivityCollaborationMode, alertTitle: String, alertMessage: String)](./collaborationmoderestriction/init%28disabledmode,alerttitle,alertmessage%29.md)
  Creates a disabled mode that displays an alert when someone tries to select that mode.
- [init(disabledMode: UIActivityCollaborationMode, alertTitle: String, alertMessage: String, alertDismissButtonTitle: String)](./collaborationmoderestriction/init%28disabledmode,alerttitle,alertmessage,alertdismissbuttontitle%29.md)
  Creates a disabled mode that displays an alert with a customized dismiss button.
- [init(disabledMode: UIActivityCollaborationMode, alertTitle: String, alertMessage: String, alertDismissButtonTitle: String, alertRecoverySuggestionButtonTitle: String, alertRecoverySuggestionButtonLaunch: URL)](./collaborationmoderestriction/init%28disabledmode,alerttitle,alertmessage,alertdismissbuttontitle,alertrecoverysuggestionbuttontitle,alertrecoverysuggestionbuttonlaunch%29.md)
  Creates a disabled mode that displays an alert with a recovery suggestion.
### Accessing the disabled mode’s properties
- [var alertDismissButtonTitle: String?](./collaborationmoderestriction/alertdismissbuttontitle.md)
  A title for the alert’s dismiss button.
- [var alertMessage: String?](./collaborationmoderestriction/alertmessage.md)
  A message displayed by the alert
- [var alertRecoverySuggestionButtonLaunchURL: URL?](./collaborationmoderestriction/alertrecoverysuggestionbuttonlaunchurl.md)
  A launch URL that the system passes to your app when someone taps the recovery suggestion button.
- [var alertRecoverySuggestionButtonTitle: String?](./collaborationmoderestriction/alertrecoverysuggestionbuttontitle.md)
  A title for the alert’s recovery suggestion button.
- [var alertTitle: String?](./collaborationmoderestriction/alerttitle.md)
  A title for the alert that the system displays when someone selects the disabled mode.
- [var disabledMode: UIActivityCollaborationMode](./collaborationmoderestriction/disabledmode.md)
  The mode that is disabled.
- [func description() -> String](./collaborationmoderestriction/description%28%29.md)
  Returns a description of the disabled mode.
### Initializers
- [init?(coder: NSCoder)](./collaborationmoderestriction/init%28coder%29.md)
- [init(disabledMode: UIActivityCollaborationMode, alertTitle: String, alertMessage: String, alertDismissButtonTitle: String, alertRecoverySuggestionButtonTitle: String, alertRecoverySuggestionButtonLaunchURL: URL)](./collaborationmoderestriction/init%28disabledmode,alerttitle,alertmessage,alertdismissbuttontitle,alertrecoverysuggestionbuttontitle,alertrecoverysuggestionbuttonlaunchurl%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)

## See Also

### Restricting the sharing mode
- [enum UIActivityCollaborationMode](../uiactivitycollaborationmode.md)
  A value that defines how the system shares an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/collaborationmoderestriction)*