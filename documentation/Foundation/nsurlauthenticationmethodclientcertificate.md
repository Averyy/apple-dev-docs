# NSURLAuthenticationMethodClientCertificate

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

Use client certificate authentication for this protection space.

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
let NSURLAuthenticationMethodClientCertificate: String
```

```c
extern NSString * const NSURLAuthenticationMethodClientCertificate;
```

#### Discussion

This authentication method can apply to any protocol.

## See Also

### Session-wide authentication challenges
- [let NSURLAuthenticationMethodNegotiate: String](./nsurlauthenticationmethodnegotiate.md)
  Negotiate whether to use Kerberos or NTLM authentication for this protection space.
- [let NSURLAuthenticationMethodNTLM: String](./nsurlauthenticationmethodntlm.md)
  Use NTLM authentication for this protection space.
- [let NSURLAuthenticationMethodServerTrust: String](./nsurlauthenticationmethodservertrust.md)
  Perform server trust authentication (certificate validation) for this protection space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlauthenticationmethodclientcertificate)*