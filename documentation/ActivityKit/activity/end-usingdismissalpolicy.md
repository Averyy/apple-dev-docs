# end(using:dismissalPolicy:)

**Framework**: ActivityKit  
**Kind**: method

Ends an active Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
func end(using contentState: Activity<Attributes>.ContentState? = nil, dismissalPolicy: ActivityUIDismissalPolicy = .default) async
```

#### Discussion

End an active Live Activity while your app is in the foreground or while it’s in the background — for example, by using [`Background Tasks`](https://developer.apple.com/documentation/BackgroundTasks).

Include updated data in the `contentState` parameter to ensure the Live Activity shows the latest and final content update after it ends. This is important because the Live Activity remains visible until the system or the person removes it.

## Parameters

- `contentState`: The latest and final dynamic content for the Live Activity that ended.   The size of the encoded content can’t exceed 4KB in size.
- `dismissalPolicy`: Describes how and when the system should dismiss a Live Activity and   and remove it from the Lock Screen.

## See Also

- [static func request(attributes: Attributes, contentState: Activity<Attributes>.ContentState, pushType: PushType?) throws -> Activity<Attributes>](activity/request(attributes:contentstate:pushtype:).md)
  Requests and starts a Live Activity.
- [func update(using: Activity<Attributes>.ContentState) async](activity/update(using:).md)
  Updates the dynamic content of the Live Activity.
- [func update(using: Activity<Attributes>.ContentState, alertConfiguration: AlertConfiguration?) async](activity/update(using:alertconfiguration:).md)
  Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
- [var contentState: Activity<Attributes>.ContentState](activity/contentstate-swift.property.md)
  The dynamic content of a Live Activity.
- [var contentStateUpdates: Activity<Attributes>.ContentStateUpdates](activity/contentstateupdates-swift.property.md)
  An asynchronous sequence you use to observe changes to the dynamic content of a Live Activity.
- [Activity.ContentStateUpdates](activity/contentstateupdates-swift.struct.md)
  A structure that offers functionality to observe changes to the dynamic content of a Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/end(using:dismissalpolicy:))*