# INCreateNoteIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a request to create a note.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INCreateNoteIntentResponse is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class INCreateNoteIntentResponse
```

```objc
@interface INCreateNoteIntentResponse : INIntentResponse
```

#### Overview

Use an [`INCreateNoteIntentResponse`](./increatenoteintentresponse.md) object to return information about the note that your app created. Siri communicates the information from your app’s response to the user at appropriate times.

You create an [`INCreateNoteIntentResponse`](./increatenoteintentresponse.md) object in the [`confirm(intent:completion:)`](./increatenoteintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./increatenoteintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INCreateNoteIntentHandling`](./increatenoteintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INCreateNoteIntentResponseCode, userActivity: NSUserActivity?)](./increatenoteintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INCreateNoteIntentResponseCode](./increatenoteintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INCreateNoteIntentResponseCode](./increatenoteintentresponsecode.md)
  Constants indicating the state of the response.
### Accessing the Note Content
- [var createdNote: INNote?](./increatenoteintentresponse/creatednote.md)
  The details of the note that you created.

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

### Note Creation
- [protocol INCreateNoteIntentHandling](./increatenoteintenthandling.md)
  The handler interface for creating notes.
- [class INCreateNoteIntent](./increatenoteintent.md)
  A request to create a new note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatenoteintentresponse)*