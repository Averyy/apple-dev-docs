# init(_:action:fallback:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init(_ label: PayWithApplePayButtonLabel = .plain, action: @escaping () -> Void, @ViewBuilder fallback: () -> Fallback)
```

## See Also

- [init(PayWithApplePayButtonLabel, action: () -> Void)](paywithapplepaybutton/init(_:action:).md)
- [init(PayWithApplePayButtonLabel, request: PKPaymentRequest, onPaymentAuthorizationChange: (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void)](paywithapplepaybutton/init(_:request:onpaymentauthorizationchange:).md)
- [init(PayWithApplePayButtonLabel, request: PKPaymentRequest, onPaymentAuthorizationChange: (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void, fallback: () -> Fallback)](paywithapplepaybutton/init(_:request:onpaymentauthorizationchange:fallback:).md)
- [init(PayWithApplePayButtonLabel, request: PKPaymentRequest, onPaymentAuthorizationChange: (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void, onMerchantSessionRequested: () async -> PKPaymentRequestMerchantSessionUpdate)](paywithapplepaybutton/init(_:request:onpaymentauthorizationchange:onmerchantsessionrequested:).md)
- [init(PayWithApplePayButtonLabel, request: PKPaymentRequest, onPaymentAuthorizationChange: (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void, onMerchantSessionRequested: () async -> PKPaymentRequestMerchantSessionUpdate, fallback: () -> Fallback)](paywithapplepaybutton/init(_:request:onpaymentauthorizationchange:onmerchantsessionrequested:fallback:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/paywithapplepaybutton/init(_:action:fallback:))*