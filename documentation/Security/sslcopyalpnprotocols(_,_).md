# SSLCopyALPNProtocols(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Gets the list of supported application layer protocols.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.13+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLCopyALPNProtocols(_ context: SSLContext, _ protocols: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus
```

```c
OSStatus SSLCopyALPNProtocols(SSLContextRef context, CFArrayRef*protocols);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

You must set the `protocols` parameter to `NULL` on input, or the operation fails. If the function has data to provide, it allocates memory for an array and returns it using `protocols`. Otherwise, `protocols` remains `NULL` on output.

## Parameters

- `context`: The session context.
- `protocols`: A pointer the function uses to return an array of ASCII-encoded strings representing the supported protocols, such as http/1.1. See [RFC 7301](https://tools.ietf.org/html/rfc7301) for more details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslcopyalpnprotocols(_:_:))*