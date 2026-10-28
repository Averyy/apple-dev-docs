# SSLSetIOFuncs(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Specifies callback functions that perform the network I/O operations.

**Availability**:
- iOS 5.0+ - Deprecated in 13.0
- iPadOS 5.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLSetIOFuncs(_ context: SSLContext, _ readFunc: SSLReadFunc, _ writeFunc: SSLWriteFunc) -> OSStatus
```

```c
OSStatus SSLSetIOFuncs(SSLContextRef context, SSLReadFunc readFunc, SSLWriteFunc writeFunc);
```

## Mentions

- [Using the Secure Socket Layer for Network Communication](./using-the-secure-socket-layer-for-network-communication.md)

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

Secure Transport calls your read and write callback functions to perform network I/O. You must define these functions before calling [`SSLSetIOFuncs(_:_:_:)`](./sslsetiofuncs%28_,_,_%29.md).

You must call [`SSLSetIOFuncs(_:_:_:)`](./sslsetiofuncs%28_,_,_%29.md) prior to calling the [`SSLHandshake(_:)`](./sslhandshake%28_%29.md) function. [`SSLSetIOFuncs(_:_:_:)`](./sslsetiofuncs%28_,_,_%29.md) cannot be called while a session is active.

## Parameters

- `context`: An SSL session context reference.
- `readFunc`: A pointer to your read callback function. See [`SSLReadFunc`](./sslreadfunc.md) for information on defining this function.
- `writeFunc`: A pointer to your write callback function. See [`SSLWriteFunc`](./sslwritefunc.md) for information on defining this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetiofuncs(_:_:_:))*