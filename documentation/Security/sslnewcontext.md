# SSLNewContext

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates a new Secure Sockets Layer (SSL) session context.

**Availability**:
- macOS 10.2+ - Deprecated in 10.9

> **Deprecated**: Use [`SSLCreateContext(_:_:_:)`](./sslcreatecontext%28_,_,_%29.md) instead.

## Declaration

```c
OSStatus SSLNewContext(Boolean isServer, SSLContextRef*contextPtr);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

The SSL session context is an opaque data structure that identifies a session and stores session information. You must pass this object to every other function in the Secure Transport API.

## Parameters

- `isServer`: Set `true` if the calling process is a server.
- `contextPtr`: On return, points to a new SSL session context reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslnewcontext)*