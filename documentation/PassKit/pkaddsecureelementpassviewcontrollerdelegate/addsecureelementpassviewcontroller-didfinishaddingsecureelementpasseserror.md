# addSecureElementPassViewController(_:didFinishAddingSecureElementPasses:error:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Required**: Yes

Tells the delegate when PassKit finishes adding one or more Secure Element passes.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
func addSecureElementPassViewController(_ controller: PKAddSecureElementPassViewController, didFinishAddingSecureElementPasses passes: [PKSecureElementPass]?, error: (any Error)?)
```

## Parameters

- `controller`: The view controller that requests PassKit to add passes.
- `passes`: If addition succeeds, the array of Secure Element passes that PassKit adds; otherwise,  .
- `error`: If addition fails, an error that describes the failure; otherwise,  . See   for more information.

## See Also

- [func addSecureElementPassViewController(PKAddSecureElementPassViewController, didFinishAdding: PKSecureElementPass?, error: (any Error)?)](pkaddsecureelementpassviewcontrollerdelegate/addsecureelementpassviewcontroller(_:didfinishadding:error:).md)
  Tells the delegate when PassKit finishes adding a Secure Element pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddsecureelementpassviewcontrollerdelegate/addsecureelementpassviewcontroller(_:didfinishaddingsecureelementpasses:error:))*