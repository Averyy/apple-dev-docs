# INStartVideoCallIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A response to an intent to start a video call.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`INStartCallIntentResponse`](./instartcallintentresponse.md) instead.

## Declaration

```swift
class INStartVideoCallIntentResponse
```

```objc
@interface INStartVideoCallIntentResponse : INIntentResponse
```

## Overview

Use an [`INStartVideoCallIntentResponse`](./instartvideocallintentresponse.md) object to specify whether your app is able to initiate a video call. You create instances of this class when confirming and handling an [`INStartVideoCallIntent`](./instartvideocallintent.md) object. When it’s time to call the user, SiriKit launches your app and delivers the [`NSUserActivity`](../Foundation/nsuseractivity.md) object contained in this object. Use that user activity object to specify any additional information that would assist your app in placing the call.

You create an [`INStartVideoCallIntentResponse`](./instartvideocallintentresponse.md) object in the [`confirm(intent:completion:)`](./instartvideocallintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./instartvideocallintenthandling/handle%28intent,completion%29.md) methods of your start video call handler object. For more information about implementing your handler object, see [`INStartVideoCallIntentHandling`](./instartvideocallintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INStartVideoCallIntentResponseCode, userActivity: NSUserActivity?)](./instartvideocallintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INStartVideoCallIntentResponseCode](./instartvideocallintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INStartVideoCallIntentResponseCode](./instartvideocallintentresponsecode.md)
  Constants indicating the status of the response.

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

### Video Call Initiation
- [protocol INStartVideoCallIntentHandling](./instartvideocallintenthandling.md)
  The handler interface for initiating a video call from your app.
- [class INStartVideoCallIntent](./instartvideocallintent.md)
  A request to start a video call with one or more users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartvideocallintentresponse)*