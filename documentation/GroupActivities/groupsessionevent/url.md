# url

**Framework**: Group Activities  
**Kind**: property

The URL to open when the participant taps the event link in the system UI.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
let url: URL?
```

#### Discussion

When the user taps your custom event in the system UI, the system opens the provided URL. Specify a universal link to open your app to the place where the action occurred. If the value of this link is `nil`, the system brings your app to the foreground.

For information about how to support universal links in your app, see [`Supporting universal links in your app`](https://developer.apple.com/documentation/Xcode/supporting-universal-links-in-your-app)

## See Also

- [let originator: Participant](groupsessionevent/originator.md)
  The participant that initiated the event.
- [let action: GroupSessionEvent.Action](groupsessionevent/action-swift.property.md)
  The reason for the event.
- [GroupSessionEvent.Action](groupsessionevent/action-swift.struct.md)
  A playback-related change that occurs during the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionevent/url)*