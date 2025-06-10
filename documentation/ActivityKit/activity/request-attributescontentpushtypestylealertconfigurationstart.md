# request(attributes:content:pushType:style:alertConfiguration:start:)

**Framework**: ActivityKit  
**Kind**: method

Requests and schedules a Live Activity for a specific date.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
static func request(attributes: Attributes, content: ActivityContent<Activity<Attributes>.ContentState>, pushType: PushType? = nil, style: ActivityStyle, alertConfiguration: AlertConfiguration, start: Date) throws -> Activity<Attributes>
```

#### Return Value

The object that represents the Live Activity you started.

#### Discussion

Use this function to request Live Activity from your app while it’s in the foreground. Note that you can’t request a Live Activity while your app is in the background. The system starts the Live Activity at the specified date, even if the app is in the background. Note that you must provide an [`AlertConfiguration`](alertconfiguration.md). This makes sure that the system notifies people when your app starts the Live Activity.

> **Note**: The system limits the number of simultaneous ongoing Live Activities. Scheduled Live Activities count towards this limit.

If your Live Activity displays image assets, the system requires them to use a resolution that’s smaller or equal to the size of the Live Activity presentation for a device. If you use an image asset that’s larger than the size of the Live Activity presentation, the system may fail to start the Live Activity. For information about the sizes of Live Activity presentations, see [`Human Interface Guidelines > Live Activities`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities).

For additional information on starting a Live Activity, see [`Displaying live data with Live Activities`](displaying-live-data-with-live-activities.md).

> **Note**: [`ActivityAuthorizationError`](activityauthorizationerror.md) if the app can’t start a new Live Activity. For example, [`ActivityAuthorizationError.denied`](activityauthorizationerror/denied.md) indicates that the person deactivated Live Activities for the app.

## Parameters

- `attributes`: A set of attributes that describe the Live Activity and its static content.
- `content`: A structure that describes the dynamic content of the Live Activity that changes over time.
- `pushType`: A value that indicates whether the Live Activity receives updates to its dynamic   content with ActivityKit push notifications. Pass   to start a Live Activity that only receives   updates from the app with the   function.   To start a Live Activity that receives updates to its dynamic content with ActivityKit push notifications in   addition to the   function, pass   to this parameter.
- `style`: A flag that indicates whether the Live Activity uses standard or transient behavior. For most apps, passing    is the best choice. It starts a standard Live Activity that continues until the app, a push notification, or a person ends it,   or until it exceeds the maximum duration for Live Activities.   By passing  , you start a Live Activity that appears in the extended presentation in the Dynamic Island   but ends automatically when a person automatically locks the device, collapses the extended presentation, leaves the app,   or performs other tasks outside the Dynamic Island.
- `alertConfiguration`: The alert configuration you use to configure how the system notifies   a person about the updated content of the Live Activity.
- `start`: The date to schedule the start of your Live Activity; for example, for an upcoming sports game. You must provide   an   to let people know that your app started a Live Activity. The   for a scheduled   but not yet started Live Activity is  .

## See Also

- [static func request(attributes: Attributes, content: ActivityContent<Activity<Attributes>.ContentState>, pushType: PushType?) throws -> Activity<Attributes>](activity/request(attributes:content:pushtype:).md)
  Requests and starts a standard Live Activity.
- [static func request(attributes: Attributes, content: ActivityContent<Activity<Attributes>.ContentState>, pushType: PushType?, style: ActivityStyle) throws -> Activity<Attributes>](activity/request(attributes:content:pushtype:style:).md)
  Requests and starts a Live Activity.
- [static func request(attributes: Attributes, content: ActivityContent<Activity<Attributes>.ContentState>, pushType: PushType?, style: ActivityStyle, alertConfiguration: AlertConfiguration, startDate: Date) throws -> Activity<Attributes>](activity/request(attributes:content:pushtype:style:alertconfiguration:startdate:).md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/request(attributes:content:pushtype:style:alertconfiguration:start:))*