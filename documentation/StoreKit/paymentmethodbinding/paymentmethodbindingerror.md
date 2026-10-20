# PaymentMethodBinding.PaymentMethodBindingError

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

Error information for payment method binding.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- visionOS 1.0+

## Declaration

```swift
enum PaymentMethodBindingError
```

#### Overview

The methods of [`PaymentMethodBinding`](../paymentmethodbinding.md) may return these errors, as well as the [`StoreKitError.userCancelled`](../storekiterror/usercancelled.md) error.

## Topics

### Getting error codes
- [PaymentMethodBinding.PaymentMethodBindingError.failed](./paymentmethodbindingerror/failed.md)
  The initialization or binding operation failed.
- [PaymentMethodBinding.PaymentMethodBindingError.invalidPinningID](./paymentmethodbindingerror/invalidpinningid.md)
  The in-app binding identifier is invalid or expired.
- [PaymentMethodBinding.PaymentMethodBindingError.notEligible](./paymentmethodbindingerror/noteligible.md)
  The user isn’t eligible.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/paymentmethodbinding/paymentmethodbindingerror)*