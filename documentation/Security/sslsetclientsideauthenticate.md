# SSLSetClientSideAuthenticate(_:_:)

**Framework**: Security  
**Kind**: func

Specifies the requirements for client-side authentication.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
func SSLSetClientSideAuthenticate(_ context: SSLContext, _ auth: SSLAuthenticate) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

This function can be called only by servers. Use of this function is optional. The default authentication requirement is [`SSLAuthenticate.neverAuthenticate`](sslauthenticate/neverauthenticate.md). This function may be called only when no session is active.

## Parameters

- `context`: An SSL session context reference.
- `auth`: A flag setting the requirements for client-side authentication. See   for possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetclientsideauthenticate(_:_:))*