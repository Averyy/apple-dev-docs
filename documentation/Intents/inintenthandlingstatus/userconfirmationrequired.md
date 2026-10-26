# INIntentHandlingStatus.userConfirmationRequired

**Framework**: Intents  
**Kind**: case  
**Role**: Case

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
case userConfirmationRequired
```

```c
INIntentHandlingStatusUserConfirmationRequired
```

## See Also

### Constants
- [INIntentHandlingStatus.unspecified](./unspecified.md)
  The status of the interaction is unknown. This is the default value.
- [INIntentHandlingStatus.ready](./ready.md)
  The intent is ready to be handled, but has not yet been handled.
- [INIntentHandlingStatus.inProgress](./inprogress.md)
  The Intents extension is in the process of handling the intent.
- [INIntentHandlingStatus.success](./success.md)
  The Intents extension successfully handled the intent.
- [INIntentHandlingStatus.failure](./failure.md)
  The Intents extension encountered an unrecoverable problem when handling the intent.
- [INIntentHandlingStatus.deferredToApplication](./deferredtoapplication.md)
  The Intents extension asked its associated app to handle the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintenthandlingstatus/userconfirmationrequired)*