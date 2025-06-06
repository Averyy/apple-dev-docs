# lifetimePolicy

**Framework**: Group Activities  
**Kind**: property

Determines how an activity can be ended.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var lifetimePolicy: GroupActivityMetadata.LifetimePolicy
```

#### Discussion

Most activities can be left or ended independently by any participant. For example, a game being played together or a TV show being watched together doesn’t depend on a particular participant to be able to continue for everyone else.

Some activities, though, might depend on the initiator’s presence in the activity for it to continue.  For example, the initiator might be sharing a photo that belongs to them, or a file from their device.  Setting [`lifetimePolicy`](groupactivitymetadata/lifetimepolicy-swift.property.md) to [`endsWhenInitiatorLeaves`](groupactivitymetadata/lifetimepolicy-swift.struct/endswheninitiatorleaves.md) in these cases would ensure that the activity ends when the initiator leaves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitymetadata/lifetimepolicy-swift.property)*