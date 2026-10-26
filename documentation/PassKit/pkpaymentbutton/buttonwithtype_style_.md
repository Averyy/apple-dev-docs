# buttonWithType:style:

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Type Method

Creates a new payment button with the specified type and style.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) buttonWithType:(PKPaymentButtonType) buttonType style:(PKPaymentButtonStyle) buttonStyle;
```

#### Return Value

Returns a `PKPaymentButton` instance with the specified type and style.

#### Discussion

Use the returned button to trigger a purchase through Apple Pay. Add the button instance to your view hierarchy, and then set its [Target-Action](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/TargetAction.html#//apple_ref/doc/uid/TP40009071-CH3) by calling its [`addTarget(_:action:for:)`](../../UIKit/uicontrol/addtarget%28_,action,for%29.md) method. In the action method, create the payment request and present the payment authorization view controller. These buttons can be used only to initiate Apple Pay transactions.

Do not display a button smaller than its intrinsic content size. You can extend the button’s width to fit your layout, but do not reduce the width or change the button’s height.

For more information on using Apple Pay, see [Apple Pay Programming Guide](https://developer.apple.com/library/archive/ApplePay_Guide/index.html#//apple_ref/doc/uid/TP40014764).

## Parameters

- `buttonType`: The button’s content. For a complete list of button types, see [`PKPaymentButtonType`](../pkpaymentbuttontype.md).
- `buttonStyle`: The button’s appearance. For a complete list of button styles, see [`PKPaymentButtonStyle`](../pkpaymentbuttonstyle.md).

## See Also

### Creating payment buttons
- [init(paymentButtonType: PKPaymentButtonType, paymentButtonStyle: PKPaymentButtonStyle)](./init%28paymentbuttontype,paymentbuttonstyle%29.md)
  Creates a new payment button with the specified type and style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentbutton/buttonwithtype:style:)*