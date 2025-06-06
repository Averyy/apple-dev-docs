# PaymentMethodBinding.PaymentMethodBindingError.failed

**Framework**: StoreKit  
**Kind**: case

The initialization or binding operation failed.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- visionOS 1.0+

## Declaration

```swift
case failed
```

#### Discussion

The methods of the [`PaymentMethodBinding`](paymentmethodbinding.md) struct can fail if the app isn’t entitled to use this API, or if other errors occur.

## See Also

- [PaymentMethodBinding.PaymentMethodBindingError.invalidPinningID](paymentmethodbinding/paymentmethodbindingerror/invalidpinningid.md)
  The in-app binding identifier is invalid or expired.
- [PaymentMethodBinding.PaymentMethodBindingError.notEligible](paymentmethodbinding/paymentmethodbindingerror/noteligible.md)
  The user isn’t eligible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/paymentmethodbinding/paymentmethodbindingerror/failed)*