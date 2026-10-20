# allowedProtocols

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The protocols allowed for communication with the Smart Card. [`any`](../tksmartcardprotocol/any.md) by default.

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
var allowedProtocols: TKSmartCardProtocol { get set }
```

```objc
@property TKSmartCardProtocol allowedProtocols;
```

#### Discussion

This property is consulted only when beginning a session to a Smart Card. Any changes to this property will not be reflected by the current session, if one is already established.

## See Also

### Setting the Communication Protocol
- [var currentProtocol: TKSmartCardProtocol](./currentprotocol.md)
  The protocol used for communication with the Smart Card. Returns [`TKSmartCardProtocolNone`](../tksmartcardprotocol/tksmartcardprotocolnone.md) if no session is currently established.
- [struct TKSmartCardProtocol](../tksmartcardprotocol.md)
  Smart Card transmission protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/allowedprotocols)*