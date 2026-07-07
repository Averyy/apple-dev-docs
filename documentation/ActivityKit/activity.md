# Activity

**Framework**: ActivityKit  
**Kind**: class

The object you use to start, update, and end a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
class Activity<Attributes> where Attributes : ActivityAttributes
```

## Mentions

- [Displaying live data with Live Activities](displaying-live-data-with-live-activities.md)

#### Overview

The `Activity` object offers functionality to start, update, and end a Live Activity from within your app. You can update or end a Live Activity while your app is in the background, but you can only start a Live Activity while the app is in the foreground, unless you adopt [`App Intents`](https://developer.apple.com/documentation/AppIntents) and start the Live Activity using a [`LiveActivityIntent`](https://developer.apple.com/documentation/AppIntents/LiveActivityIntent).

Additionally, `Activity` offers functionality to observe changes to:

- The Live Activity
- The Live Activity’s state in its life cycle
- A person’s permission to start Live Activities
- The Live Activity’s push token if you configure it to receive updates through ActivityKit push notifications.

To observe these changes, use the asynchronous sequences the activity object offers; for example, use the [`activityStateUpdates`](activity/activitystateupdates-swift.property.md) sequence to observe changes to the state of a Live Activity.

## Topics

### Starting a Live Activity
- [static func request(attributes: Attributes, content: ActivityContent<Activity<Attributes>.ContentState>, pushType: PushType?) throws -> Activity<Attributes>](activity/request(attributes:content:pushtype:).md)
  Requests and starts a standard Live Activity.
- [static func request(attributes: Attributes, content: ActivityContent<Activity<Attributes>.ContentState>, pushType: PushType?, style: ActivityStyle) throws -> Activity<Attributes>](activity/request(attributes:content:pushtype:style:).md)
  Requests and starts a Live Activity.
- [static func request(attributes: Attributes, content: ActivityContent<Activity<Attributes>.ContentState>, pushType: PushType?, style: ActivityStyle, alertConfiguration: AlertConfiguration, start: Date) throws -> Activity<Attributes>](activity/request(attributes:content:pushtype:style:alertconfiguration:start:).md)
  Requests and schedules a Live Activity for a specific date.
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
### Updating a Live Activity
- [func update(ActivityContent<Activity<Attributes>.ContentState>) async](activity/update(_:).md)
  Updates the dynamic content of the Live Activity.
- [func update(ActivityContent<Activity<Attributes>.ContentState>, alertConfiguration: AlertConfiguration?) async](activity/update(_:alertconfiguration:).md)
  Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
- [struct AlertConfiguration](alertconfiguration.md)
  A structure you use to configure an alert that appears when you update your Live Activity.
- [func update(ActivityContent<Activity<Attributes>.ContentState>, alertConfiguration: AlertConfiguration?, timestamp: Date) async](activity/update(_:alertconfiguration:timestamp:).md)
  Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
### Ending a Live Activity
- [func end(ActivityContent<Activity<Attributes>.ContentState>?, dismissalPolicy: ActivityUIDismissalPolicy) async](activity/end(_:dismissalpolicy:).md)
  Ends an active Live Activity.
- [struct ActivityUIDismissalPolicy](activityuidismissalpolicy.md)
  The structure that describes when the system should remove a Live Activity that ended.
- [func end(ActivityContent<Activity<Attributes>.ContentState>?, dismissalPolicy: ActivityUIDismissalPolicy, timestamp: Date) async](activity/end(_:dismissalpolicy:timestamp:).md)
  Ends an active Live Activity.
### Observing Live Activity content changes
- [var contentUpdates: Activity<Attributes>.ContentUpdates](activity/contentupdates-swift.property.md)
  An asynchronous sequence you use to observe changes to the dynamic content of a Live Activity.
- [Activity.ContentUpdates](activity/contentupdates-swift.struct.md)
  A structure that offers functionality to observe changes to the dynamic content of a Live Activity.
### Observing the Live Activity life cycle
- [var activityState: ActivityState](activity/activitystate.md)
  The current state of a Live Activity in its life cycle.
- [enum ActivityState](activitystate.md)
  The enum that describes the state of a Live Activity in its life cycle.
- [var activityStateUpdates: Activity<Attributes>.ActivityStateUpdates](activity/activitystateupdates-swift.property.md)
  An asynchronous sequence you use to observe activity state changes.
- [Activity.ActivityStateUpdates](activity/activitystateupdates-swift.struct.md)
  A structure that offers functionality to observe state changes of a Live Activity.
### Using ActivityKit push notifications
- [var pushToken: Data?](activity/pushtoken.md)
  The token you use to send ActivityKit push notifications to a Live Activity.
- [var pushTokenUpdates: Activity<Attributes>.PushTokenUpdates](activity/pushtokenupdates-swift.property.md)
  An asynchronous sequence you use to observe changes to the push token of a Live Activity.
- [Activity.PushTokenUpdates](activity/pushtokenupdates-swift.struct.md)
  A structure that offers functionality to observe changes to the push token of a Live Activity.
- [static var pushToStartToken: Data?](activity/pushtostarttoken.md)
  The token you use to start a Live Activity with an ActivityKit push notification.
- [static var pushToStartTokenUpdates: Activity<Attributes>.PushTokenUpdates](activity/pushtostarttokenupdates.md)
  An asynchronous sequence you use to observe changes to the token for starting a Live Activity with an ActivityKit push notification.
### Checking user authorization
- [class ActivityAuthorizationInfo](activityauthorizationinfo.md)
  An object with information about whether a person allowed your app to start Live Activities and permitted content updates with frequent ActivityKit push notifications.
### Accessing Live Activities
- [static var activities: [Activity<Attributes>]](activity/activities.md)
  An array of your app’s current Live Activities.
- [static var activityUpdates: Activity<Attributes>.ActivityUpdates](activity/activityupdates-swift.type.property.md)
  An asynchronous sequence you use to observe changes to ongoing Live Activities and to asynchronously access a Live Activity when you start it.
- [Activity.ActivityUpdates](activity/activityupdates-swift.struct.md)
  A structure that offers functionality to observe changes to a Live Activity.
### Identifying a Live Activity
- [let id: String](activity/id.md)
  A unique identifier for a Live Activity.
- [let id: String](activity/id.md)
  A unique identifier for a Live Activity.
### Deprecated
- [Deprecated symbols](deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [Displaying live data with Live Activities](displaying-live-data-with-live-activities.md)
  Display up-to-date data and offer quick interactions in the Dynamic Island, on the Lock Screen, in CarPlay, and on a paired Mac or Apple Watch.
- [Starting and updating Live Activities with ActivityKit push notifications](starting-and-updating-live-activities-with-activitykit-push-notifications.md)
  Use ActivityKit to receive push tokens and to remotely start, update, and end your Live Activity with ActivityKit notifications.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](../WidgetKit/emoji-rangers-supporting-live-activities-interactivity-and-animations.md)
  Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- [NSSupportsLiveActivities](../BundleResources/Information-Property-List/NSSupportsLiveActivities.md)
  A Boolean value that indicates whether an app supports Live Activities.
- [NSSupportsLiveActivitiesFrequentUpdates](../BundleResources/Information-Property-List/NSSupportsLiveActivitiesFrequentUpdates.md)
  A Boolean value that indicates whether an app can update its Live Activities frequently.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity)*