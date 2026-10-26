# INSendPaymentPayeeUnsupportedReason

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the reason for being unable to resolve the payee.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum INSendPaymentPayeeUnsupportedReason
```

```c
enum INSendPaymentPayeeUnsupportedReason : NSInteger;
```

## Topics

### Constants
- [INSendPaymentPayeeUnsupportedReason.credentialsUnverified](./insendpaymentpayeeunsupportedreason/credentialsunverified.md)
  The payee’s credentials are unverifiable.
- [INSendPaymentPayeeUnsupportedReason.insufficientFunds](./insendpaymentpayeeunsupportedreason/insufficientfunds.md)
  The current user’s account has insufficient funds to make the payment.
- [INSendPaymentPayeeUnsupportedReason.noAccount](./insendpaymentpayeeunsupportedreason/noaccount.md)
  The payee does not have an account in your app.
- [INSendPaymentPayeeUnsupportedReason.noValidHandle](./insendpaymentpayeeunsupportedreason/novalidhandle.md)
  The unique handle that you use to identify the payee is invalid or missing.
### Initializers
- [init?(rawValue: Int)](./insendpaymentpayeeunsupportedreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a Resolution Result Object
- [class func unsupported(forReason: INSendPaymentPayeeUnsupportedReason) -> Self](./insendpaymentpayeeresolutionresult/unsupported%28forreason%29.md)
  Creates an object whose resolution indicates that the specified value is not supported.
- [init(personResolutionResult: INPersonResolutionResult)](./insendpaymentpayeeresolutionresult/init%28personresolutionresult%29.md)
  Creates a resolution result object with the specified person resolution result object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendpaymentpayeeunsupportedreason)*