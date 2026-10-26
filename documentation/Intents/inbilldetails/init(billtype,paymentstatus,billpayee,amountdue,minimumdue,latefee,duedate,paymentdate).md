# init(billType:paymentStatus:billPayee:amountDue:minimumDue:lateFee:dueDate:paymentDate:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes a bill details object with information about the bill to pay.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
init?(billType: INBillType, paymentStatus: INPaymentStatus, billPayee: INBillPayee?, amountDue: INCurrencyAmount?, minimumDue: INCurrencyAmount?, lateFee: INCurrencyAmount?, dueDate: DateComponents?, paymentDate: DateComponents?)
```

```objc
- (instancetype) initWithBillType:(INBillType) billType paymentStatus:(INPaymentStatus) paymentStatus billPayee:(INBillPayee *) billPayee amountDue:(INCurrencyAmount *) amountDue minimumDue:(INCurrencyAmount *) minimumDue lateFee:(INCurrencyAmount *) lateFee dueDate:(NSDateComponents *) dueDate paymentDate:(NSDateComponents *) paymentDate;
```

#### Return Value

An initialized bill details object or `nil` if the object could not be created.

## Parameters

- `billType`: The type of the bill.
- `paymentStatus`: A constant indicating the current status of the bill, such as whether the bill is pending.
- `billPayee`: The originator of the bill and the recipient of any funds applied to the bill payment.
- `amountDue`: The total amount of the bill.
- `minimumDue`: The minimum amount that the user must pay toward the bill.
- `lateFee`: The fee applied if the user pays the bill after the due date.
- `dueDate`: The date on which the bill is due.
- `paymentDate`: The date on which payment occured.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbilldetails/init(billtype:paymentstatus:billpayee:amountdue:minimumdue:latefee:duedate:paymentdate:))*