# addSecureElementPassViewController(_:didFinishAdding:error:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when PassKit finishes adding a Secure Element pass.

**Availability**:
- iOS 13.4+ - Deprecated in 14.0
- iPadOS 13.4+ - Deprecated in 14.0
- Mac Catalyst 13.4+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`addSecureElementPassViewController(_:didFinishAddingSecureElementPasses:error:)`](./addsecureelementpassviewcontroller%28_,didfinishaddingsecureelementpasses,error%29.md) instead.

## Declaration

```swift
optional func addSecureElementPassViewController(_ controller: PKAddSecureElementPassViewController, didFinishAdding pass: PKSecureElementPass?, error: (any Error)?)
```

```objc
- (void) addSecureElementPassViewController:(PKAddSecureElementPassViewController *) controller didFinishAddingSecureElementPass:(PKSecureElementPass *) pass error:(NSError *) error;
```

## Parameters

- `controller`: The view controller that requests PassKit to add a pass.
- `pass`: If addition succeeds, the Secure Element pass that PassKit adds; otherwise, `nil`.
- `error`: If addition fails, an error that describes the failure; otherwise, `nil`. See [`PKAddSecureElementPassError`](../pkaddsecureelementpasserror.md) for more information.

## See Also

### Responding to pass addition
- [func addSecureElementPassViewController(PKAddSecureElementPassViewController, didFinishAddingSecureElementPasses: [PKSecureElementPass]?, error: (any Error)?)](./addsecureelementpassviewcontroller%28_,didfinishaddingsecureelementpasses,error%29.md)
  Tells the delegate when PassKit finishes adding one or more Secure Element passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddsecureelementpassviewcontrollerdelegate/addsecureelementpassviewcontroller(_:didfinishadding:error:))*