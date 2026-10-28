# billDetails

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The details of the bill to pay.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
@NSCopying
var billDetails: INBillDetails? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INBillDetails * billDetails;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INBillDetails * billDetails;
```

## Discussion

Use this property to specify the details of the bill, including the amount due, the due date, the payee, and the type of the bill. Always provide as much detail as possible. It’s your responsibility to gather information about payees and any bills that the user needs to pay in your app. You must then make the payee and bill information available to your Intents extension so that you can fill in this property.

## See Also

### Providing the Transaction Details
- [var transactionAmount: INPaymentAmount?](./transactionamount.md)
  The amount of money to transfer to the payee.
- [var transactionScheduledDate: INDateComponentsRange?](./transactionscheduleddate.md)
  The date on which the transaction is to occur.
- [var transactionNote: String?](./transactionnote.md)
  Notes to include with the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintentresponse/billdetails)*