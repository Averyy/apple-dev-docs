# init(requestConfiguration:delegate:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Returns an initialized add payment view controller object, using the provided configuration and delegate.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init?(requestConfiguration configuration: PKAddPaymentPassRequestConfiguration, delegate: (any PKAddPaymentPassViewControllerDelegate)?)
```

#### Return Value

A newly initialized add payment view controller.

#### Discussion

Adding payment passes requires a special entitlement issued by Apple. If your app does not include this entitlement, this method returns `nil`. For more information on requesting this entitlement, see the Card Issuers section on [`developer.apple.com/apple-pay/`](https://developer.apple.comhttps://developer.apple.com/apple-pay/).

## Parameters

- `configuration`: A configuration object that defines the view controller’s appearance.
- `delegate`: The add payment view controller’s delegate.

## See Also

- [class PKAddPaymentPassRequestConfiguration](pkaddpaymentpassrequestconfiguration.md)
  Contains the configuration data for a view controller that lets the user add a payment pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontroller/init(requestconfiguration:delegate:))*