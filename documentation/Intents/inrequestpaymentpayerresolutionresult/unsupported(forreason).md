# unsupported(forReason:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution indicates that the specified value is not supported.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func unsupported(forReason reason: INRequestPaymentPayerUnsupportedReason) -> Self
```

```objc
+ (instancetype) unsupportedForReason:(INRequestPaymentPayerUnsupportedReason) reason;
```

## Return Value

A new [`INRequestPaymentPayerResolutionResult`](../inrequestpaymentpayerresolutionresult.md) object.

## Discussion

Use this method when the designated payer does not meet your qualifications for delivering a payment. For example, you might use this method if the user’s account does not have sufficient funds or you cant verify the user’s credentials.

## Parameters

- `reason`: The reason why the specified person is unsupported. For a list of possible values, see [`INRequestPaymentPayerUnsupportedReason`](../inrequestpaymentpayerunsupportedreason.md).

## See Also

### Creating a Resolution Result Object
- [enum INRequestPaymentPayerUnsupportedReason](../inrequestpaymentpayerunsupportedreason.md)
  Constants indicating the reason for being unable to resolve the provider of the funds.
- [init(personResolutionResult: INPersonResolutionResult)](./init%28personresolutionresult%29.md)
  Creates a resolution result object with the specified person resolution result object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentpayerresolutionresult/unsupported(forreason:))*