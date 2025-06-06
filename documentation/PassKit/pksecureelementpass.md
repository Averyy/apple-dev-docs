# PKSecureElementPass

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

A pass with a credential that the device stores in a certified payment information chip.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
class PKSecureElementPass
```

## Topics

### Getting the activation state
- [var passActivationState: PKSecureElementPass.PassActivationState](pksecureelementpass/passactivationstate-swift.property.md)
  The activation state of the pass.
- [PKSecureElementPass.PassActivationState](pksecureelementpass/passactivationstate-swift.enum.md)
  The activation states of a Secure Element pass.
### Getting the hardware attributes
- [var deviceAccountIdentifier: String](pksecureelementpass/deviceaccountidentifier.md)
  The unique identifier for the device-specific account number.
- [var deviceAccountNumberSuffix: String](pksecureelementpass/deviceaccountnumbersuffix.md)
  A display-ready version of the device-specific account number.
- [var devicePassIdentifier: String?](pksecureelementpass/devicepassidentifier.md)
  An opaque value for the pass.
- [var pairedTerminalIdentifier: String?](pksecureelementpass/pairedterminalidentifier.md)
  The unique identifier of the paired terminal.
### Getting the account attributes
- [var primaryAccountIdentifier: String](pksecureelementpass/primaryaccountidentifier.md)
  An opaque value that identifies the primary account number that funds the pass’s transactions.
- [var primaryAccountNumberSuffix: String](pksecureelementpass/primaryaccountnumbersuffix.md)
  A display-ready version of the primary account number.

## Relationships

### Inherits From
- [PKPass](pkpass.md)
### Inherited By
- [PKPaymentPass](pkpaymentpass.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

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
- [protocol PKShareSecureElementPassViewControllerDelegate](pksharesecureelementpassviewcontrollerdelegate.md)
- [PKShareablePassMetadata.Preview](pkshareablepassmetadata/preview-swift.class.md)
- [enum PKShareSecureElementPassResult](pksharesecureelementpassresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksecureelementpass)*