# seek

**Framework**: Group Activities  
**Kind**: property  
**Role**: Type Property

An event that indicates a change to the current playback location.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static let seek: GroupSessionEvent.Action
```

## See Also

### Getting playback-related actions
- [static let play: GroupSessionEvent.Action](./play.md)
  An action that indicates the start of playback.
- [static let pause: GroupSessionEvent.Action](./pause.md)
  An action that indicates an end to playback.
- [static func skip(item: String) -> GroupSessionEvent.Action](./skip%28item%29.md)
  Returns an event that indicates a skipped track or playback item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionevent/action-swift.struct/seek)*