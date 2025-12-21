# currentProtocol

**Framework**: CryptoTokenKit  
**Kind**: property

The protocol used for communication with the Smart Card. Returns [`TKSmartCardProtocolNone`](tksmartcardprotocol/tksmartcardprotocolnone.md) if no session is currently established.

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
var currentProtocol: TKSmartCardProtocol { get }
```

## See Also

- [var allowedProtocols: TKSmartCardProtocol](tksmartcard/allowedprotocols.md)
  The protocols allowed for communication with the Smart Card. [`any`](tksmartcardprotocol/any.md) by default.
- [struct TKSmartCardProtocol](tksmartcardprotocol.md)
  Smart Card transmission protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/currentprotocol)*