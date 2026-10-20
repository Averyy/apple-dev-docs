# alertMessage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A message displayed by the alert

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
var alertMessage: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * alertMessage;
```

## See Also

### Accessing the disabled mode’s properties
- [var alertDismissButtonTitle: String?](./alertdismissbuttontitle.md)
  A title for the alert’s dismiss button.
- [var alertRecoverySuggestionButtonLaunchURL: URL?](./alertrecoverysuggestionbuttonlaunchurl.md)
  A launch URL that the system passes to your app when someone taps the recovery suggestion button.
- [var alertRecoverySuggestionButtonTitle: String?](./alertrecoverysuggestionbuttontitle.md)
  A title for the alert’s recovery suggestion button.
- [var alertTitle: String?](./alerttitle.md)
  A title for the alert that the system displays when someone selects the disabled mode.
- [var disabledMode: UIActivityCollaborationMode](./disabledmode.md)
  The mode that is disabled.
- [func description() -> String](./description%28%29.md)
  Returns a description of the disabled mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/collaborationmoderestriction/alertmessage)*