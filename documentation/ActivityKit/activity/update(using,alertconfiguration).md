# update(using:alertConfiguration:)

**Framework**: ActivityKit  
**Kind**: method  
**Role**: Instance Method

Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.

**Availability**:
- iOS 16.1+ - Deprecated in 16.2
- iPadOS 16.1+ - Deprecated in 16.2

> **Deprecated**: Use update(_:alertConfiguration:) instead

## Declaration

```swift
func update(using contentState: Activity<Attributes>.ContentState, alertConfiguration: AlertConfiguration? = nil) async
```

#### Discussion

The system ignores updates to a Live Activity that’s in the [`ActivityState.ended`](../activitystate/ended.md) state.

## Parameters

- `contentState`: The updated dynamic content for the Live Activity. The size of the encoded content can’t exceed 4KB in size.
- `alertConfiguration`: The alert configuration you use to configure how the system notifies a person about the updated content of the Live Activity.

## See Also

### Deprecated
- [static func request(attributes: Attributes, contentState: Activity<Attributes>.ContentState, pushType: PushType?) throws -> Activity<Attributes>](./request%28attributes,contentstate,pushtype%29.md)
  Requests and starts a Live Activity.
- [func update(using: Activity<Attributes>.ContentState) async](./update%28using%29.md)
  Updates the dynamic content of the Live Activity.
- [func end(using: Activity<Attributes>.ContentState?, dismissalPolicy: ActivityUIDismissalPolicy) async](./end%28using,dismissalpolicy%29.md)
  Ends an active Live Activity.
- [var contentState: Activity<Attributes>.ContentState](./contentstate-swift.property.md)
  The dynamic content of a Live Activity.
- [var contentStateUpdates: Activity<Attributes>.ContentStateUpdates](./contentstateupdates-swift.property.md)
  An asynchronous sequence you use to observe changes to the dynamic content of a Live Activity.
- [Activity.ContentStateUpdates](./contentstateupdates-swift.struct.md)
  A structure that offers functionality to observe changes to the dynamic content of a Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/update(using:alertconfiguration:))*