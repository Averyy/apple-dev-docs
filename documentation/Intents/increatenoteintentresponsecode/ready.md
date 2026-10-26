# INCreateNoteIntentResponseCode.ready

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You are ready to handle the intent.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INCreateNoteIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
case ready
```

```c
INCreateNoteIntentResponseCodeReady
```

#### Discussion

Return this response code during the confirmation phase after you have verified that you are able to create the note. Do not return this response code when handling the intent; doing so causes the system to display an error.

## See Also

### Constants
- [INCreateNoteIntentResponseCode.unspecified](./unspecified.md)
  The response code was not specified.
- [INCreateNoteIntentResponseCode.inProgress](./inprogress.md)
  Note creation is still in progress.
- [INCreateNoteIntentResponseCode.success](./success.md)
  You successfully created the note.
- [INCreateNoteIntentResponseCode.failure](./failure.md)
  You were unable to create the note.
- [INCreateNoteIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must create the note from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatenoteintentresponsecode/ready)*