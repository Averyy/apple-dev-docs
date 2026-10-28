# INSendRideFeedbackIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a send ride feedback intent.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INSendRideFeedbackIntentResponse
```

```objc
@interface INSendRideFeedbackIntentResponse : INIntentResponse
```

## Overview

An [`INSendRideFeedbackIntentResponse`](./insendridefeedbackintentresponse.md) object contains your app’s response to a request for feedback about a ride. After creating the response object, specify any feedback using the properties of this object. Siri and Maps display your response information to the user during the confirmation phase.

You create an [`INSendRideFeedbackIntentResponse`](./insendridefeedbackintentresponse.md) object in the [`confirm(sendRideFeedback:completion:)`](./insendridefeedbackintenthandling/confirm%28sendridefeedback,completion%29.md) and [`confirm(sendRideFeedback:completion:)`](./insendridefeedbackintenthandling/confirm%28sendridefeedback,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INSendRideFeedbackIntentHandling`](./insendridefeedbackintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INSendRideFeedbackIntentResponseCode, userActivity: NSUserActivity?)](./insendridefeedbackintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INSendRideFeedbackIntentResponseCode](./insendridefeedbackintentresponse/code.md)
  The code indicating whether your app successfully handled the intent.
- [enum INSendRideFeedbackIntentResponseCode](./insendridefeedbackintentresponsecode.md)
  Constants indicating the state of the response.

## Relationships

### Inherits From
- [INIntentResponse](./inintentresponse.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Send Ride Feedback
- [protocol INSendRideFeedbackIntentHandling](./insendridefeedbackintenthandling.md)
  The handler interface for sending ride feedback to your service.
- [class INSendRideFeedbackIntent](./insendridefeedbackintent.md)
  An intent indicating that the user provided feedback for a completed ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendridefeedbackintentresponse)*