# init(payee:payer:currencyAmount:paymentMethod:note:status:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes a payment record with the specified payment details.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
convenience init?(payee: INPerson?, payer: INPerson?, currencyAmount: INCurrencyAmount?, paymentMethod: INPaymentMethod?, note: String?, status: INPaymentStatus)
```

```objc
- (instancetype) initWithPayee:(INPerson *) payee payer:(INPerson *) payer currencyAmount:(INCurrencyAmount *) currencyAmount paymentMethod:(INPaymentMethod *) paymentMethod note:(NSString *) note status:(INPaymentStatus) status;
```

## Return Value

An initialized payment record object.

## Parameters

- `payee`: The person receiving the funds.
- `payer`: The person providing the funds.
- `currencyAmount`: The amount being transferred.
- `paymentMethod`: The payment method that represents the source of the funds.
- `note`: Any notes or instructions associated with the payment. Provide notes to convey extra details about the reason for the payment.
- `status`: The status of the transaction. For a list of possible values, see [`INPaymentStatus`](../inpaymentstatus.md).

## See Also

### Creating a Payment Record Object
- [init?(payee: INPerson?, payer: INPerson?, currencyAmount: INCurrencyAmount?, paymentMethod: INPaymentMethod?, note: String?, status: INPaymentStatus, feeAmount: INCurrencyAmount?)](./init%28payee,payer,currencyamount,paymentmethod,note,status,feeamount%29.md)
  Initializes a payment record with the specified payment details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentrecord/init(payee:payer:currencyamount:paymentmethod:note:status:))*