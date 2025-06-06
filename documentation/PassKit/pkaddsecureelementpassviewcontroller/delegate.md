# delegate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

An object that acts as the view controller’s delegate.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any PKAddSecureElementPassViewControllerDelegate)? { get set }
```

#### Discussion

The delegate must adopt the [`PKAddSecureElementPassViewControllerDelegate`](pkaddsecureelementpassviewcontrollerdelegate.md) protocol. The view controller doesn’t retain the delegate.

## See Also

- [protocol PKAddSecureElementPassViewControllerDelegate](pkaddsecureelementpassviewcontrollerdelegate.md)
  The methods for responding to the life cycle events of a Secure Element pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddsecureelementpassviewcontroller/delegate)*