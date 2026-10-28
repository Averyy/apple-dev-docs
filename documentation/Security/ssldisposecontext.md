# SSLDisposeContext

**Framework**: Security  
**Kind**: func  
**Role**: Function

Disposes of a Secure Sockets Layer (SSL) session context.

**Availability**:
- macOS 10.2+ - Deprecated in 10.9

> **Deprecated**: You use this function to dispose of a context that you create with [`SSLNewContext`](./sslnewcontext.md), but that function is deprecated. Instead, use [`SSLCreateContext(_:_:_:)`](./sslcreatecontext%28_,_,_%29.md) to create a new context and use [`CFRelease`](../CoreFoundation/cfrelease.md) to dispose of that context.

## Declaration

```c
OSStatus SSLDisposeContext(SSLContextRef context);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

When you are completely finished with a secure session, you should dispose of the SSL session context in order to release the memory associated with the session.

## Parameters

- `context`: A reference to the SSL session context to dispose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ssldisposecontext)*