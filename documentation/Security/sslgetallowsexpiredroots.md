# SSLGetAllowsExpiredRoots

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the value indicating whether expired roots are allowed.

**Availability**:
- macOS 10.2+ - Deprecated in 10.9

> **Deprecated**: See the replacement procedure for allowing expired root certificates in the deprecation summary of [`SSLSetAllowsExpiredRoots`](./sslsetallowsexpiredroots.md).

## Declaration

```c
OSStatus SSLGetAllowsExpiredRoots(SSLContextRef context, Boolean *allowsExpired);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

Use the [`SSLSetAllowsExpiredRoots`](./sslsetallowsexpiredroots.md) function to change the setting of the `allowsExpired` flag.

## Parameters

- `context`: An SSL session context reference.
- `allowsExpired`: On return, points to a Boolean value indicating whether expired roots are allowed. If this value is `true`, no errors are returned if the certificate chain ends in an expired root.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslgetallowsexpiredroots)*