# INCreateNoteIntentResponseCode.inProgress

**Framework**: Intents  
**Kind**: case  
**Role**: Case

Note creation is still in progress.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INCreateNoteIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
case inProgress
```

```c
INCreateNoteIntentResponseCodeInProgress
```

#### Discussion

Return this code if you initiated the note creation process but did not receive a timely response. You might use this code when a server handles note creation and you have not yet received a confirmation from that server.

When handling an intent, you might want to first configure a timer to fire if your server does not return within a few seconds. Use your timer’s handler block to provide the in-progress response back to Siri.

## See Also

### Constants
- [INCreateNoteIntentResponseCode.unspecified](./unspecified.md)
  The response code was not specified.
- [INCreateNoteIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INCreateNoteIntentResponseCode.success](./success.md)
  You successfully created the note.
- [INCreateNoteIntentResponseCode.failure](./failure.md)
  You were unable to create the note.
- [INCreateNoteIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must create the note from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatenoteintentresponsecode/inprogress)*