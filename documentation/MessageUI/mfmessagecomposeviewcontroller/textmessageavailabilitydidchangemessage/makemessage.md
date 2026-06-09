# makeMessage(_:)

**Framework**: Message UI  
**Kind**: method

Transform a legacy Notification into a type-safe Message

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func makeMessage(_ notification: Notification) -> MFMessageComposeViewController.TextMessageAvailabilityDidChangeMessage?
```

#### Return Value

A Message if the notification contains valid data, nil otherwise

## Parameters

- `notification`: The notification to parse


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/textmessageavailabilitydidchangemessage/makemessage(_:))*