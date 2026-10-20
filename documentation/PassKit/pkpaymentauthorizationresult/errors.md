# errors

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

List of errors in the Apple Pay sheet.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var errors: [any Error]! { get set }
```

```objc
@property (nonatomic, copy, null_resettable) NSArray<NSError *> * errors;
```

#### Discussion

If the Apple Pay sheet contains errors, you provide a [`PKPaymentAuthorizationStatus.failure`](../pkpaymentauthorizationstatus/failure.md) status to [`PKPaymentAuthorizationResult`](../pkpaymentauthorizationresult.md), and include the individual errors in this array. If there are no errors, you provide a [`PKPaymentAuthorizationStatus.success`](../pkpaymentauthorizationstatus/success.md) status and leave the error array empty. Errors are of the standard type, [`NSError`](../../Foundation/nserror.md). To create errors, you can either use the convenience methods found in [`PKPaymentRequest`](../pkpaymentrequest.md), or create an [`NSError`](../../Foundation/nserror.md) using the domain, error codes, and user info from [`PKPaymentError`](../pkpaymenterror.md).

Add the errors to the array in order of severity, with the most important error first.

## See Also

### Setting payment authorization status and errors
- [var status: PKPaymentAuthorizationStatus](./status.md)
  Payment authorization general status.
- [enum PKPaymentAuthorizationStatus](../pkpaymentauthorizationstatus.md)
  General success and failure status for payment authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationresult/errors)*