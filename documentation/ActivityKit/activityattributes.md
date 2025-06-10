# ActivityAttributes

**Framework**: ActivityKit  
**Kind**: protocol

The protocol you implement to describe the content of a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
protocol ActivityAttributes : Decodable, Encodable
```

## Mentions

- [Displaying live data with Live Activities](displaying-live-data-with-live-activities.md)
- [Starting and updating Live Activities with ActivityKit push notifications](starting-and-updating-live-activities-with-activitykit-push-notifications.md)
- [Launching your app from a Live Activity](launching-your-app-from-a-live-activity.md)

#### Overview

The `ActivityAttributes` protocol describes the content that appears in your Live Activity. Its inner type [`ContentState`](activityattributes/contentstate.md) represents the dynamic content of the Live Activity.

The following example shows an implementation of the `ActivityAttributes` protocol for a pizza delivery app. The app’s Live Activity shows the number of ordered pizzas and the total amount on the bill as static data and the name of the driver and an estimated delivery time as dynamic data that changes over time. Note how the implementation defines the type alias `PizzaDeliveryStatus` to make the code more descriptive and easier to read.

```swift
public import Foundation
import ActivityKit

struct PizzaDeliveryAttributes: ActivityAttributes {
    public typealias PizzaDeliveryStatus = ContentState

    public struct ContentState: Codable, Hashable {
        var driverName: String
        var deliveryTimer: ClosedRange<Date>
    }

    var numberOfPizzas: Int
    var totalAmount: String
    var orderNumber: String
}
```

## Topics

### Dynamic content
- [associatedtype ContentState : Decodable, Encodable, Hashable](activityattributes/contentstate.md)
  The associated type that describes the dynamic content of a Live Activity.
### Instance Methods
- [func previewContext(Self.ContentState, isStale: Bool, viewKind: ActivityPreviewViewKind) -> some View](activityattributes/previewcontext(_:isstale:viewkind:).md)
  Generates a preview for a Live Activity.

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activityattributes)*