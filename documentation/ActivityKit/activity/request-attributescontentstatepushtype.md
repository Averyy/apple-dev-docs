# request(attributes:contentState:pushType:)

**Framework**: ActivityKit  
**Kind**: method

Requests and starts a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
static func request(attributes: Attributes, contentState: Activity<Attributes>.ContentState, pushType: PushType? = nil) throws -> Activity<Attributes>
```

#### Return Value

The object that represents the started Live Activity.

#### Discussion

Use this function to request and start a Live Activity from your app while it’s in the foreground. Note that you can’t do this while your app is in the background, unless you adopt [`App Intents`](https://developer.apple.com/documentation/AppIntents) and start the Live Activity using a [`LiveActivityIntent`](https://developer.apple.com/documentation/AppIntents/LiveActivityIntent).

If your Live Activity displays image assets, the system requires them to use a resolution that’s smaller or equal to the size of the Live Activity presentation for a device. If you use an image asset that’s larger than the size of the Live Activity presentation, the system may fail to start the Live Activity. For information about the sizes of Live Activity presentations, see [`Human Interface Guidelines > Live Activities`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities).

For additional information on starting a Live Activity, see [`Displaying live data with Live Activities`](displaying-live-data-with-live-activities.md).

> **Note**: [`ActivityAuthorizationError`](activityauthorizationerror.md) if the app can’t start a new Live Activity. For example, [`ActivityAuthorizationError.denied`](activityauthorizationerror/denied.md) indicates that a person deactivated Live Activities for the app.

## Parameters

- `attributes`: A set of attributes that describe the Live Activity and its static content.
- `contentState`: A structure that describes the dynamic content of the Live Activity that changes over time.
- `pushType`: A value that indicates whether the Live Activity receives updates to its dynamic   content with ActivityKit push notifications. Pass   to start a Live Activity that only receives   updates from the app with the   function.   To start a Live Activity that receives updates to its dynamic content with ActivityKit push   notifications in addition to the   function, pass    to this parameter.

## See Also

- [func update(using: Activity<Attributes>.ContentState) async](activity/update(using:).md)
  Updates the dynamic content of the Live Activity.
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

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/request(attributes:contentstate:pushtype:))*