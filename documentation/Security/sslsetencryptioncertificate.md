# SSLSetEncryptionCertificate(_:_:)

**Framework**: Security  
**Kind**: func

Specifies the encryption certificates used for this connection.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```swift
func SSLSetEncryptionCertificate(_ context: SSLContext, _ certRefs: CFArray) -> OSStatus
```

#### Return Value

A result code. See [`Secure Transport Result Codes`](secure-transport-result-codes.md).

#### Discussion

Use this function in one of the following cases:

- The leaf certificate specified in the [`SSLSetCertificate(_:_:)`](sslsetcertificate(_:_:).md) function is not capable of encryption.
- The leaf certificate specified in the [`SSLSetCertificate(_:_:)`](sslsetcertificate(_:_:).md) function contains a key that is too large or strong for legal encryption in this session. In this case, a weaker certificate is specified here and is used for server-initiated key exchange.

The following assumptions are made:

- The `certRefs` parameter’s references remain valid for the lifetime of the connection.
- The specified `certRefs[0]` value is capable of encryption.

This function can be called only when no session is active.

SSL servers that enforce the SSL3 or TLS1 specification to the letter do not accept encryption certificates with key sizes larger than 512 bits for exportable ciphers (that is, for SSL sessions with 40-bit session keys). Therefore, if you wish to support exportable ciphers and your certificate has a key larger than 512 bits, you must specify a separate encryption certificate.

## Parameters

- `context`: An SSL session context reference.
- `certRefs`: A value of type   referring to an array of certificate references. The references are type  , except for  , which is of type  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslsetencryptioncertificate(_:_:))*