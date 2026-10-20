# init(paymentButtonType:paymentButtonStyle:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init  
**Role**: Initializer

Creates a new payment button with the specified type and style.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(paymentButtonType type: PKPaymentButtonType, paymentButtonStyle style: PKPaymentButtonStyle)
```

```objc
- (instancetype) initWithPaymentButtonType:(PKPaymentButtonType) type paymentButtonStyle:(PKPaymentButtonStyle) style;
```

#### Return Value

Returns a `PKPaymentButton` instance with the specified type and style.

## Parameters

- `type`: The button’s content. For a complete list of button types, see [`PKPaymentButtonType`](../pkpaymentbuttontype.md).
- `style`: The button’s appearance. For a complete list of button styles, see [`PKPaymentButtonStyle`](../pkpaymentbuttonstyle.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentbutton/init(paymentbuttontype:paymentbuttonstyle:))*