# PKPaymentMerchantSession

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

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

```objc
@interface PKPaymentMerchantSession : NSObject
```

## Topics

### Creating a merchant session
- [init(dictionary: [AnyHashable : Any])](./pkpaymentmerchantsession/init%28dictionary%29.md)
  Creates an object that validates the identity of a merchant for a payment request.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Getting information for the merchant session update
- [var status: PKPaymentAuthorizationStatus](./pkpaymentrequestmerchantsessionupdate/status.md)
  The current authorization status for the payment.
- [var session: PKPaymentMerchantSession?](./pkpaymentrequestmerchantsessionupdate/session.md)
  An object that validates the identity of a merchant for the payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentmerchantsession)*