# PKAddSecureElementPassViewControllerDelegate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: protocol  
**Role**: Protocol

The methods for responding to the life cycle events of a Secure Element pass.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
protocol PKAddSecureElementPassViewControllerDelegate : NSObjectProtocol
```

```objc
@protocol PKAddSecureElementPassViewControllerDelegate <NSObject>
```

## Topics

### Responding to pass addition
- [func addSecureElementPassViewController(PKAddSecureElementPassViewController, didFinishAddingSecureElementPasses: [PKSecureElementPass]?, error: (any Error)?)](./pkaddsecureelementpassviewcontrollerdelegate/addsecureelementpassviewcontroller%28_,didfinishaddingsecureelementpasses,error%29.md)
  Tells the delegate when PassKit finishes adding one or more Secure Element passes.
- [func addSecureElementPassViewController(PKAddSecureElementPassViewController, didFinishAdding: PKSecureElementPass?, error: (any Error)?)](./pkaddsecureelementpassviewcontrollerdelegate/addsecureelementpassviewcontroller%28_,didfinishadding,error%29.md)
  Tells the delegate when PassKit finishes adding a Secure Element pass.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to the life cycle of a pass
- [var delegate: (any PKAddSecureElementPassViewControllerDelegate)?](./pkaddsecureelementpassviewcontroller/delegate.md)
  An object that acts as the view controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddsecureelementpassviewcontrollerdelegate)*