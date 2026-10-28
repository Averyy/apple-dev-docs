# delegate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The view controller’s delegate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any PKPaymentAuthorizationViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<PKPaymentAuthorizationViewControllerDelegate> delegate;
```

## Discussion

The delegate is called at various points in the interaction, such as when the user selects shipping or billing information and when the user authorizes the payment request.

## See Also

### Handling user interactions
- [protocol PKPaymentAuthorizationViewControllerDelegate](../pkpaymentauthorizationviewcontrollerdelegate.md)
  Methods that let you respond to user interactions with your payment authorization view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/delegate)*