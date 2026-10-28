# INStartCallIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a start call intent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INStartCallIntentResponse
```

```objc
@interface INStartCallIntentResponse : INIntentResponse
```

## Overview

Use an [`INStartCallIntentResponse`](./instartcallintentresponse.md) object to specify whether your app is able to initiate an audio or video call. You create instances of this class when confirming and handling an [`INStartCallIntent`](./instartcallintent.md) object. When it’s time to call the user, SiriKit launches your app and delivers the [`NSUserActivity`](../Foundation/nsuseractivity.md) object contained in this object. Use that user activity object to specify any additional information that assists your app in placing the call.

You create an [`INStartCallIntentResponse`](./instartcallintentresponse.md) object in the [`confirm(intent:completion:)`](./instartcallintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./instartcallintenthandling/handle%28intent,completion%29.md) methods of your start call handler object. For more information about implementing your handler object, see [`INStartCallIntentHandling`](./instartcallintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INStartCallIntentResponseCode, userActivity: NSUserActivity?)](./instartcallintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INStartCallIntentResponseCode](./instartcallintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INStartCallIntentResponseCode](./instartcallintentresponsecode.md)
  Constants that indicate the response state.

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

### Starting a Call
- [protocol INStartCallIntentHandling](./instartcallintenthandling.md)
  An interface that handles requests to start audio and video calls.
- [class INStartCallIntent](./instartcallintent.md)
  A request to start an audio or video call with one or more users.
- [enum INStartCallCallRecordToCallBackUnsupportedReason](./instartcallcallrecordtocallbackunsupportedreason.md)
  A reason why your app can’t use a record to call a person back.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintentresponse)*