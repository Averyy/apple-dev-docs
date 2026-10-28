# INSendRideFeedbackIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for sending ride feedback to your service.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
protocol INSendRideFeedbackIntentHandling : NSObjectProtocol
```

```objc
@protocol INSendRideFeedbackIntentHandling <NSObject>
```

## Overview

Use the methods of the [`INSendRideFeedbackIntentHandling`](./insendridefeedbackintenthandling.md) protocol to confirm and handle requests to send feedback about a ride to your service. Adopt this protocol in an object of your Intents extension that is capable of conveying the feedback to your service.

To initiate the delivery of an [`INSendRideFeedbackIntent`](./insendridefeedbackintent.md), the user must have previously completed a ride in Maps or Siri and asked the user to provide feedback. Specifically, the [`INRideCompletionStatus`](./inridecompletionstatus.md) object that you created must indicate that it requires feedback before beginning a new ride. (Maps also gives the user a chance to provide feedback proactively). After the user provides feedback, Siri delivers the feedback intent to your Intents extension.

## Topics

### Confirming the Intent
- [func confirm(sendRideFeedback: INSendRideFeedbackIntent, completion: (INSendRideFeedbackIntentResponse) -> Void)](./insendridefeedbackintenthandling/confirm%28sendridefeedback,completion%29.md)
  Confirms that you can apply the feedback to the specified ride.
### Handling the Intent
- [func handle(sendRideFeedback: INSendRideFeedbackIntent, completion: (INSendRideFeedbackIntentResponse) -> Void)](./insendridefeedbackintenthandling/handle%28sendridefeedback,completion%29.md)
  Handles the recording of feedback for the specified ride.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INRidesharingDomainHandling](./inridesharingdomainhandling.md)

## See Also

### Send Ride Feedback
- [class INSendRideFeedbackIntent](./insendridefeedbackintent.md)
  An intent indicating that the user provided feedback for a completed ride.
- [class INSendRideFeedbackIntentResponse](./insendridefeedbackintentresponse.md)
  Your app’s response to a send ride feedback intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendridefeedbackintenthandling)*