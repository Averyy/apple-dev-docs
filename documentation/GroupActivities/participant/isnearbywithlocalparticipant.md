# isNearbyWithLocalParticipant

**Framework**: Group Activities  
**Kind**: property

A Boolean value that indicates whether the participant is physically nearby with the local participant.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var isNearbyWithLocalParticipant: Bool { get }
```

## Mentions

- [Configure your visionOS app for sharing with people nearby](configure-your-app-for-sharing-with-people-nearby.md)

#### Discussion

This property is always true for the local participant.

You can observe which remote participants are nearby with the [`$activeParticipants`](groupsession/$activeparticipants.md) publisher.

```swift
for await activeParticipants in session.$activeParticipants.values {
    // Ignore the local participant value that defaults to 'true'.
    self.isNearbyWithOthers = activeParticipants.contains {
         $0 != session.localParticipant && $0.isNearbyWithLocalParticipant
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/participant/isnearbywithlocalparticipant)*