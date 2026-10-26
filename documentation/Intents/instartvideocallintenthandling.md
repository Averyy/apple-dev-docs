# INStartVideoCallIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for initiating a video call from your app.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`INStartCallIntentHandling`](./instartcallintenthandling.md) instead.

## Declaration

```swift
protocol INStartVideoCallIntentHandling : NSObjectProtocol
```

```objc
@protocol INStartVideoCallIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INStartVideoCallIntentHandling`](./instartvideocallintenthandling.md) protocol to resolve, confirm, and handle requests to start a video call with the designated users. Adopt this protocol in an object of your Intents extension that’s capable of validating the call information. Don’t try to initiate the call directly in your Intents app extension. Instead, a successful response involves asking Siri to launch your app to begin the call.

Siri delivers an [`INStartVideoCallIntent`](./instartvideocallintent.md) object to your handler when the user asks to initiate a call using your app. The provided intent object contains information about who the user wants to call. Use the methods of this protocol to resolve the list of contacts to include in the call and to validate that your app can place the call successfully.

## Topics

### Resolving the Intent Parameters
- [func resolveContacts(for: INStartVideoCallIntent, with: ([INPersonResolutionResult]) -> Void)](./instartvideocallintenthandling/resolvecontacts%28for,with%29.md)
  Resolves the recipients of the call.
### Confirming the Response
- [func confirm(intent: INStartVideoCallIntent, completion: (INStartVideoCallIntentResponse) -> Void)](./instartvideocallintenthandling/confirm%28intent,completion%29.md)
  Validates whether your app is able to initiate the video call.
### Handling the Intent
- [func handle(intent: INStartVideoCallIntent, completion: (INStartVideoCallIntentResponse) -> Void)](./instartvideocallintenthandling/handle%28intent,completion%29.md)
  Provides information to hand off the call to your app.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INCallsDomainHandling](./incallsdomainhandling.md)

## See Also

### Video Call Initiation
- [class INStartVideoCallIntent](./instartvideocallintent.md)
  A request to start a video call with one or more users.
- [class INStartVideoCallIntentResponse](./instartvideocallintentresponse.md)
  A response to an intent to start a video call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartvideocallintenthandling)*