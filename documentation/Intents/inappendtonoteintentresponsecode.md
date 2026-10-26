# INAppendToNoteIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the state of the response.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
enum INAppendToNoteIntentResponseCode
```

```c
enum INAppendToNoteIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INAppendToNoteIntentResponseCode.unspecified](./inappendtonoteintentresponsecode/unspecified.md)
  The response didn’t specify a response code.
- [INAppendToNoteIntentResponseCode.ready](./inappendtonoteintentresponsecode/ready.md)
  You’re ready to handle the intent.
- [INAppendToNoteIntentResponseCode.inProgress](./inappendtonoteintentresponsecode/inprogress.md)
  You’re in the process of updating the note.
- [INAppendToNoteIntentResponseCode.success](./inappendtonoteintentresponsecode/success.md)
  You successfully updated the note.
- [INAppendToNoteIntentResponseCode.failure](./inappendtonoteintentresponsecode/failure.md)
  You were unable to update the note.
- [INAppendToNoteIntentResponseCode.failureRequiringAppLaunch](./inappendtonoteintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to update the note.
- [INAppendToNoteIntentResponseCode.failureCannotUpdatePasswordProtectedNote](./inappendtonoteintentresponsecode/failurecannotupdatepasswordprotectednote.md)
  You were unable to update the note because your app requires additional authorization to do so.
### Initializers
- [init?(rawValue: Int)](./inappendtonoteintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INAppendToNoteIntentResponseCode](./inappendtonoteintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inappendtonoteintentresponsecode)*