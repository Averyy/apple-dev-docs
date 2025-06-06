# NWProtocolWebSocket.CloseCode.applicationCode(_:)

**Framework**: Network  
**Kind**: case

A close code in the range reserved for applications and frameworks (3000-3999).

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
case applicationCode(UInt16)
```

## See Also

- [init(rawValue: UInt16) throws](nwprotocolwebsocket/closecode/init(rawvalue:).md)
  Initializes a close code with a raw value.
- [case protocolCode(NWProtocolWebSocket.CloseCode.Defined)](nwprotocolwebsocket/closecode/protocolcode(_:).md)
  A well-known close code reserved by the protocol (values 1000-2999).
- [NWProtocolWebSocket.CloseCode.Defined](nwprotocolwebsocket/closecode/defined.md)
  Well-known close code values.
- [NWProtocolWebSocket.CloseCode.privateCode(_:)](nwprotocolwebsocket/closecode/privatecode(_:).md)
  A close code in the private-use range (4000-4999).


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolwebsocket/closecode/applicationcode(_:))*