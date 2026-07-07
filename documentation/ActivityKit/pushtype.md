# PushType

**Framework**: ActivityKit  
**Kind**: struct

The structure that offers constants you use to configure a Live Activity to receive updates through ActivityKit push notifications.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
struct PushType
```

#### Overview

Pass the [`token`](pushtype/token.md) constant to the [`request(attributes:contentState:pushType:)`](activity/request(attributes:contentstate:pushtype:).md) function to start a Live Activity that receives content updates with ActivityKit push notifications. Pass [`channel(_:)`](pushtype/channel(_:).md) to [`request(attributes:contentState:pushType:)`](activity/request(attributes:contentstate:pushtype:).md) function to specify that you want to use a broadcast channel instead of a token. You can only specify one [`PushType`](pushtype.md).

To learn more about using ActivityKit push notifications to update your Live Activity, see [`Starting and updating Live Activities with ActivityKit push notifications`](starting-and-updating-live-activities-with-activitykit-push-notifications.md).

## Topics

### Supporting ActivityKit push notifications
- [static var token: PushType](pushtype/token.md)
  A constant you use to configure a Live Activity that updates its dynamic content by receiving ActivityKit push notifications.
- [static func channel(String) -> PushType](pushtype/channel(_:).md)
  A constant to configure a Live Activity that updates its dynamic content for broadcast channels.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

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
- [enum ActivityAuthorizationError](activityauthorizationerror.md)
  An error that indicates why the request to start a Live Activity failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/pushtype)*