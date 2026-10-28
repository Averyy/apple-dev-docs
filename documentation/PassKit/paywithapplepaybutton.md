# PayWithApplePayButton

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct  
**Role**: Structure

A type that provides a button to pay with Apple pay.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency struct PayWithApplePayButton<Fallback> where Fallback : View
```

## Overview

Use this structure as the SwiftUI equivalent to [`PKPaymentButton`](./pkpaymentbutton.md). For design guidance, see Human Interface Guidelines > Apple Pay > [Using Apple Pay buttons](https://developer.apple.com/design/human-interface-guidelines/apple-pay#Using-Apple-Pay-buttons).

This example shows an implementation of the Pay with Apple Pay button.

```swift
// Create a payment request.
@State private var paymentRequest = PKPaymentRequest()

// Create a payment authorization change method.
func paymentAuthorizationDidChange(phase: PayWithApplePayButtonPaymentAuthorizationPhase) { ... }

@ViewBuilder var payButton: some View {
    PayWithApplePayButton(
        .plain,
        request: paymentRequest,
        onPaymentAuthorizationChange: paymentAuthorizationDidChange
    ) {
        // Display a fallback view if the payment request fails.
    }
    .frame(width: 250, height: 50)
    .payWithApplePayButtonStyle(.automatic)
}
```

## Topics

### Creating the button
- [init(PayWithApplePayButtonLabel, action: () -> Void)](./paywithapplepaybutton/init%28_,action%29.md)
- [init(PayWithApplePayButtonLabel, action: () -> Void, fallback: () -> Fallback)](./paywithapplepaybutton/init%28_,action,fallback%29.md)
- [init(PayWithApplePayButtonLabel, request: PKPaymentRequest, onPaymentAuthorizationChange: (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void)](./paywithapplepaybutton/init%28_,request,onpaymentauthorizationchange%29.md)
- [init(PayWithApplePayButtonLabel, request: PKPaymentRequest, onPaymentAuthorizationChange: (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void, fallback: () -> Fallback)](./paywithapplepaybutton/init%28_,request,onpaymentauthorizationchange,fallback%29.md)
- [init(PayWithApplePayButtonLabel, request: PKPaymentRequest, onPaymentAuthorizationChange: (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void, onMerchantSessionRequested: () async -> PKPaymentRequestMerchantSessionUpdate)](./paywithapplepaybutton/init%28_,request,onpaymentauthorizationchange,onmerchantsessionrequested%29.md)
- [init(PayWithApplePayButtonLabel, request: PKPaymentRequest, onPaymentAuthorizationChange: (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void, onMerchantSessionRequested: () async -> PKPaymentRequestMerchantSessionUpdate, fallback: () -> Fallback)](./paywithapplepaybutton/init%28_,request,onpaymentauthorizationchange,onmerchantsessionrequested,fallback%29.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)

## See Also

### Apple Pay buttons
- [class PKPaymentButton](./pkpaymentbutton.md)
  An object that displays a button either to trigger payments through Apple Pay or to prompt the user to set up a card.
- [struct PayWithApplePayButtonLabel](./paywithapplepaybuttonlabel.md)
- [struct PayWithApplePayButtonStyle](./paywithapplepaybuttonstyle.md)
- [struct PayWithApplePayButtonLabel](./paywithapplepaybuttonlabel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/paywithapplepaybutton)*