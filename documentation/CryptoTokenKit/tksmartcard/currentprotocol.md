# currentProtocol

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The protocol used for communication with the Smart Card. Returns [`TKSmartCardProtocolNone`](../tksmartcardprotocol/tksmartcardprotocolnone.md) if no session is currently established.

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

```objc
@property (readonly) TKSmartCardProtocol currentProtocol;
```

## See Also

### Setting the Communication Protocol
- [var allowedProtocols: TKSmartCardProtocol](./allowedprotocols.md)
  The protocols allowed for communication with the Smart Card. [`any`](../tksmartcardprotocol/any.md) by default.
- [struct TKSmartCardProtocol](../tksmartcardprotocol.md)
  Smart Card transmission protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/currentprotocol)*