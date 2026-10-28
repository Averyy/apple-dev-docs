# init(billPayee:from:transactionAmount:transactionScheduledDate:transactionNote:billType:dueDate:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the bill pay intent object with the specified payee and transaction details.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
init(billPayee: INBillPayee?, from fromAccount: INPaymentAccount?, transactionAmount: INPaymentAmount?, transactionScheduledDate: INDateComponentsRange?, transactionNote: String?, billType: INBillType, dueDate: INDateComponentsRange?)
```

```objc
- (instancetype) initWithBillPayee:(INBillPayee *) billPayee fromAccount:(INPaymentAccount *) fromAccount transactionAmount:(INPaymentAmount *) transactionAmount transactionScheduledDate:(INDateComponentsRange *) transactionScheduledDate transactionNote:(NSString *) transactionNote billType:(INBillType) billType dueDate:(INDateComponentsRange *) dueDate;
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

Normally, you don’t create instances of this class yourself. Instead, SiriKit creates instances when the user asks to pay a bill. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `billPayee`: The entity that receives the payment. The user must configure payees in advance using your app. The payee in this parameter should correspond to one of the user’s known entities.
- `fromAccount`: The user account providing the funds for the transaction. The user must configure an account with your financial service before attempting to pay bills with that account. Use the information in the [`INPaymentAccount`](../inpaymentaccount.md) object to identify which account the user wants to use.
- `transactionAmount`: The amount of money to transfer from the user’s account to the bill payee. The object in this parameter may specify a numeric value or a relative value, such as the current balance due. For more information, see [`INPaymentAmount`](../inpaymentamount.md).
- `transactionScheduledDate`: The date on which to make the payment.
- `transactionNote`: A note to include with the transaction. Users can include notes for logging additional information about the payment. You should also save notes in your own system so that users can view them later.
- `billType`: The type of bill to pay. Use this parameter to categorize the type of bill. You should also save this information in your own system so that users can search for bill payments by type.
- `dueDate`: The date by which the user must pay the bill. When scheduling the bill payment, use this parameter to validate that the payment isn’t too late.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintent/init(billpayee:from:transactionamount:transactionscheduleddate:transactionnote:billtype:duedate:))*