# url

**Framework**: Group Activities  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

When the user taps your custom event in the system UI, the system opens the provided URL. Specify a universal link to open your app to the place where the action occurred. If the value of this link is `nil`, the system brings your app to the foreground.

For information about how to support universal links in your app, see [Supporting universal links in your app](../../Xcode/supporting-universal-links-in-your-app.md)

## See Also

### Getting the event details
- [let originator: Participant](./originator.md)
  The participant that initiated the event.
- [let action: GroupSessionEvent.Action](./action-swift.property.md)
  The reason for the event.
- [GroupSessionEvent.Action](./action-swift.struct.md)
  A playback-related change that occurs during the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionevent/url)*