# contentState

**Framework**: ActivityKit  
**Kind**: property

The dynamic content of a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
var contentState: Activity<Attributes>.ContentState { get }
```

## See Also

- [static func request(attributes: Attributes, contentState: Activity<Attributes>.ContentState, pushType: PushType?) throws -> Activity<Attributes>](activity/request(attributes:contentstate:pushtype:).md)
  Requests and starts a Live Activity.
- [func update(using: Activity<Attributes>.ContentState) async](activity/update(using:).md)
  Updates the dynamic content of the Live Activity.
- [func update(using: Activity<Attributes>.ContentState, alertConfiguration: AlertConfiguration?) async](activity/update(using:alertconfiguration:).md)
  Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
- [func end(using: Activity<Attributes>.ContentState?, dismissalPolicy: ActivityUIDismissalPolicy) async](activity/end(using:dismissalpolicy:).md)
  Ends an active Live Activity.
- [var contentStateUpdates: Activity<Attributes>.ContentStateUpdates](activity/contentstateupdates-swift.property.md)
  An asynchronous sequence you use to observe changes to the dynamic content of a Live Activity.
- [Activity.ContentStateUpdates](activity/contentstateupdates-swift.struct.md)
  A structure that offers functionality to observe changes to the dynamic content of a Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/contentstate-swift.property)*