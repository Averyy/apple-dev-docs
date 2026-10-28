# INGetVisualCodeIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for displaying your app’s visual codes.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
protocol INGetVisualCodeIntentHandling : NSObjectProtocol
```

```objc
@protocol INGetVisualCodeIntentHandling <NSObject>
```

## Overview

Use the methods of the [`INGetVisualCodeIntentHandling`](./ingetvisualcodeintenthandling.md) protocol to resolve, confirm, and handle requests to display visual codes such as QR codes. Adopt this protocol in an object of your Intents extension that’s capable of displaying an image representing the code.

Siri delivers an [`INGetVisualCodeIntent`](./ingetvisualcodeintent.md) object to your handler when the user asks your app to display a relevant visual code. The provided intent object contains information about the type of code to display. Use the methods of this protocol to resolve the account information and display the corresponding image.

## Topics

### Resolving the Intent Parameters
- [func resolveVisualCodeType(for: INGetVisualCodeIntent, with: (INVisualCodeTypeResolutionResult) -> Void)](./ingetvisualcodeintenthandling/resolvevisualcodetype%28for,with%29.md)
  Resolves the type of code requested by the user.
### Confirming the Response
- [func confirm(intent: INGetVisualCodeIntent, completion: (INGetVisualCodeIntentResponse) -> Void)](./ingetvisualcodeintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can provide the requested visual code.
### Handling the Intent
- [func handle(intent: INGetVisualCodeIntent, completion: (INGetVisualCodeIntentResponse) -> Void)](./ingetvisualcodeintenthandling/handle%28intent,completion%29.md)
  Handles providing the image for the specified visual code.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INVisualCodeDomainHandling](./invisualcodedomainhandling.md)

## See Also

### Visual Codes
- [class INGetVisualCodeIntent](./ingetvisualcodeintent.md)
  A request for a visual code to use for exchanging payment and contact information.
- [class INGetVisualCodeIntentResponse](./ingetvisualcodeintentresponse.md)
  Your app’s response to a request for a visual code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetvisualcodeintenthandling)*