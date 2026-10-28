# localParticipant

**Framework**: Group Activities  
**Kind**: property  
**Role**: Instance Property

The participant on the current device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
final var localParticipant: Participant { get }
```

## Discussion

Use this property to differentiate the participant on the current device from participants on other devices.

## See Also

### Getting the participants
- [var activeParticipants: Set<Participant>](./activeparticipants.md)
  The set of participants currently engaged in the activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/localparticipant)*