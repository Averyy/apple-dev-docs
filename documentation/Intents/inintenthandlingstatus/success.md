# INIntentHandlingStatus.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The Intents extension successfully handled the intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case success
```

```c
INIntentHandlingStatusSuccess
```

## See Also

### Constants
- [INIntentHandlingStatus.unspecified](./unspecified.md)
  The status of the interaction is unknown. This is the default value.
- [INIntentHandlingStatus.ready](./ready.md)
  The intent is ready to be handled, but has not yet been handled.
- [INIntentHandlingStatus.inProgress](./inprogress.md)
  The Intents extension is in the process of handling the intent.
- [INIntentHandlingStatus.failure](./failure.md)
  The Intents extension encountered an unrecoverable problem when handling the intent.
- [INIntentHandlingStatus.deferredToApplication](./deferredtoapplication.md)
  The Intents extension asked its associated app to handle the intent.
- [INIntentHandlingStatus.userConfirmationRequired](./userconfirmationrequired.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintenthandlingstatus/success)*