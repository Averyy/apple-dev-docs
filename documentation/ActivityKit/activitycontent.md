# ActivityContent

**Framework**: ActivityKit  
**Kind**: struct

A structure that describes the state and configuration of a Live Activity.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+

## Declaration

```swift
struct ActivityContent<State> where State : Decodable, State : Encodable, State : Hashable
```

## Mentions

- [Displaying live data with Live Activities](displaying-live-data-with-live-activities.md)

## Topics

### Describing a Live Activity
- [init(state: State, staleDate: Date?, relevanceScore: Double)](activitycontent/init(state:staledate:relevancescore:).md)
  Creates the object that describes the state and configuration of a Live Activity.
- [let state: State](activitycontent/state.md)
  The current state of a Live Activity in its life cycle.
- [let staleDate: Date?](activitycontent/staledate.md)
  The date when the system considers the Live Activity to be out of date.
- [let relevanceScore: Double](activitycontent/relevancescore.md)
  A score you assign that determines the order in which your Live Activities appear when you start several Live Activities for your app.
### Default Implementations
- [CustomStringConvertible Implementations](activitycontent/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [typealias ContentState](activity/contentstate-swift.typealias.md)
  The type alias for the structure that describes the dynamic content of a Live Activity.
- [struct PushType](pushtype.md)
  The structure that offers constants you use to configure a Live Activity to receive updates through ActivityKit push notifications.
- [enum ActivityAuthorizationError](activityauthorizationerror.md)
  An error that indicates why the request to start a Live Activity failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activitycontent)*