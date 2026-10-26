# INSendRideFeedbackIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An intent indicating that the user provided feedback for a completed ride.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INSendRideFeedbackIntent
```

```objc
@interface INSendRideFeedbackIntent : INIntent
```

#### Overview

When the user provides feedback for a completed ride, SiriKit sends an [`INSendRideFeedbackIntent`](./insendridefeedbackintent.md) object to your handler. SiriKit populates this intent object with the ride identifier and the feedback, including a possible driver rating and tip. Upon receiving this intent, validate the provided information and forward it along to your service. SiriKit guarantees that it provides at least one piece of feedback.

To handle this intent, the handler object in your Intents extension must adopt the [`INSendRideFeedbackIntentHandling`](./insendridefeedbackintenthandling.md) protocol. Your handler should confirm the request and create an [`INSendRideFeedbackIntentResponse`](./insendridefeedbackintentresponse.md) object with the status of the task.

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Maps |
| Always requires unlocked device | Yes |

## Topics

### Initializing the Intent Object
- [init(rideIdentifier: String)](./insendridefeedbackintent/init%28rideidentifier%29.md)
  Initializes the intent object with the specified ride identifier.
### Identifying the Ride
- [var rideIdentifier: String](./insendridefeedbackintent/rideidentifier.md)
  The unique identifier that you assigned to the ride.
### Identifying the Feedback
- [var rating: NSNumber?](./insendridefeedbackintent/rating.md)
  The user-supplied rating for the driver.
- [var tip: INCurrencyAmount?](./insendridefeedbackintent/tip.md)
  The tip for the driver.

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Send Ride Feedback
- [protocol INSendRideFeedbackIntentHandling](./insendridefeedbackintenthandling.md)
  The handler interface for sending ride feedback to your service.
- [class INSendRideFeedbackIntentResponse](./insendridefeedbackintentresponse.md)
  Your app’s response to a send ride feedback intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendridefeedbackintent)*