# delegate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The object that acts as the delegate for the add payment view controller.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any PKAddPaymentPassViewControllerDelegate)? { get set }
```

## See Also

- [protocol PKAddPaymentPassViewControllerDelegate](pkaddpaymentpassviewcontrollerdelegate.md)
  Methods that let the system prompt you for an add payment request, and inform you when a request has succeeded or failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontroller/delegate)*