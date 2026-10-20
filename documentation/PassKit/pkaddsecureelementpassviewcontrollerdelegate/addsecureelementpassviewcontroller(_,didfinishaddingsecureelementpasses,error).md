# addSecureElementPassViewController(_:didFinishAddingSecureElementPasses:error:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) addSecureElementPassViewController:(PKAddSecureElementPassViewController *) controller didFinishAddingSecureElementPasses:(NSArray<PKSecureElementPass *> *) passes error:(NSError *) error;
```

## Parameters

- `controller`: The view controller that requests PassKit to add passes.
- `passes`: If addition succeeds, the array of Secure Element passes that PassKit adds; otherwise, `nil`.
- `error`: If addition fails, an error that describes the failure; otherwise, `nil`. See [`PKAddSecureElementPassError`](../pkaddsecureelementpasserror.md) for more information.

## See Also

### Responding to pass addition
- [func addSecureElementPassViewController(PKAddSecureElementPassViewController, didFinishAdding: PKSecureElementPass?, error: (any Error)?)](./addsecureelementpassviewcontroller%28_,didfinishadding,error%29.md)
  Tells the delegate when PassKit finishes adding a Secure Element pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddsecureelementpassviewcontrollerdelegate/addsecureelementpassviewcontroller(_:didfinishaddingsecureelementpasses:error:))*