# INAppendToNoteIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for appending content to a note.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
protocol INAppendToNoteIntentHandling : NSObjectProtocol
```

```objc
@protocol INAppendToNoteIntentHandling <NSObject>
```

## Overview

Use the methods of the [`INAppendToNoteIntentHandling`](./inappendtonoteintenthandling.md) protocol to resolve, confirm, and handle requests to append content to an existing note. Adopt this protocol in an object of your Intents extension that’s capable of updating the note content in your app or note management service.

Siri delivers an [`INAppendToNoteIntent`](./inappendtonoteintent.md) object to your handler when the user asks to create a note using your app. The provided intent object contains information about which note to modify and the content to append. Use the methods of this protocol to resolve the parameters and update the note.

## Topics

### Resolving the Intent Parameters
- [func resolveContent(for: INAppendToNoteIntent, with: (INNoteContentResolutionResult) -> Void)](./inappendtonoteintenthandling/resolvecontent%28for,with%29.md)
  Resolves the content to append to the note.
- [func resolveTargetNote(for: INAppendToNoteIntent, with: (INNoteResolutionResult) -> Void)](./inappendtonoteintenthandling/resolvetargetnote%28for,with%29.md)
  Resolves the note that receives the new content.
### Confirming the Response
- [func confirm(intent: INAppendToNoteIntent, completion: (INAppendToNoteIntentResponse) -> Void)](./inappendtonoteintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can append content to the note.
### Handling the Intent
- [func handle(intent: INAppendToNoteIntent, completion: (INAppendToNoteIntentResponse) -> Void)](./inappendtonoteintenthandling/handle%28intent,completion%29.md)
  Handles appending content to a note.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INNotebookDomainHandling](./innotebookdomainhandling.md)

## See Also

### Note Additions
- [class INAppendToNoteIntent](./inappendtonoteintent.md)
  A request to append content to a note.
- [class INAppendToNoteIntentResponse](./inappendtonoteintentresponse.md)
  Your app’s response to a request to append content to a note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inappendtonoteintenthandling)*