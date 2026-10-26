# INCreateNoteIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must create the note from within your app.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INCreateNoteIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INCreateNoteIntentResponseCodeFailureRequiringAppLaunch
```

#### Discussion

Use this response code when you cannot create the note from your Intents extension but the user can create it in your app. Do not use this code for general errors or to force the user to launch your app.

## See Also

### Constants
- [INCreateNoteIntentResponseCode.unspecified](./unspecified.md)
  The response code was not specified.
- [INCreateNoteIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INCreateNoteIntentResponseCode.inProgress](./inprogress.md)
  Note creation is still in progress.
- [INCreateNoteIntentResponseCode.success](./success.md)
  You successfully created the note.
- [INCreateNoteIntentResponseCode.failure](./failure.md)
  You were unable to create the note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatenoteintentresponsecode/failurerequiringapplaunch)*