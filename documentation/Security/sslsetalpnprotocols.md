# SSLSetALPNProtocols(_:_:)

**Framework**: Security  
**Kind**: func

Sets the list of supported applicaiton layer protocols.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+

## Declaration

```swift
func SSLSetALPNProtocols(_ context: SSLContext, _ protocols: CFArray) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

## Parameters

- `context`: The session context.
- `protocols`: An array of ASCII-encoded strings representing the supported protocols, such as  . See   for more details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetalpnprotocols(_:_:))*