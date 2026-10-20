# content

**Framework**: ActivityKit  
**Kind**: property  
**Role**: Instance Property

The dynamic content of a Live Activity.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+

## Declaration

```swift
var content: ActivityContent<Activity<Attributes>.ContentState> { get }
```

## See Also

### Starting a Live Activity
- [static func request(attributes: Attributes, content: ActivityContent<Activity<Attributes>.ContentState>, pushType: PushType?) throws -> Activity<Attributes>](./request%28attributes,content,pushtype%29.md)
  Requests and starts a standard Live Activity.
- [static func request(attributes: Attributes, content: ActivityContent<Activity<Attributes>.ContentState>, pushType: PushType?, style: ActivityStyle) throws -> Activity<Attributes>](./request%28attributes,content,pushtype,style%29.md)
  Requests and starts a Live Activity.
- [static func request(attributes: Attributes, content: ActivityContent<Activity<Attributes>.ContentState>, pushType: PushType?, style: ActivityStyle, alertConfiguration: AlertConfiguration, start: Date) throws -> Activity<Attributes>](./request%28attributes,content,pushtype,style,alertconfiguration,start%29.md)
  Requests and schedules a Live Activity for a specific date.
- [static func request(attributes: Attributes, content: ActivityContent<Activity<Attributes>.ContentState>, pushType: PushType?, style: ActivityStyle, alertConfiguration: AlertConfiguration, startDate: Date) throws -> Activity<Attributes>](./request%28attributes,content,pushtype,style,alertconfiguration,startdate%29.md)
- [let attributes: Attributes](./attributes.md)
  A set of attributes that describe a Live Activity and its content.
- [protocol ActivityAttributes](../activityattributes.md)
  The protocol you implement to describe the content of a Live Activity.
- [enum ActivityStyle](../activitystyle.md)
- [struct ActivityContent](../activitycontent.md)
  A structure that describes the state and configuration of a Live Activity.
- [typealias ContentState](./contentstate-swift.typealias.md)
  The type alias for the structure that describes the dynamic content of a Live Activity.
- [struct PushType](../pushtype.md)
  The structure that offers constants you use to configure a Live Activity to receive updates through ActivityKit push notifications.
- [enum ActivityAuthorizationError](../activityauthorizationerror.md)
  An error that indicates why the request to start a Live Activity failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/content)*