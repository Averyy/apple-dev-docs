# init(rawValue:)

**Framework**: Network  
**Kind**: init  
**Role**: Initializer

Initializes a close code with a raw value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(rawValue: UInt16) throws
```

## See Also

### Close Code Types
- [case protocolCode(NWProtocolWebSocket.CloseCode.Defined)](./protocolcode%28_%29.md)
  A well-known close code reserved by the protocol (values 1000-2999).
- [NWProtocolWebSocket.CloseCode.Defined](./defined.md)
  Well-known close code values.
- [NWProtocolWebSocket.CloseCode.applicationCode(_:)](./applicationcode%28_%29.md)
  A close code in the range reserved for applications and frameworks (3000-3999).
- [NWProtocolWebSocket.CloseCode.privateCode(_:)](./privatecode%28_%29.md)
  A close code in the private-use range (4000-4999).


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/closecode/init(rawvalue:))*