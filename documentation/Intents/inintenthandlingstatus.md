# INIntentHandlingStatus

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the current state of the interaction.

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
enum INIntentHandlingStatus
```

```c
enum INIntentHandlingStatus : NSInteger;
```

## Topics

### Constants
- [INIntentHandlingStatus.unspecified](./inintenthandlingstatus/unspecified.md)
  The status of the interaction is unknown. This is the default value.
- [INIntentHandlingStatus.ready](./inintenthandlingstatus/ready.md)
  The intent is ready to be handled, but has not yet been handled.
- [INIntentHandlingStatus.inProgress](./inintenthandlingstatus/inprogress.md)
  The Intents extension is in the process of handling the intent.
- [INIntentHandlingStatus.success](./inintenthandlingstatus/success.md)
  The Intents extension successfully handled the intent.
- [INIntentHandlingStatus.failure](./inintenthandlingstatus/failure.md)
  The Intents extension encountered an unrecoverable problem when handling the intent.
- [INIntentHandlingStatus.deferredToApplication](./inintenthandlingstatus/deferredtoapplication.md)
  The Intents extension asked its associated app to handle the intent.
- [INIntentHandlingStatus.userConfirmationRequired](./inintenthandlingstatus/userconfirmationrequired.md)
### Initializers
- [init?(rawValue: Int)](./inintenthandlingstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum INInteractionDirection](./ininteractiondirection.md)
  Constants indicating whether the app is providing or receiving information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintenthandlingstatus)*