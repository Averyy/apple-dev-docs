# Deprecated symbols

**Framework**: ActivityKit  
**Role**: API Collection

Review unsupported symbols and their replacements.

## Topics

### Deprecated
- [static func request(attributes: Attributes, contentState: Activity<Attributes>.ContentState, pushType: PushType?) throws -> Activity<Attributes>](./activity/request%28attributes,contentstate,pushtype%29.md)
  Requests and starts a Live Activity.
- [func update(using: Activity<Attributes>.ContentState) async](./activity/update%28using%29.md)
  Updates the dynamic content of the Live Activity.
- [func update(using: Activity<Attributes>.ContentState, alertConfiguration: AlertConfiguration?) async](./activity/update%28using,alertconfiguration%29.md)
  Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
- [func end(using: Activity<Attributes>.ContentState?, dismissalPolicy: ActivityUIDismissalPolicy) async](./activity/end%28using,dismissalpolicy%29.md)
  Ends an active Live Activity.
- [var contentState: Activity<Attributes>.ContentState](./activity/contentstate-swift.property.md)
  The dynamic content of a Live Activity.
- [var contentStateUpdates: Activity<Attributes>.ContentStateUpdates](./activity/contentstateupdates-swift.property.md)
  An asynchronous sequence you use to observe changes to the dynamic content of a Live Activity.
- [Activity.ContentStateUpdates](./activity/contentstateupdates-swift.struct.md)
  A structure that offers functionality to observe changes to the dynamic content of a Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/deprecated-symbols)*