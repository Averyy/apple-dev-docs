# remoteParticipantIdentifiers

**Framework**: Messages  
**Kind**: property  
**Role**: Instance Property

An array of UUIDs representing the remote participants in this conversation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var remoteParticipantIdentifiers: [UUID] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSUUID *> * remoteParticipantIdentifiers;
```

#### Discussion

These UUIDs are scoped to this device. They remain stable as long as the extension is enabled. If the extension is disabled and reenabled, or if the containing app is removed and reinstalled, the UUIDs for remote participants change.

## See Also

### Accessing Participants
- [var localParticipantIdentifier: UUID](./localparticipantidentifier.md)
  A UUID that identifies the user on this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msconversation/remoteparticipantidentifiers)*