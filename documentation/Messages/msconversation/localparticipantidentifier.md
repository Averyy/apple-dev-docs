# localParticipantIdentifier

**Framework**: Messages  
**Kind**: property

A UUID that identifies the user on this device.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var localParticipantIdentifier: UUID { get }
```

#### Discussion

This UUID is scoped to this device. It remains stable as long as the extension is enabled. If the extension is disabled and reenabled, or if the containing app is removed and reinstalled, the UUID for the local participant changes.

## See Also

- [var remoteParticipantIdentifiers: [UUID]](msconversation/remoteparticipantidentifiers.md)
  An array of UUIDs representing the remote participants in this conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msconversation/localparticipantidentifier)*