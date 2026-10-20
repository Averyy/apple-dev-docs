# contentStateUpdates

**Framework**: ActivityKit  
**Kind**: property  
**Role**: Instance Property

An asynchronous sequence you use to observe changes to the dynamic content of a Live Activity.

**Availability**:
- iOS 16.1+ - Deprecated in 16.2
- iPadOS 16.1+ - Deprecated in 16.2

> **Deprecated**: Use contentUpdates instead

## Declaration

```swift
var contentStateUpdates: Activity<Attributes>.ContentStateUpdates { get }
```

## See Also

### Deprecated
- [static func request(attributes: Attributes, contentState: Activity<Attributes>.ContentState, pushType: PushType?) throws -> Activity<Attributes>](./request%28attributes,contentstate,pushtype%29.md)
  Requests and starts a Live Activity.
- [func update(using: Activity<Attributes>.ContentState) async](./update%28using%29.md)
  Updates the dynamic content of the Live Activity.
- [func update(using: Activity<Attributes>.ContentState, alertConfiguration: AlertConfiguration?) async](./update%28using,alertconfiguration%29.md)
  Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
- [func end(using: Activity<Attributes>.ContentState?, dismissalPolicy: ActivityUIDismissalPolicy) async](./end%28using,dismissalpolicy%29.md)
  Ends an active Live Activity.
- [var contentState: Activity<Attributes>.ContentState](./contentstate-swift.property.md)
  The dynamic content of a Live Activity.
- [Activity.ContentStateUpdates](./contentstateupdates-swift.struct.md)
  A structure that offers functionality to observe changes to the dynamic content of a Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/contentstateupdates-swift.property)*