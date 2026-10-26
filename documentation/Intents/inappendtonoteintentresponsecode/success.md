# INAppendToNoteIntentResponseCode.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You successfully updated the note.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case success
```

```c
INAppendToNoteIntentResponseCodeSuccess
```

#### Discussion

Use this code after updating the note successfully. Your response should contain the details of the note that you updated.

## See Also

### Constants
- [INAppendToNoteIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INAppendToNoteIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INAppendToNoteIntentResponseCode.inProgress](./inprogress.md)
  You’re in the process of updating the note.
- [INAppendToNoteIntentResponseCode.failure](./failure.md)
  You were unable to update the note.
- [INAppendToNoteIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to update the note.
- [INAppendToNoteIntentResponseCode.failureCannotUpdatePasswordProtectedNote](./failurecannotupdatepasswordprotectednote.md)
  You were unable to update the note because your app requires additional authorization to do so.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inappendtonoteintentresponsecode/success)*