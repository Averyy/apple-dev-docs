# presentationWindow(for:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Required**: Yes

Returns the window in which to present a payment authorization sheet.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
optional func presentationWindow(for controller: PKPaymentAuthorizationController) -> UIWindow?
```

#### Return Value

The window in which to present the payment authorization sheet.

## Parameters

- `controller`: The controller for the payment authorization sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/presentationwindow(for:))*