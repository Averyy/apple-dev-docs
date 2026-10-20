# init(_:request:onPaymentAuthorizationChange:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
nonisolated
init(_ label: PayWithApplePayButtonLabel = .plain, request: PKPaymentRequest, onPaymentAuthorizationChange: @escaping (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void)
```

Available when `Fallback` is `EmptyView`.

## See Also

### Creating the button
- [init(PayWithApplePayButtonLabel, action: () -> Void)](./init%28_,action%29.md)
- [init(PayWithApplePayButtonLabel, action: () -> Void, fallback: () -> Fallback)](./init%28_,action,fallback%29.md)
- [init(PayWithApplePayButtonLabel, request: PKPaymentRequest, onPaymentAuthorizationChange: (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void, fallback: () -> Fallback)](./init%28_,request,onpaymentauthorizationchange,fallback%29.md)
- [init(PayWithApplePayButtonLabel, request: PKPaymentRequest, onPaymentAuthorizationChange: (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void, onMerchantSessionRequested: () async -> PKPaymentRequestMerchantSessionUpdate)](./init%28_,request,onpaymentauthorizationchange,onmerchantsessionrequested%29.md)
- [init(PayWithApplePayButtonLabel, request: PKPaymentRequest, onPaymentAuthorizationChange: (PayWithApplePayButtonPaymentAuthorizationPhase) -> Void, onMerchantSessionRequested: () async -> PKPaymentRequestMerchantSessionUpdate, fallback: () -> Fallback)](./init%28_,request,onpaymentauthorizationchange,onmerchantsessionrequested,fallback%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/paywithapplepaybutton/init(_:request:onpaymentauthorizationchange:))*