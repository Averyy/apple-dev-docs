# SSLGetAllowsAnyRoot

**Framework**: Security  
**Kind**: func  
**Role**: Function

Obtains a value specifying whether an unknown root is allowed.

**Availability**:
- macOS 10.2+ - Deprecated in 10.9

> **Deprecated**: See the replacement procedure for allowing arbitrary root certificates in the deprecation summary of [`SSLSetAllowsAnyRoot`](./sslsetallowsanyroot.md).

## Declaration

```c
OSStatus SSLGetAllowsAnyRoot(SSLContextRef context, Boolean *anyRoot);
```

#### Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

#### Discussion

Use the [`SSLSetAllowsAnyRoot`](./sslsetallowsanyroot.md) function to set the value of the `anyRoot` flag. The effect and meaning of this flag is described in the discussion of the [`SSLSetAllowsAnyRoot`](./sslsetallowsanyroot.md) function.

## Parameters

- `context`: An SSL session context reference.
- `anyRoot`: On return, a Boolean indicating the current setting of the `anyRoot` flag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetallowsanyroot)*