# allowedProtocols

**Framework**: CryptoTokenKit  
**Kind**: property

The protocols allowed for communication with the Smart Card. [`any`](tksmartcardprotocol/any.md) by default.

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
var allowedProtocols: TKSmartCardProtocol { get set }
```

#### Discussion

This property is consulted only when beginning a session to a Smart Card. Any changes to this property will not be reflected by the current session, if one is already established.

## See Also

- [var currentProtocol: TKSmartCardProtocol](tksmartcard/currentprotocol.md)
  The protocol used for communication with the Smart Card. Returns [`TKSmartCardProtocolNone`](tksmartcardprotocol/tksmartcardprotocolnone.md) if no session is currently established.
- [struct TKSmartCardProtocol](tksmartcardprotocol.md)
  Smart Card transmission protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/allowedprotocols)*