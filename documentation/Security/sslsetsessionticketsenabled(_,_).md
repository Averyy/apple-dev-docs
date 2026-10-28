# SSLSetSessionTicketsEnabled(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Enables or disables session ticket resumption.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.13+ - Deprecated in 10.15

> **Deprecated**: No longer supported. Use Network.framework.

## Declaration

```swift
func SSLSetSessionTicketsEnabled(_ context: SSLContext, _ enabled: Bool) -> OSStatus
```

```c
OSStatus SSLSetSessionTicketsEnabled(SSLContextRef context, Boolean enabled);
```

## Return Value

A result code. See [Secure Transport Result Codes](./secure-transport-result-codes.md).

## Discussion

By default, session tickets are disabled.

## Parameters

- `context`: A session context.
- `enabled`: A Boolean set to [`true`](../Swift/true.md) to enable session ticket resumption, or [`false`](../Swift/false.md) to disable it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetsessionticketsenabled(_:_:))*