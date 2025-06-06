# PKLabeledValue

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that can represent a detail about a payment card or other item.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 3.1+

## Declaration

```swift
class PKLabeledValue
```

#### Overview

See [`cardDetails`](pkaddpaymentpassrequestconfiguration/carddetails.md).

## Topics

### Creating a labeled value
- [init(label: String, value: String)](pklabeledvalue/init(label:value:).md)
  Instantiates a new labeled value object with the specified label and value strings.
### Labeled value properties
- [var label: String](pklabeledvalue/label.md)
  A string that contains the label for the value.
- [var value: String](pklabeledvalue/value.md)
  A string that contains the value associated with a label.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PKObject](pkobject.md)
  An opaque type that acts as the superclass for the pass object.
- [class PKAddPassButton](pkaddpassbutton.md)
  Provides a button that enables users to add passes to Wallet.
- [struct AddPassToWalletButton](addpasstowalletbutton.md)
- [struct AddPassToWalletButtonFilter](addpasstowalletbuttonfilter.md)
- [struct AddPassToWalletButtonResponse](addpasstowalletbuttonresponse.md)
- [struct AddPassToWalletButtonStyle](addpasstowalletbuttonstyle.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pklabeledvalue)*