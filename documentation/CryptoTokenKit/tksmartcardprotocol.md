# TKSmartCardProtocol

**Framework**: CryptoTokenKit  
**Kind**: struct  
**Role**: Structure

Smart Card transmission protocols.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
struct TKSmartCardProtocol
```

```c
enum TKSmartCardProtocol : NSUInteger;
```

## Topics

### Constants
- [static var t0: TKSmartCardProtocol](./tksmartcardprotocol/t0.md)
- [static var t1: TKSmartCardProtocol](./tksmartcardprotocol/t1.md)
- [static var t15: TKSmartCardProtocol](./tksmartcardprotocol/t15.md)
- [static var any: TKSmartCardProtocol](./tksmartcardprotocol/any.md)
### Initializers
- [init(rawValue: UInt)](./tksmartcardprotocol/init%28rawvalue%29.md)

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

### Setting the Communication Protocol
- [var allowedProtocols: TKSmartCardProtocol](./tksmartcard/allowedprotocols.md)
  The protocols allowed for communication with the Smart Card. [`any`](./tksmartcardprotocol/any.md) by default.
- [var currentProtocol: TKSmartCardProtocol](./tksmartcard/currentprotocol.md)
  The protocol used for communication with the Smart Card. Returns [`TKSmartCardProtocolNone`](./tksmartcardprotocol/tksmartcardprotocolnone.md) if no session is currently established.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardprotocol)*