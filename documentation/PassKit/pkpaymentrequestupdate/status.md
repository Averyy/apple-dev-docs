# status

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The status of the payment request that indicates whether authorization succeeds or fails.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var status: PKPaymentAuthorizationStatus { get set }
```

```objc
@property (nonatomic, assign) PKPaymentAuthorizationStatus status;
```

#### Discussion

See [`PKPaymentAuthorizationStatus`](../pkpaymentauthorizationstatus.md) for valid values.

## See Also

### Updating authorization status
- [enum PKPaymentAuthorizationStatus](../pkpaymentauthorizationstatus.md)
  General success and failure status for payment authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequestupdate/status)*