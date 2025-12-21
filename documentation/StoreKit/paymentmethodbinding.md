# PaymentMethodBinding

**Framework**: StoreKit  
**Kind**: struct

A binding that makes payment methods available in apps for an Apple Account.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- visionOS 1.0+

## Declaration

```swift
struct PaymentMethodBinding
```

#### Overview

This functionality is available only to eligible apps with server entitlements. The initializer [`init(id:)`](paymentmethodbinding/init(id:).md) throws an error if your app doesn’t have the appropriate entitlement to use this API, or if the user isn’t eligible.

> ❗ **Important**:  The [`init(id:)`](paymentmethodbinding/init(id:).md) and [`bind()`](paymentmethodbinding/bind().md) methods may display a system prompt that asks users to authenticate with their Apple Account. Call these methods only after an explicit user action, like tapping or clicking a button.

Initialize this structure using the in-app binding identifier that your server receives from the Apple server when your server initiates payment method binding. Call the [`bind()`](paymentmethodbinding/bind().md) method to prompt users to confirm adding the payment method and making it their primary payment method.

## Topics

### Determining eligiblity
- [init(id: String) async throws](paymentmethodbinding/init(id:).md)
  Creates the payment method binding for eligible apps and users.
### Creating and identifying bindings
- [let id: String](paymentmethodbinding/id.md)
  The in-app binding identifier.
### Binding payment methods
- [func bind() async throws](paymentmethodbinding/bind.md)
  Asks the user to confirm whether to add the payment method to their Apple payment methods.
### Reading errors
- [PaymentMethodBinding.PaymentMethodBindingError](paymentmethodbinding/paymentmethodbindingerror.md)
  Error information for payment method binding.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/paymentmethodbinding)*