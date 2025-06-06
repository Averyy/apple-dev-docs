# PKShareSecureElementPassViewControllerDelegate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: protocol

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol PKShareSecureElementPassViewControllerDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func shareSecureElementPassViewController(PKShareSecureElementPassViewController, didCreateShare: URL?, activationCode: String?)](pksharesecureelementpassviewcontrollerdelegate/sharesecureelementpassviewcontroller(_:didcreateshare:activationcode:).md)
- [func shareSecureElementPassViewController(PKShareSecureElementPassViewController, didFinishWith: PKShareSecureElementPassResult)](pksharesecureelementpassviewcontrollerdelegate/sharesecureelementpassviewcontroller(_:didfinishwith:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PKSecureElementPass](pksecureelementpass.md)
  A pass with a credential that the device stores in a certified payment information chip.
- [class PKAddSecureElementPassConfiguration](pkaddsecureelementpassconfiguration.md)
  An object that describes the configuration of a secure element payment pass.
- [class PKAddSecureElementPassViewController](pkaddsecureelementpassviewcontroller.md)
  A view controller that manages the addition of secure element payment passes.
- [class PKPass](pkpass.md)
  An object that represents a single pass.
- [class PKAddPassesViewController](pkaddpassesviewcontroller.md)
  Lets your app show a pass and prompt the user to add that pass to the pass library.
- [struct AsyncShareablePassConfiguration](asyncshareablepassconfiguration.md)
- [class PKShareSecureElementPassViewController](pksharesecureelementpassviewcontroller.md)
- [PKShareablePassMetadata.Preview](pkshareablepassmetadata/preview-swift.class.md)
- [enum PKShareSecureElementPassResult](pksharesecureelementpassresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksharesecureelementpassviewcontrollerdelegate)*