# INGetVisualCodeIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a request for a visual code.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INGetVisualCodeIntentResponse
```

```objc
@interface INGetVisualCodeIntentResponse : INIntentResponse
```

## Overview

Use an [`INGetVisualCodeIntentResponse`](./ingetvisualcodeintentresponse.md) object to provide the visual code to display. When handling the intent, provide an image with the requested visual code. Siri communicates the details back to the user at appropriate times.

You create an [`INGetVisualCodeIntentResponse`](./ingetvisualcodeintentresponse.md) object in the [`confirm(intent:completion:)`](./ingetvisualcodeintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./ingetvisualcodeintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INGetVisualCodeIntentHandling`](./ingetvisualcodeintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INGetVisualCodeIntentResponseCode, userActivity: NSUserActivity?)](./ingetvisualcodeintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INGetVisualCodeIntentResponseCode](./ingetvisualcodeintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INGetVisualCodeIntentResponseCode](./ingetvisualcodeintentresponsecode.md)
  Constants indicating the state of the response.
### Providing the Code Image
- [var visualCodeImage: INImage?](./ingetvisualcodeintentresponse/visualcodeimage.md)
  The image containing the visual code.

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

### Visual Codes
- [protocol INGetVisualCodeIntentHandling](./ingetvisualcodeintenthandling.md)
  The handler interface for displaying your app’s visual codes.
- [class INGetVisualCodeIntent](./ingetvisualcodeintent.md)
  A request for a visual code to use for exchanging payment and contact information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetvisualcodeintentresponse)*