# init(payer:currencyAmount:note:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the request payment intent object with the specified recipient and payment information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
init(payer: INPerson?, currencyAmount: INCurrencyAmount?, note: String?)
```

```objc
- (instancetype) initWithPayer:(INPerson *) payer currencyAmount:(INCurrencyAmount *) currencyAmount note:(NSString *) note;
```

#### Return Value

An initialized intent or `nil` if the object could not be created.

#### Discussion

Normally, you do not create instances of this class yourself. Instead, SiriKit creates instances when the user makes a payment request to another person. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `payer`: The person receiving the payment request.
- `currencyAmount`: The amount of money being requested from the `payer`.
- `note`: A note to include with the request. Use this parameter to convey the reason for the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentintent/init(payer:currencyamount:note:))*