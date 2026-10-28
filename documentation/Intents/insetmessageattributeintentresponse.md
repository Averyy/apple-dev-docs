# INSetMessageAttributeIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a set message attribute intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INSetMessageAttributeIntentResponse
```

```objc
@interface INSetMessageAttributeIntentResponse : INIntentResponse
```

## Overview

An [`INSetMessageAttributeIntentResponse`](./insetmessageattributeintentresponse.md) object contains the status of modifying the specified messages. You create instances of this class when confirming or handling a set message attribute intent.

You create an [`INSetMessageAttributeIntentResponse`](./insetmessageattributeintentresponse.md) object in the [`confirm(intent:completion:)`](./insetmessageattributeintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./insetmessageattributeintenthandling/handle%28intent,completion%29.md) methods of your set message attribute handler object. For more information about implementing your handler object, see [`INSetMessageAttributeIntentHandling`](./insetmessageattributeintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INSetMessageAttributeIntentResponseCode, userActivity: NSUserActivity?)](./insetmessageattributeintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INSetMessageAttributeIntentResponseCode](./insetmessageattributeintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INSetMessageAttributeIntentResponseCode](./insetmessageattributeintentresponsecode.md)
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

### Setting Message Attributes
- [protocol INSetMessageAttributeIntentHandling](./insetmessageattributeintenthandling.md)
  An interface that handles modifying message attributes.
- [class INSetMessageAttributeIntent](./insetmessageattributeintent.md)
  A request to modify the attributes of a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetmessageattributeintentresponse)*