# init(disabledMode:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Copies the provided disabled mode.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
init(disabledMode: UIActivityCollaborationMode)
```

```objc
- (instancetype) initWithDisabledMode:(UIActivityCollaborationMode) disabledMode;
```

## See Also

### Creating a disabled mode
- [init(disabledMode: UIActivityCollaborationMode, alertTitle: String, alertMessage: String)](./init%28disabledmode,alerttitle,alertmessage%29.md)
  Creates a disabled mode that displays an alert when someone tries to select that mode.
- [init(disabledMode: UIActivityCollaborationMode, alertTitle: String, alertMessage: String, alertDismissButtonTitle: String)](./init%28disabledmode,alerttitle,alertmessage,alertdismissbuttontitle%29.md)
  Creates a disabled mode that displays an alert with a customized dismiss button.
- [init(disabledMode: UIActivityCollaborationMode, alertTitle: String, alertMessage: String, alertDismissButtonTitle: String, alertRecoverySuggestionButtonTitle: String, alertRecoverySuggestionButtonLaunch: URL)](./init%28disabledmode,alerttitle,alertmessage,alertdismissbuttontitle,alertrecoverysuggestionbuttontitle,alertrecoverysuggestionbuttonlaunch%29.md)
  Creates a disabled mode that displays an alert with a recovery suggestion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/collaborationmoderestriction/init(disabledmode:))*