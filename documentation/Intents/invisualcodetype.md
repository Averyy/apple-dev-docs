# INVisualCodeType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the purpose of the visual code.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
enum INVisualCodeType
```

```c
enum INVisualCodeType : NSInteger;
```

## Topics

### General Types
- [INVisualCodeType.unknown](./invisualcodetype/unknown.md)
  An unknown type of visual code.
- [INVisualCodeType.contact](./invisualcodetype/contact.md)
  A visual code providing the user’s contact information.
### Payment Types
- [INVisualCodeType.requestPayment](./invisualcodetype/requestpayment.md)
  A visual code for requesting a payment.
- [INVisualCodeType.sendPayment](./invisualcodetype/sendpayment.md)
  A visual code for making a payment.
### Transportation Types
- [INVisualCodeType.bus](./invisualcodetype/bus.md)
  A visual code for bus transportation.
- [INVisualCodeType.subway](./invisualcodetype/subway.md)
  A visual code for subway transportation.
- [INVisualCodeType.transit](./invisualcodetype/transit.md)
  A visual code for public transit.
### Initializers
- [init?(rawValue: Int)](./invisualcodetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Visual Code Type
- [var visualCodeType: INVisualCodeType](./ingetvisualcodeintent/visualcodetype.md)
  The type of visual code requested by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invisualcodetype)*