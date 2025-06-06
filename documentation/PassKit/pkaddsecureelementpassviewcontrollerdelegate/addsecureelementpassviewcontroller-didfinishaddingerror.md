# addSecureElementPassViewController(_:didFinishAdding:error:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Tells the delegate when PassKit finishes adding a Secure Element pass.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
optional func addSecureElementPassViewController(_ controller: PKAddSecureElementPassViewController, didFinishAdding pass: PKSecureElementPass?, error: (any Error)?)
```

## Parameters

- `controller`: The view controller that requests PassKit to add a pass.
- `pass`: If addition succeeds, the Secure Element pass that PassKit adds; otherwise,  .
- `error`: If addition fails, an error that describes the failure; otherwise,  . See   for more information.

## See Also

- [func addSecureElementPassViewController(PKAddSecureElementPassViewController, didFinishAddingSecureElementPasses: [PKSecureElementPass]?, error: (any Error)?)](pkaddsecureelementpassviewcontrollerdelegate/addsecureelementpassviewcontroller(_:didfinishaddingsecureelementpasses:error:).md)
  Tells the delegate when PassKit finishes adding one or more Secure Element passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddsecureelementpassviewcontrollerdelegate/addsecureelementpassviewcontroller(_:didfinishadding:error:))*