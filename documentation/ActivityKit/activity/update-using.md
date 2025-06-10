# update(using:)

**Framework**: ActivityKit  
**Kind**: method

Updates the dynamic content of the Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
func update(using contentState: Activity<Attributes>.ContentState) async
```

#### Discussion

Use this function to update the Live Activity while your app is in the foreground or while it’s in the background — for example, by using [`Background Tasks`](https://developer.apple.com/documentation/BackgroundTasks).

> **Note**: The system ignores attempts to update a Live Activity that ended.

## Parameters

- `contentState`: The updated dynamic content for the Live Activity. The size of   the encoded content can’t exceed 4KB in size.

## See Also

- [static func request(attributes: Attributes, contentState: Activity<Attributes>.ContentState, pushType: PushType?) throws -> Activity<Attributes>](activity/request(attributes:contentstate:pushtype:).md)
  Requests and starts a Live Activity.
- [func update(using: Activity<Attributes>.ContentState, alertConfiguration: AlertConfiguration?) async](activity/update(using:alertconfiguration:).md)
  Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
- [func end(using: Activity<Attributes>.ContentState?, dismissalPolicy: ActivityUIDismissalPolicy) async](activity/end(using:dismissalpolicy:).md)
  Ends an active Live Activity.
- [var contentState: Activity<Attributes>.ContentState](activity/contentstate-swift.property.md)
  The dynamic content of a Live Activity.
- [var contentStateUpdates: Activity<Attributes>.ContentStateUpdates](activity/contentstateupdates-swift.property.md)
  An asynchronous sequence you use to observe changes to the dynamic content of a Live Activity.
- [Activity.ContentStateUpdates](activity/contentstateupdates-swift.struct.md)
  A structure that offers functionality to observe changes to the dynamic content of a Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/update(using:))*