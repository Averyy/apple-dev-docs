# init(billPayee:paymentDateRange:billType:status:dueDateRange:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes an intent object that describes a search for bill details with the specified search parameters.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
init(billPayee: INBillPayee?, paymentDateRange: INDateComponentsRange?, billType: INBillType, status: INPaymentStatus, dueDateRange: INDateComponentsRange?)
```

```objc
- (instancetype) initWithBillPayee:(INBillPayee *) billPayee paymentDateRange:(INDateComponentsRange *) paymentDateRange billType:(INBillType) billType status:(INPaymentStatus) status dueDateRange:(INDateComponentsRange *) dueDateRange;
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

Normally, you don’t create instances of this class yourself. Instead, SiriKit creates instances when the user asks to search for bills. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `billPayee`: The entity that created the bill. The user must configure payees in advance using your app. Use this parameter to search for bills from a specific organization.
- `paymentDateRange`: The date range during which payment occured. Use this parameter to search for bill payments within the specified date range.
- `billType`: The type of bill to pay. Use this parameter to search for bills of a specific type. Specify [`INBillType.unknown`](../inbilltype/unknown.md) to search for bills of any type.
- `status`: The current status of the bill. Use this parameter to search for pending or paid bills, or failed attempts to pay a bill.
- `dueDateRange`: The date range during which payment is due. Use this parameter to search for bills whose due date falls within the specified date range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforbillsintent/init(billpayee:paymentdaterange:billtype:status:duedaterange:))*