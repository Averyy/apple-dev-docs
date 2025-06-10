# NSURLAuthenticationMethodServerTrust

**Framework**: Foundation  
**Kind**: var

Perform server trust authentication (certificate validation) for this protection space.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSURLAuthenticationMethodServerTrust: String
```

## Mentions

- [Performing manual server trust authentication](performing-manual-server-trust-authentication.md)

#### Discussion

This authentication method can apply to any protocol, and is most commonly used for overriding SSL and TLS chain validation.

To learn more, read [`Overriding TLS Chain Validation Correctly`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/NetworkingTopics/Articles/OverridingSSLChainValidationCorrectly.html#//apple_ref/doc/uid/TP40012544).

## See Also

- [let NSURLAuthenticationMethodClientCertificate: String](nsurlauthenticationmethodclientcertificate.md)
  Use client certificate authentication for this protection space.
- [let NSURLAuthenticationMethodNegotiate: String](nsurlauthenticationmethodnegotiate.md)
  Negotiate whether to use Kerberos or NTLM authentication for this protection space.
- [let NSURLAuthenticationMethodNTLM: String](nsurlauthenticationmethodntlm.md)
  Use NTLM authentication for this protection space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlauthenticationmethodservertrust)*