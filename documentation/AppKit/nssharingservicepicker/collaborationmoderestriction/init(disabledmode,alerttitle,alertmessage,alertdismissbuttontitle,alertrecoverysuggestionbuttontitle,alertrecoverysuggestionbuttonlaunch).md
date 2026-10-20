# init(disabledMode:alertTitle:alertMessage:alertDismissButtonTitle:alertRecoverySuggestionButtonTitle:alertRecoverySuggestionButtonLaunch:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- macOS 15.0+

## Declaration

```swift
init(disabledMode: NSSharingCollaborationMode, alertTitle: String, alertMessage: String, alertDismissButtonTitle: String, alertRecoverySuggestionButtonTitle: String, alertRecoverySuggestionButtonLaunch alertRecoverySuggestionButtonLaunchURL: URL)
```

```objc
- (instancetype) initWithDisabledMode:(NSSharingCollaborationMode) disabledMode alertTitle:(NSString *) alertTitle alertMessage:(NSString *) alertMessage alertDismissButtonTitle:(NSString *) alertDismissButtonTitle alertRecoverySuggestionButtonTitle:(NSString *) alertRecoverySuggestionButtonTitle alertRecoverySuggestionButtonLaunchURL:(NSURL *) alertRecoverySuggestionButtonLaunchURL;
```

## Parameters

- `disabledMode`: The disabled type of sharing
- `alertTitle`: The alert title
- `alertMessage`: The alert message
- `alertDismissButtonTitle`: The label on the default alert button
- `alertRecoverySuggestionButtonTitle`: The label on the optional recovery suggestion button on the alert
- `alertRecoverySuggestionButtonLaunchURL`: The URL that is opened when the optional recovery suggestion button is selected


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepicker/collaborationmoderestriction/init(disabledmode:alerttitle:alertmessage:alertdismissbuttontitle:alertrecoverysuggestionbuttontitle:alertrecoverysuggestionbuttonlaunch:))*