# PKAddSecureElementPassConfiguration

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that describes the configuration of a secure element payment pass.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
class PKAddSecureElementPassConfiguration
```

#### Overview

This class supports identity document configuration.

## Topics

### Managing the issuer identity
- [var issuerIdentifier: String?](pkaddsecureelementpassconfiguration/issueridentifier.md)
  An opaque value for the configuration.
- [var localizedDescription: String?](pkaddsecureelementpassconfiguration/localizeddescription.md)
  The configuration’s localized description.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [PKAddCarKeyPassConfiguration](pkaddcarkeypassconfiguration.md)
- [PKAddIdentityDocumentConfiguration](pkaddidentitydocumentconfiguration.md)
- [PKAddShareablePassConfiguration](pkaddshareablepassconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PKSecureElementPass](pksecureelementpass.md)
  A pass with a credential that the device stores in a certified payment information chip.
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

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddsecureelementpassconfiguration)*