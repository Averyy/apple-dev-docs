# INCreateNoteIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for creating notes.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INCreateNoteIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
protocol INCreateNoteIntentHandling : NSObjectProtocol
```

```objc
@protocol INCreateNoteIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INCreateNoteIntentHandling`](./increatenoteintenthandling.md) protocol to resolve, confirm, and handle requests to create notes. Adopt this protocol in an object of your Intents extension that is capable of forwarding the note content to your app or note management service.

Siri delivers an [`INCreateNoteIntent`](./increatenoteintent.md) object to your handler when the user asks to create a note using your app. The provided intent object contains the information to put into the note. Use the methods of this protocol to resolve the parameters and create the note.

## Topics

### Resolving the Intent Parameters
- [func resolveTitle(for: INCreateNoteIntent, with: (INSpeakableStringResolutionResult) -> Void)](./increatenoteintenthandling/resolvetitle%28for,with%29.md)
  Resolves the title of the note.
- [func resolveContent(for: INCreateNoteIntent, with: (INNoteContentResolutionResult) -> Void)](./increatenoteintenthandling/resolvecontent%28for,with%29.md)
  Resolves the main content of the note.
- [func resolveGroupName(for: INCreateNoteIntent, with: (INSpeakableStringResolutionResult) -> Void)](./increatenoteintenthandling/resolvegroupname%28for,with%29.md)
  Resolves the intended group of the note.
### Confirming the Response
- [func confirm(intent: INCreateNoteIntent, completion: (INCreateNoteIntentResponse) -> Void)](./increatenoteintenthandling/confirm%28intent,completion%29.md)
  Confirms whether you can create the note.
### Handling the Intent
- [func handle(intent: INCreateNoteIntent, completion: (INCreateNoteIntentResponse) -> Void)](./increatenoteintenthandling/handle%28intent,completion%29.md)
  Handles the creation of a note.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INNotebookDomainHandling](./innotebookdomainhandling.md)

## See Also

### Note Creation
- [class INCreateNoteIntent](./increatenoteintent.md)
  A request to create a new note.
- [class INCreateNoteIntentResponse](./increatenoteintentresponse.md)
  Your app’s response to a request to create a note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatenoteintenthandling)*