# INPaymentsDomainHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

An interface for adopting all of the protocols in the payments domain.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 6.0

> **Deprecated**: Please conform to INSendPaymentIntentHandling, INRequestPaymentIntentHandling, INPayBillIntentHandling, INSearchForBillsIntentHandling, INSearchForAccountsIntentHandling and INTransferMoneyIntentHandling instead

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
protocol INPaymentsDomainHandling : INPayBillIntentHandling, INRequestPaymentIntentHandling, INSearchForAccountsIntentHandling, INSearchForBillsIntentHandling, INSendPaymentIntentHandling, INTransferMoneyIntentHandling
```

*watchOS*

```swift
protocol INPaymentsDomainHandling : INRequestPaymentIntentHandling, INSendPaymentIntentHandling
```

*iOS, iPadOS, Mac Catalyst, macOS, visionOS*

```objc
@protocol INPaymentsDomainHandling <INSendPaymentIntentHandling, INRequestPaymentIntentHandling, INPayBillIntentHandling, INSearchForBillsIntentHandling, INSearchForAccountsIntentHandling, INTransferMoneyIntentHandling>
```

*watchOS*

```objc
@protocol INPaymentsDomainHandling <INSendPaymentIntentHandling, INRequestPaymentIntentHandling>
```

## Overview

The [`INPaymentsDomainHandling`](./inpaymentsdomainhandling.md) protocol is a convenience protocol that adopts all of the protocols used to handle payment-related intents. When your app adopts all of the protocols associated with payments, you can adopt this one protocol instead of adopting the [`INSendPaymentIntentHandling`](./insendpaymentintenthandling.md), [`INRequestPaymentIntentHandling`](./inrequestpaymentintenthandling.md), [`INPayBillIntentHandling`](./inpaybillintenthandling.md), [`INSearchForBillsIntentHandling`](./insearchforbillsintenthandling.md), [`INSearchForAccountsIntentHandling`](./insearchforaccountsintenthandling.md), and [`INTransferMoneyIntentHandling`](./intransfermoneyintenthandling.md) protocols separately.

An object that adopts this protocol must be able to respond to the following intents:

- [`INRequestPaymentIntent`](./inrequestpaymentintent.md), a request for a payment from another user.
- [`INSendPaymentIntent`](./insendpaymentintent.md), a request to send a payment to another user.
- [`INPayBillIntent`](./inpaybillintent.md), a request to pay a bill.
- [`INSearchForBillsIntent`](./insearchforbillsintent.md), a request to search for bills to pay.
- [`INSearchForAccountsIntent`](./insearchforaccountsintent.md), a request to provide a list of the user’s accounts.
- [`INTransferMoneyIntent`](./intransfermoneyintent.md), a request to transfer money between the designated accounts.

Your handler object must be prepared to resolve any parameters associated with these intents and to confirm and handle the requests. When confirming and handling a request, you provide the response object that matches the specified intent.

## Relationships

### Inherits From
- [INPayBillIntentHandling](./inpaybillintenthandling.md)
- [INRequestPaymentIntentHandling](./inrequestpaymentintenthandling.md)
- [INSearchForAccountsIntentHandling](./insearchforaccountsintenthandling.md)
- [INSearchForBillsIntentHandling](./insearchforbillsintenthandling.md)
- [INSendPaymentIntentHandling](./insendpaymentintenthandling.md)
- [INTransferMoneyIntentHandling](./intransfermoneyintenthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Domain-Handling Protocols
- [protocol INMessagesDomainHandling](./inmessagesdomainhandling.md)
  An interface for adopting all of the protocols in the messages domain.
- [protocol INNotebookDomainHandling](./innotebookdomainhandling.md)
  An interface for adopting all of the protocols in the lists and notes domain.
- [protocol INWorkoutsDomainHandling](./inworkoutsdomainhandling.md)
  An interface for adopting all of the protocols in the workouts domain.
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentsdomainhandling)*