# INCreateNoteIntentResponseCode.unspecified

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The response code was not specified.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INCreateNoteIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
case unspecified
```

```c
INCreateNoteIntentResponseCodeUnspecified
```

## Discussion

Do not return this response code when handling the intent; doing so causes the system to display an error.

## See Also

### Constants
- [INCreateNoteIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INCreateNoteIntentResponseCode.inProgress](./inprogress.md)
  Note creation is still in progress.
- [INCreateNoteIntentResponseCode.success](./success.md)
  You successfully created the note.
- [INCreateNoteIntentResponseCode.failure](./failure.md)
  You were unable to create the note.
- [INCreateNoteIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must create the note from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatenoteintentresponsecode/unspecified)*