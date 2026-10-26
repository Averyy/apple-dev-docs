# INMessagesDomainHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

An interface for adopting all of the protocols in the messages domain.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 6.0

> **Deprecated**: Please conform to INSendMessageIntentHandling, INSearchForMessagesIntentHandling and INSetMessageAttributeIntentHandling instead

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
protocol INMessagesDomainHandling : INSearchForMessagesIntentHandling, INSendMessageIntentHandling, INSetMessageAttributeIntentHandling
```

*watchOS*

```swift
protocol INMessagesDomainHandling : INSearchForMessagesIntentHandling, INSendMessageIntentHandling
```

*iOS, iPadOS, Mac Catalyst, macOS, visionOS*

```objc
@protocol INMessagesDomainHandling <INSendMessageIntentHandling, INSearchForMessagesIntentHandling, INSetMessageAttributeIntentHandling>
```

*watchOS*

```objc
@protocol INMessagesDomainHandling <INSendMessageIntentHandling, INSearchForMessagesIntentHandling>
```

#### Overview

The [`INMessagesDomainHandling`](./inmessagesdomainhandling.md) protocol is a convenience protocol that adopts all of the protocols used to handle message-related intents. When your app adopts all of the protocols associated with messages, you can adopt this one protocol instead of adopting the [`INSendMessageIntentHandling`](./insendmessageintenthandling.md), [`INSearchForMessagesIntentHandling`](./insearchformessagesintenthandling.md), and [`INSetMessageAttributeIntent`](./insetmessageattributeintent.md) protocols separately.

An object that adopts this protocol must be able to respond to the following intents:

- [`INSendMessageIntent`](./insendmessageintent.md), a request to compose and send a message to one or more recipients.
- [`INSearchForMessagesIntent`](./insearchformessagesintent.md), a request to search for specific messages based on a set of query parameters.
- [`INSetMessageAttributeIntent`](./insetmessageattributeintent.md), a request to modify a message, such as mark it as read.

You must prepare your handler object to resolve any parameters associated with these intents and to confirm and handle the requests. When confirming and handling a request, you provide the response object that matches the specified intent.

## Relationships

### Inherits From
- [INSearchForMessagesIntentHandling](./insearchformessagesintenthandling.md)
- [INSendMessageIntentHandling](./insendmessageintenthandling.md)
- [INSetMessageAttributeIntentHandling](./insetmessageattributeintenthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Domain-Handling Protocols
- [protocol INNotebookDomainHandling](./innotebookdomainhandling.md)
  An interface for adopting all of the protocols in the lists and notes domain.
- [protocol INWorkoutsDomainHandling](./inworkoutsdomainhandling.md)
  An interface for adopting all of the protocols in the workouts domain.
- [protocol INPaymentsDomainHandling](./inpaymentsdomainhandling.md)
  An interface for adopting all of the protocols in the payments domain.
- [protocol INCallsDomainHandling](./incallsdomainhandling.md)
  Provides a convenient way to adopt all of the protocols in the VoIP calling domain.
- [protocol INVisualCodeDomainHandling](./invisualcodedomainhandling.md)
  An interface for adopting all of the protocols in the visual codes domain.
- [protocol INPhotosDomainHandling](./inphotosdomainhandling.md)
  An interface for adopting all of the protocols in the photos domain.
- [protocol INRidesharingDomainHandling](./inridesharingdomainhandling.md)
  An interface for adopting all of the protocols in the ride-booking domain.
- [protocol INCarCommandsDomainHandling](./incarcommandsdomainhandling.md)
  An interface for adopting all the handling protocols in the car commands domain.
- [protocol INCarPlayDomainHandling](./incarplaydomainhandling.md)
  An interface for adopting all of the protocols in the CarPlay domain.
- [protocol INRadioDomainHandling](./inradiodomainhandling.md)
  An interface for adopting all of the protocols in the radio domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessagesdomainhandling)*