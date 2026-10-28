# INStartAudioCallIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An app’s response to an intent to start an audio call.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 6.0

> **Deprecated**: Use [`INStartCallIntentResponse`](./instartcallintentresponse.md) instead.

## Declaration

```swift
class INStartAudioCallIntentResponse
```

```objc
@interface INStartAudioCallIntentResponse : INIntentResponse
```

## Overview

Use an [`INStartAudioCallIntentResponse`](./instartaudiocallintentresponse.md) object to specify whether your app is able to initiate an audio-based call. You create instances of this class when confirming and handling an [`INStartAudioCallIntent`](./instartaudiocallintent.md) object. When it’s time to call the user, SiriKit launches your app and delivers the [`NSUserActivity`](../Foundation/nsuseractivity.md) object contained in this object. Use that user activity object to specify any additional information that would assist your app in placing the call.

You create an [`INStartAudioCallIntentResponse`](./instartaudiocallintentresponse.md) object in the [`confirm(intent:completion:)`](./instartaudiocallintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./instartaudiocallintenthandling/handle%28intent,completion%29.md) methods of your start audio call handler object. For more information about implementing your handler object, see [`INStartAudioCallIntentHandling`](./instartaudiocallintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INStartAudioCallIntentResponseCode, userActivity: NSUserActivity?)](./instartaudiocallintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INStartAudioCallIntentResponseCode](./instartaudiocallintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INStartAudioCallIntentResponseCode](./instartaudiocallintentresponsecode.md)
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

### Audio Call Initiation
- [protocol INStartAudioCallIntentHandling](./instartaudiocallintenthandling.md)
  The handler interface for initiating an audio call from your app.
- [class INStartAudioCallIntent](./instartaudiocallintent.md)
  A request to start an audio-only call with one or more users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartaudiocallintentresponse)*