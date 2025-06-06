# SSLSetSessionTicketsEnabled(_:_:)

**Framework**: Security  
**Kind**: func

Enables or disables session ticket resumption.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+

## Declaration

```swift
func SSLSetSessionTicketsEnabled(_ context: SSLContext, _ enabled: Bool) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

By default, session tickets are disabled.

## Parameters

- `context`: A session context.
- `enabled`: A Boolean set to   to enable session ticket resumption, or   to disable it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetsessionticketsenabled(_:_:))*