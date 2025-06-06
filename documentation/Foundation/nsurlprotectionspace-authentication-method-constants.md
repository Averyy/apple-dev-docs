# NSURLProtectionSpace authentication method constants

**Framework**: Foundation

Constants describing known values of the [`authenticationMethod`](urlprotectionspace/authenticationmethod.md) property of a [`URLProtectionSpace`](urlprotectionspace.md).

#### Overview

These constants are also used with the [`URLProtectionSpace`](urlprotectionspace.md) initializers [`init(host:port:protocol:realm:authenticationMethod:)`](urlprotectionspace/init(host:port:protocol:realm:authenticationmethod:).md) and [`init(proxyHost:port:type:realm:authenticationMethod:)`](urlprotectionspace/init(proxyhost:port:type:realm:authenticationmethod:).md).

## Topics

### Session-wide authentication challenges
- [let NSURLAuthenticationMethodClientCertificate: String](nsurlauthenticationmethodclientcertificate.md)
  Use client certificate authentication for this protection space.
- [let NSURLAuthenticationMethodNegotiate: String](nsurlauthenticationmethodnegotiate.md)
  Negotiate whether to use Kerberos or NTLM authentication for this protection space.
- [let NSURLAuthenticationMethodNTLM: String](nsurlauthenticationmethodntlm.md)
  Use NTLM authentication for this protection space.
- [let NSURLAuthenticationMethodServerTrust: String](nsurlauthenticationmethodservertrust.md)
  Perform server trust authentication (certificate validation) for this protection space.
### Task-specific authentication challenges
- [let NSURLAuthenticationMethodDefault: String](nsurlauthenticationmethoddefault.md)
  Use the default authentication method for a protocol.
- [let NSURLAuthenticationMethodHTMLForm: String](nsurlauthenticationmethodhtmlform.md)
  Use HTML form authentication for this protection space.
- [let NSURLAuthenticationMethodHTTPBasic: String](nsurlauthenticationmethodhttpbasic.md)
  Use HTTP basic authentication for this protection space.
- [let NSURLAuthenticationMethodHTTPDigest: String](nsurlauthenticationmethodhttpdigest.md)
  Use HTTP digest authentication for this protection space.

## See Also

- [Handling an authentication challenge](handling-an-authentication-challenge.md)
  Respond appropriately when a server demands authentication for a URL request.
- [Performing manual server trust authentication](performing-manual-server-trust-authentication.md)
  Evaluate the server’s security credentials in your app.
- [NSURLProtectionSpace protocol types](nsurlprotectionspace-protocol-types.md)
  These constants describe the supported protocols for a protection space, as returned by [`protocol`](urlprotectionspace/protocol.md).
- [NSURLProtectionSpace proxy types](nsurlprotectionspace-proxy-types.md)
  These constants describe the supported proxy types used in [`init(proxyHost:port:type:realm:authenticationMethod:)`](urlprotectionspace/init(proxyhost:port:type:realm:authenticationmethod:).md) and returned by [`proxyType`](urlprotectionspace/proxytype.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlprotectionspace-authentication-method-constants)*