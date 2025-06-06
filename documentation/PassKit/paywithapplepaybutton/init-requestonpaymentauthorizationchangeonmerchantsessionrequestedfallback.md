# init(_:request:onPaymentAuthorizationChange:onMerchantSessionRequested:fallback:)

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
init(_ label: PayWithApplePayButtonLabel = .plain, request: PKPaymentRequest, onPaymentAuthorizationChange: @escaping (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void, onMerchantSessionRequested: @escaping () async -> PKPaymentRequestMerchantSessionUpdate, @ViewBuilder fallback: () -> Fallback)
```

## See Also

- [init(PayWithApplePayButtonLabel, action: () -> Void)](paywithapplepaybutton/init(_:action:).md)
- [init(PayWithApplePayButtonLabel, action: () -> Void, fallback: () -> Fallback)](paywithapplepaybutton/init(_:action:fallback:).md)
- [init(PayWithApplePayButtonLabel, request: PKPaymentRequest, onPaymentAuthorizationChange: (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void)](paywithapplepaybutton/init(_:request:onpaymentauthorizationchange:).md)
- [init(PayWithApplePayButtonLabel, request: PKPaymentRequest, onPaymentAuthorizationChange: (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void, fallback: () -> Fallback)](paywithapplepaybutton/init(_:request:onpaymentauthorizationchange:fallback:).md)
- [init(PayWithApplePayButtonLabel, request: PKPaymentRequest, onPaymentAuthorizationChange: (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void, onMerchantSessionRequested: () async -> PKPaymentRequestMerchantSessionUpdate)](paywithapplepaybutton/init(_:request:onpaymentauthorizationchange:onmerchantsessionrequested:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/paywithapplepaybutton/init(_:request:onpaymentauthorizationchange:onmerchantsessionrequested:fallback:))*