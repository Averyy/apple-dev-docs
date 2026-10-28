# presentationWindow(for:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Returns the window in which to present a payment authorization sheet.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, watchOS*

```swift
optional func presentationWindow(for controller: PKPaymentAuthorizationController) -> UIWindow?
```

*Mac Catalyst, visionOS*

```swift
func presentationWindow(for controller: PKPaymentAuthorizationController) -> UIWindow?
```

*macOS*

```swift
func presentationWindow(for controller: PKPaymentAuthorizationController) -> NSWindow?
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
- (UIWindow *) presentationWindowForPaymentAuthorizationController:(PKPaymentAuthorizationController *) controller;
```

*macOS*

```objc
- (NSWindow *) presentationWindowForPaymentAuthorizationController:(PKPaymentAuthorizationController *) controller;
```

## Return Value

The window in which to present the payment authorization sheet.

## Parameters

- `controller`: The controller for the payment authorization sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/presentationwindow(for:))*