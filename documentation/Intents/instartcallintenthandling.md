# INStartCallIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

An interface that handles requests to start audio and video calls.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol INStartCallIntentHandling : NSObjectProtocol
```

```objc
@protocol INStartCallIntentHandling <NSObject>
```

## Mentions

- [Dispatching intents to handlers](../SiriKit/dispatching-intents-to-handlers.md)

#### Overview

Use the methods of the [`INStartCallIntentHandling`](./instartcallintenthandling.md) protocol to resolve, confirm, and handle requests to start an audio or video call with the designated users. Adopt this protocol in an object of your Intents extension that’s capable of validating the call information. Your Intents extension shouldn’t try to initiate the call directly. Instead, a successful response involves asking Siri to launch your app to begin the call.

Siri delivers an [`INStartCallIntent`](./instartcallintent.md) object to your handler when the user asks to initiate a call using your app. The provided intent object contains information about who the user wants to call. Use the methods of this protocol to resolve the list of callable contacts and to validate that your app can place the call successfully.

## Topics

### Resolving the Intent Parameters
- [func resolveCallCapability(for: INStartCallIntent, with: (INStartCallCallCapabilityResolutionResult) -> Void)](./instartcallintenthandling/resolvecallcapability%28for,with%29.md)
  Resolves the type of call to start.
- [func resolveContacts(for: INStartCallIntent, with: ([INStartCallContactResolutionResult]) -> Void)](./instartcallintenthandling/resolvecontacts%28for,with%29.md)
  Resolves the recipients of the call.
- [func resolveDestinationType(for: INStartCallIntent, with: (INCallDestinationTypeResolutionResult) -> Void)](./instartcallintenthandling/resolvedestinationtype%28for,with%29.md)
  Resolves the destination of the call.
- [func resolveCallRecordToCallBack(for: INStartCallIntent, with: (INCallRecordResolutionResult) -> Void)](./instartcallintenthandling/resolvecallrecordtocallback%28for,with%29.md)
  Resolves the redial of a missed call.
### Confirming the Response
- [func confirm(intent: INStartCallIntent, completion: (INStartCallIntentResponse) -> Void)](./instartcallintenthandling/confirm%28intent,completion%29.md)
  Confirms whether your app is able to initiate the call.
### Handling the Intent
- [func handle(intent: INStartCallIntent, completion: (INStartCallIntentResponse) -> Void)](./instartcallintenthandling/handle%28intent,completion%29.md)
  Handles handing off the call to your app.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Starting a Call
- [class INStartCallIntent](./instartcallintent.md)
  A request to start an audio or video call with one or more users.
- [class INStartCallIntentResponse](./instartcallintentresponse.md)
  Your app’s response to a start call intent.
- [enum INStartCallCallRecordToCallBackUnsupportedReason](./instartcallcallrecordtocallbackunsupportedreason.md)
  A reason why your app can’t use a record to call a person back.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintenthandling)*