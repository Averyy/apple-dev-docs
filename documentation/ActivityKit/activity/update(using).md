# update(using:)

**Framework**: ActivityKit  
**Kind**: method  
**Role**: Instance Method

Updates the dynamic content of the Live Activity.

**Availability**:
- iOS 16.1+ - Deprecated in 16.2
- iPadOS 16.1+ - Deprecated in 16.2

> **Deprecated**: Use update(_:) instead

## Declaration

```swift
func update(using contentState: Activity<Attributes>.ContentState) async
```

## Discussion

Use this function to update the Live Activity while your app is in the foreground or while it’s in the background — for example, by using [Background Tasks](../../BackgroundTasks/BackgroundTasks.md).

> **Note**: The system ignores attempts to update a Live Activity that ended.

## Parameters

- `contentState`: The updated dynamic content for the Live Activity. The size of the encoded content can’t exceed 4KB in size.

## See Also

### Deprecated
- [static func request(attributes: Attributes, contentState: Activity<Attributes>.ContentState, pushType: PushType?) throws -> Activity<Attributes>](./request%28attributes,contentstate,pushtype%29.md)
  Requests and starts a Live Activity.
- [func update(using: Activity<Attributes>.ContentState, alertConfiguration: AlertConfiguration?) async](./update%28using,alertconfiguration%29.md)
  Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
- [func end(using: Activity<Attributes>.ContentState?, dismissalPolicy: ActivityUIDismissalPolicy) async](./end%28using,dismissalpolicy%29.md)
  Ends an active Live Activity.
- [var contentState: Activity<Attributes>.ContentState](./contentstate-swift.property.md)
  The dynamic content of a Live Activity.
- [var contentStateUpdates: Activity<Attributes>.ContentStateUpdates](./contentstateupdates-swift.property.md)
  An asynchronous sequence you use to observe changes to the dynamic content of a Live Activity.
- [Activity.ContentStateUpdates](./contentstateupdates-swift.struct.md)
  A structure that offers functionality to observe changes to the dynamic content of a Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/update(using:))*