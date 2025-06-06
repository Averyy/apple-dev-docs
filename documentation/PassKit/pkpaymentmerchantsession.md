# PKPaymentMerchantSession

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that validates the identity of a merchant for a payment request.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class PKPaymentMerchantSession
```

## Topics

### Creating a merchant session
- [init(dictionary: [AnyHashable : Any])](pkpaymentmerchantsession/init(dictionary:).md)
  Creates an object that validates the identity of a merchant for a payment request.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var status: PKPaymentAuthorizationStatus](pkpaymentrequestmerchantsessionupdate/status.md)
  The current authorization status for the payment.
- [var session: PKPaymentMerchantSession?](pkpaymentrequestmerchantsessionupdate/session.md)
  An object that validates the identity of a merchant for the payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentmerchantsession)*