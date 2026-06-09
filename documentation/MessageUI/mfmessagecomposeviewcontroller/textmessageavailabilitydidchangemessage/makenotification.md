# makeNotification(_:)

**Framework**: Message UI  
**Kind**: method

Transform a type-safe Message into a legacy Notification

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func makeNotification(_ message: MFMessageComposeViewController.TextMessageAvailabilityDidChangeMessage) -> Notification
```

#### Return Value

A Notification compatible with Objective-C observers

## Parameters

- `message`: The message to convert


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/textmessageavailabilitydidchangemessage/makenotification(_:))*