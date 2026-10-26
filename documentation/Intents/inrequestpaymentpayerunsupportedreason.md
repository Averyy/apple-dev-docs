# INRequestPaymentPayerUnsupportedReason

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the reason for being unable to resolve the provider of the funds.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum INRequestPaymentPayerUnsupportedReason
```

```c
enum INRequestPaymentPayerUnsupportedReason : NSInteger;
```

## Topics

### Constants
- [INRequestPaymentPayerUnsupportedReason.credentialsUnverified](./inrequestpaymentpayerunsupportedreason/credentialsunverified.md)
  The payer’s credentials are unverifiable.
- [INRequestPaymentPayerUnsupportedReason.noAccount](./inrequestpaymentpayerunsupportedreason/noaccount.md)
  The payer does not have an account in your app.
- [INRequestPaymentPayerUnsupportedReason.noValidHandle](./inrequestpaymentpayerunsupportedreason/novalidhandle.md)
  The unique handle that you use to identify the payer is invalid or missing.
### Initializers
- [init?(rawValue: Int)](./inrequestpaymentpayerunsupportedreason/init%28rawvalue%29.md)

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
- [class func unsupported(forReason: INRequestPaymentPayerUnsupportedReason) -> Self](./inrequestpaymentpayerresolutionresult/unsupported%28forreason%29.md)
  Creates an object whose resolution indicates that the specified value is not supported.
- [init(personResolutionResult: INPersonResolutionResult)](./inrequestpaymentpayerresolutionresult/init%28personresolutionresult%29.md)
  Creates a resolution result object with the specified person resolution result object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentpayerunsupportedreason)*