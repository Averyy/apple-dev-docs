# SuggestedActionsMessage.Participant

**Framework**: Suggested Actions  
**Kind**: struct

A sender or recipient of a message in a conversation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Participant
```

#### Overview

Create a `Participant` by providing a display name, a handle that uniquely identifies the participant, and a Boolean value that indicates whether the participant is the user of this device. Common handles are phone numbers or email addresses, but you can use any string that uniquely identifies a participant within your app’s user identity system.

To enable the Suggested Actions to tailor the suggested actions to the person who uses a device, make sure the `isUser` parameter of [`init(name:handle:isUser:)`](suggestedactionsmessage/participant/init(name:handle:isuser:).md) is `true` for the participant that uses the device. Set `isUser` to `false` for other participants. The following code snippet shows how an app can initialize a `Participant` who uses the current device and a second participant who sends a message from their own device to the first participant’s device:

```swift
// The participant who uses this device.
let user = SuggestedActionsMessage.Participant(
    name: "Anne Johnson",
    handle: "annejohnson1@icloud.com",
    isUser: true
)

// A second participant, usually contact in the conversation.
let contact = SuggestedActionsMessage.Participant(
    name: "Juan Chavez",
    handle: "chavez4@icloud.com",
    isUser: false
)
```

## Topics

### Creating the participant representation
- [init(name: String, handle: String, isUser: Bool)](suggestedactionsmessage/participant/init(name:handle:isuser:).md)
  Creates a participant in a conversation.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [init(id: some Hashable, date: Date, subject: AttributedString?, body: AttributedString, sender: SuggestedActionsMessage.Participant, recipients: [SuggestedActionsMessage.Participant])](suggestedactionsmessage/init(id:date:subject:body:sender:recipients:).md)
  Creates a representation of a message that the system uses to display suggested actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/suggestedactions/suggestedactionsmessage/participant)*