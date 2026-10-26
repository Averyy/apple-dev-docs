# PKRadioTechnology

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct  
**Role**: Structure

Constants that describe the type of wireless radio technology that a pass uses.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS
- visionOS 1.0+
- watchOS 7.3+

## Declaration

```swift
struct PKRadioTechnology
```

```c
enum PKRadioTechnology : NSUInteger;
```

## Topics

### Reading the radio technology type
- [static var NFC: PKRadioTechnology](./pkradiotechnology/nfc.md)
  An identifier that indicates the near field communication (NFC) radio frequency communication technology.
- [static var bluetooth: PKRadioTechnology](./pkradiotechnology/bluetooth.md)
  An identifier that indicates the Bluetooth radio frequency communication technology.
### Creating a radio technology object
- [init(rawValue: UInt)](./pkradiotechnology/init%28rawvalue%29.md)
  Creates a radio technology object of the specified type.
### Enumeration Cases
- [PKRadioTechnologyNone](./pkradiotechnology/pkradiotechnologynone.md)
  An identifier that indicates the pass doesn’t use radio frequency communication.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Setting the wireless radio technology
- [var supportedRadioTechnologies: PKRadioTechnology](./pkaddcarkeypassconfiguration/supportedradiotechnologies.md)
  The wireless radio technology that the key uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkradiotechnology)*