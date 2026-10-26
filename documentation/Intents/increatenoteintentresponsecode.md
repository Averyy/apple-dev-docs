# INCreateNoteIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the state of the response.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INCreateNoteIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
enum INCreateNoteIntentResponseCode
```

```c
enum INCreateNoteIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INCreateNoteIntentResponseCode.unspecified](./increatenoteintentresponsecode/unspecified.md)
  The response code was not specified.
- [INCreateNoteIntentResponseCode.ready](./increatenoteintentresponsecode/ready.md)
  You are ready to handle the intent.
- [INCreateNoteIntentResponseCode.inProgress](./increatenoteintentresponsecode/inprogress.md)
  Note creation is still in progress.
- [INCreateNoteIntentResponseCode.success](./increatenoteintentresponsecode/success.md)
  You successfully created the note.
- [INCreateNoteIntentResponseCode.failure](./increatenoteintentresponsecode/failure.md)
  You were unable to create the note.
- [INCreateNoteIntentResponseCode.failureRequiringAppLaunch](./increatenoteintentresponsecode/failurerequiringapplaunch.md)
  The user must create the note from within your app.
### Initializers
- [init?(rawValue: Int)](./increatenoteintentresponsecode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Response Code
- [var code: INCreateNoteIntentResponseCode](./increatenoteintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatenoteintentresponsecode)*