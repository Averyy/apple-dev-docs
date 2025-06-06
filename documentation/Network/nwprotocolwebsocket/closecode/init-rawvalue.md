# init(rawValue:)

**Framework**: Network  
**Kind**: init

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

- [case protocolCode(NWProtocolWebSocket.CloseCode.Defined)](nwprotocolwebsocket/closecode/protocolcode(_:).md)
  A well-known close code reserved by the protocol (values 1000-2999).
- [NWProtocolWebSocket.CloseCode.Defined](nwprotocolwebsocket/closecode/defined.md)
  Well-known close code values.
- [NWProtocolWebSocket.CloseCode.applicationCode(_:)](nwprotocolwebsocket/closecode/applicationcode(_:).md)
  A close code in the range reserved for applications and frameworks (3000-3999).
- [NWProtocolWebSocket.CloseCode.privateCode(_:)](nwprotocolwebsocket/closecode/privatecode(_:).md)
  A close code in the private-use range (4000-4999).


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/closecode/init(rawvalue:))*