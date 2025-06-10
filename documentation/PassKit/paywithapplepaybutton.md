# PayWithApplePayButton

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency struct PayWithApplePayButton<Fallback> where Fallback : View
```

## Topics

### Creating the button
- [init(PayWithApplePayButtonLabel, action: () -> Void)](paywithapplepaybutton/init(_:action:).md)
- [init(PayWithApplePayButtonLabel, action: () -> Void, fallback: () -> Fallback)](paywithapplepaybutton/init(_:action:fallback:).md)
- [init(PayWithApplePayButtonLabel, request: PKPaymentRequest, onPaymentAuthorizationChange: (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void)](paywithapplepaybutton/init(_:request:onpaymentauthorizationchange:).md)
- [init(PayWithApplePayButtonLabel, request: PKPaymentRequest, onPaymentAuthorizationChange: (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void, fallback: () -> Fallback)](paywithapplepaybutton/init(_:request:onpaymentauthorizationchange:fallback:).md)
- [init(PayWithApplePayButtonLabel, request: PKPaymentRequest, onPaymentAuthorizationChange: (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void, onMerchantSessionRequested: () async -> PKPaymentRequestMerchantSessionUpdate)](paywithapplepaybutton/init(_:request:onpaymentauthorizationchange:onmerchantsessionrequested:).md)
- [init(PayWithApplePayButtonLabel, request: PKPaymentRequest, onPaymentAuthorizationChange: (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void, onMerchantSessionRequested: () async -> PKPaymentRequestMerchantSessionUpdate, fallback: () -> Fallback)](paywithapplepaybutton/init(_:request:onpaymentauthorizationchange:onmerchantsessionrequested:fallback:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [class PKPaymentButton](pkpaymentbutton.md)
  An object that displays a button either to trigger payments through Apple Pay or to prompt the user to set up a card.
- [struct PayWithApplePayButtonLabel](paywithapplepaybuttonlabel.md)
- [struct PayWithApplePayButtonStyle](paywithapplepaybuttonstyle.md)
- [struct PayWithApplePayButtonLabel](paywithapplepaybuttonlabel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/paywithapplepaybutton)*