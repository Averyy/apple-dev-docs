# PTPushResult

**Framework**: Push to Talk  
**Kind**: class

An object that represents a push result.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
class PTPushResult
```

## Mentions

- [Creating a Push to Talk app](creating-a-push-to-talk-app.md)

#### Overview

When an app receives an Apple Push Notification service payload, return a [`PTPushResult`](ptpushresult.md) object as part of the delegate method. Use [`activeRemoteParticipant(_:)`](ptpushresult/activeremoteparticipant(_:).md) to show the latest participant information in the system user interface. Create a push result with [`leaveChannel`](ptpushresult/leavechannel.md) to remove a user from the channel.

```swift
func incomingPushResult(channelManager: PTChannelManager,
                        channelUUID: UUID,
                        pushPayload: [String: Any]) -> PTPushResult {
    guard let activeSpeaker = pushPayload["activeSpeaker"] as? String else {
        // Report that there's no active speaker, so leave the channel.
        return .leaveChannel
    }

    let activeSpeakerImage = // Get the cached image for the active speaker.
    let participant = PTParticipant(name: activeSpeaker,
                                    image: activeSpeakerImage)
    // Report the active participant information to the system.
    return .activeRemoteParticipant(participant)
}
```

## Topics

### Updating the active participant
- [class func activeRemoteParticipant(PTParticipant) -> PTPushResult](ptpushresult/activeremoteparticipant(_:).md)
  Creates a push result for reporting that a remote participant started to speak.
### Leaving the channel
- [class var leaveChannel: PTPushResult](ptpushresult/leavechannel.md)
  Creates a push result for leaving a channel.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptpushresult)*