# delegate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The view controller’s delegate.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any PKAddPassesViewControllerDelegate)? { get set }
```

#### Discussion

For information about the protocol that the delegate must implement, see [`PKAddPassesViewControllerDelegate`](pkaddpassesviewcontrollerdelegate.md).

## See Also

- [protocol PKAddPassesViewControllerDelegate](pkaddpassesviewcontrollerdelegate.md)
  Methods that an add-passes view controller’s delegate implements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontroller/delegate)*