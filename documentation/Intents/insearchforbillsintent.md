# INSearchForBillsIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request for the list of bills matching the specified criteria.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INSearchForBillsIntent
```

```objc
@interface INSearchForBillsIntent : INIntent
```

## Overview

Siri creates an [`INSearchForBillsIntent`](./insearchforbillsintent.md) object when the user asks to see pending or already paid bills. The intent object contains the values to match when searching for bills. Users can search for bills based on the due date, the payee, the type, and whether they’re pending or already paid. When performing the search, use only the provided parameters to filter the search results and ignore any parameters that have a missing or unknown value.

To handle this intent, the handler object in your Intents extension must adopt the [`INSearchForBillsIntentHandling`](./insearchforbillsintenthandling.md) protocol. Your handler should confirm the request and create an [`INSearchForBillsIntentResponse`](./insearchforbillsintentresponse.md) object with the results of the search. For successful searches, Siri offers a way for the user to view the results.

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents |
| Always requires unlocked device | Yes |

When performing a search, Siri automatically asks the user to unlock a currently locked device. You don’t need to explicitly ask to unlock the device.

## Topics

### Initializing the Intent Object
- [init(billPayee: INBillPayee?, paymentDateRange: INDateComponentsRange?, billType: INBillType, status: INPaymentStatus, dueDateRange: INDateComponentsRange?)](./insearchforbillsintent/init%28billpayee,paymentdaterange,billtype,status,duedaterange%29.md)
  Initializes an intent object that describes a search for bill details with the specified search parameters.
### Getting the Search Attributes
- [var billPayee: INBillPayee?](./insearchforbillsintent/billpayee.md)
  The recipient of the payment.
- [var billType: INBillType](./insearchforbillsintent/billtype.md)
  The type of the bill.
- [var dueDateRange: INDateComponentsRange?](./insearchforbillsintent/duedaterange.md)
  The range of due dates in which to search for bills.
- [var paymentDateRange: INDateComponentsRange?](./insearchforbillsintent/paymentdaterange.md)
  The range of payment dates in which to search for bills.
- [var status: INPaymentStatus](./insearchforbillsintent/status.md)
  The status of the bill.

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Bill Search
- [protocol INSearchForBillsIntentHandling](./insearchforbillsintenthandling.md)
  The handler interface for searching for bills associated with the user.
- [class INSearchForBillsIntentResponse](./insearchforbillsintentresponse.md)
  Your app’s response to a request to a search for bills.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforbillsintent)*