# request(attributes:content:pushType:)

**Framework**: Activitykit  
**Kind**: method

Requests and starts a Live Activity.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+

## Declaration

```swift
static func request(attributes: Attributes, content: ActivityContent<Activity<Attributes>.ContentState>, pushType: PushType? = nil) throws -> Activity<Attributes>
```

## Mentions

- [Starting and updating Live Activities with ActivityKit push notifications](starting-and-updating-live-activities-with-activitykit-push-notifications.md)
- [Displaying live data with Live Activities](displaying-live-data-with-live-activities.md)

#### Return Value

The object that represents the Live Activity you started.

#### Discussion

Use this function to request and start a Live Activity from your app while it’s in the foreground. Note that you can’t do this while your app is in the background.

If your Live Activity displays image assets, the system requires them to use a resolution that’s smaller or equal to the size of the Live Activity presentation for a device. If you use an image asset that’s larger than the size of the Live Activity presentation, the system may fail to start the Live Activity. For information about the sizes of Live Activity presentations, see [`Human Interface Guidelines > Live Activities`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities).

For additional information on starting a Live Activity, see [`Displaying live data with Live Activities`](displaying-live-data-with-live-activities.md).

> **Note**: [`ActivityAuthorizationError`](activityauthorizationerror.md) if the app can’t start a new Live Activity. For example, [`ActivityAuthorizationError.denied`](activityauthorizationerror/denied.md) indicates that the person deactivated Live Activities for the app.

## Parameters

- `attributes`: A set of attributes that describe the Live Activity and its static content.
- `content`: A structure that describes the dynamic content of the Live Activity that changes over time.
- `pushType`: A value that indicates whether the Live Activity receives updates to its dynamic   content with ActivityKit push notifications. Pass   to start a Live Activity that only receives   updates from the app with the   function.   To start a Live Activity that receives updates to its dynamic content with ActivityKit push notifications in   addition to the   function, pass   to this parameter.

## See Also

- [let attributes: Attributes](activity/attributes.md)
  A set of attributes that describe a Live Activity and its content.
- [protocol ActivityAttributes](activityattributes.md)
  The protocol you implement to describe the content of a Live Activity.
- [enum ActivityStyle](activitystyle.md)
- [var content: ActivityContent<Activity<Attributes>.ContentState>](activity/content.md)
  The dynamic content of a Live Activity.
- [struct ActivityContent](activitycontent.md)
  A structure that describes the state and configuration of a Live Activity.
- [typealias ContentState](activity/contentstate-swift.typealias.md)
  The type alias for the structure that describes the dynamic content of a Live Activity.
- [struct PushType](pushtype.md)
  The structure that offers constants you use to configure a Live Activity to receive updates through ActivityKit push notifications.
- [enum ActivityAuthorizationError](activityauthorizationerror.md)
  An error that indicates why the request to start a Live Activity failed.
- [static func request(attributes: Attributes, content: ActivityContent<Activity<Attributes>.ContentState>, pushType: PushType?, style: ActivityStyle) throws -> Activity<Attributes>](activity/request(attributes:content:pushtype:style:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/request(attributes:content:pushtype:))*