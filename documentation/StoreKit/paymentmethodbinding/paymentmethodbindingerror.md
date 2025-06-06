# PaymentMethodBinding.PaymentMethodBindingError

**Framework**: StoreKit  
**Kind**: enum

Error information for payment method binding.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- visionOS 1.0+

## Declaration

```swift
enum PaymentMethodBindingError
```

#### Overview

The methods of [`PaymentMethodBinding`](paymentmethodbinding.md) may return these errors, as well as the [`StoreKitError.userCancelled`](storekiterror/usercancelled.md) error.

## Topics

### Getting error codes
- [PaymentMethodBinding.PaymentMethodBindingError.failed](paymentmethodbinding/paymentmethodbindingerror/failed.md)
  The initialization or binding operation failed.
- [PaymentMethodBinding.PaymentMethodBindingError.invalidPinningID](paymentmethodbinding/paymentmethodbindingerror/invalidpinningid.md)
  The in-app binding identifier is invalid or expired.
- [PaymentMethodBinding.PaymentMethodBindingError.notEligible](paymentmethodbinding/paymentmethodbindingerror/noteligible.md)
  The user isn’t eligible.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/paymentmethodbinding/paymentmethodbindingerror)*