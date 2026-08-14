# PKRadioTechnology

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

Constants that describe the type of wireless radio technology that a pass uses.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS ?+
- visionOS 1.0+
- watchOS 7.3+

## Declaration

```swift
struct PKRadioTechnology
```

## Topics

### Reading the radio technology type
- [static var NFC: PKRadioTechnology](pkradiotechnology/nfc.md)
  An identifier that indicates the near field communication (NFC) radio frequency communication technology.
- [static var bluetooth: PKRadioTechnology](pkradiotechnology/bluetooth.md)
  An identifier that indicates the Bluetooth radio frequency communication technology.
### Creating a radio technology object
- [init(rawValue: UInt)](pkradiotechnology/init(rawvalue:).md)
  Creates a radio technology object of the specified type.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [var supportedRadioTechnologies: PKRadioTechnology](pkaddcarkeypassconfiguration/supportedradiotechnologies.md)
  The wireless radio technology that the key uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkradiotechnology)*