# INAppendToNoteIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a request to append content to a note.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INAppendToNoteIntentResponse
```

```objc
@interface INAppendToNoteIntentResponse : INIntentResponse
```

## Overview

Use an [`INAppendToNoteIntentResponse`](./inappendtonoteintentresponse.md) object to return information about the updated note. Siri communicates the information from the response to the user at appropriate times. Be sure to include the details of the note in the [`note`](./inappendtonoteintentresponse/note.md) property.

You create an [`INAppendToNoteIntentResponse`](./inappendtonoteintentresponse.md) object in the [`confirm(intent:completion:)`](./inappendtonoteintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./inappendtonoteintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INAppendToNoteIntentHandling`](./inappendtonoteintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INAppendToNoteIntentResponseCode, userActivity: NSUserActivity?)](./inappendtonoteintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INAppendToNoteIntentResponseCode](./inappendtonoteintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INAppendToNoteIntentResponseCode](./inappendtonoteintentresponsecode.md)
  Constants indicating the state of the response.
### Accessing the Note Content
- [var note: INNote?](./inappendtonoteintentresponse/note.md)
  The details of the note that you updated.

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

### Note Additions
- [protocol INAppendToNoteIntentHandling](./inappendtonoteintenthandling.md)
  The handler interface for appending content to a note.
- [class INAppendToNoteIntent](./inappendtonoteintent.md)
  A request to append content to a note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inappendtonoteintentresponse)*