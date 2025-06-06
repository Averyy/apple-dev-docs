# TKSmartCardProtocol

**Framework**: CryptoTokenKit  
**Kind**: struct

Smart Card transmission protocols.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct TKSmartCardProtocol
```

## Topics

### Constants
- [static var t0: TKSmartCardProtocol](tksmartcardprotocol/t0.md)
- [static var t1: TKSmartCardProtocol](tksmartcardprotocol/t1.md)
- [static var t15: TKSmartCardProtocol](tksmartcardprotocol/t15.md)
- [static var any: TKSmartCardProtocol](tksmartcardprotocol/any.md)
### Initializers
- [init(rawValue: UInt)](tksmartcardprotocol/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var allowedProtocols: TKSmartCardProtocol](tksmartcard/allowedprotocols.md)
  The protocols allowed for communication with the Smart Card. [`any`](tksmartcardprotocol/any.md) by default.
- [var currentProtocol: TKSmartCardProtocol](tksmartcard/currentprotocol.md)
  The protocol used for communication with the Smart Card. Returns [`TKSmartCardProtocolNone`](tksmartcardprotocol/tksmartcardprotocolnone.md) if no session is currently established.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardprotocol)*