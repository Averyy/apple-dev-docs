# kGSSICVerifyCredentialAcceptorName

**Framework**: GSS  
**Kind**: var

The value is a string indicating the name of the acceptor.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var kGSSICVerifyCredentialAcceptorName: String { get }
```

## See Also

- [var kGSSICPassword: String](kgssicpassword.md)
  The value is a string that indicates a password.
- [var kGSSICCertificate: String](kgssiccertificate.md)
  The value that indicates a certificate to use with PKINIT/PKU2U.
- [var kGSSCredentialUsage: String](kgsscredentialusage.md)
  The value indicates how to use the credential.
- [var kGSSICVerifyCredential: String](kgssicverifycredential.md)
  The value indicates whether to validate the credential with a trusted source to ensure there was no machine-in-the-middle attack.
- [var kGSSICLKDCHostname: String](kgssiclkdchostname.md)
  The value is a string indicating the LKDC hostname.
- [var kGSSICKerberosCacheName: String](kgssickerberoscachename.md)
  The value is a string indicating the name of the cache created for use with the Kerberos mechanism.
- [var kGSSICSiteName: String](kgssicsitename.md)
  The value is a string that is the name of site you are authenticating with, used for load balancing in DNS in Kerberos.
- [var kGSSICAppIdentifierACL: String](kgssicappidentifieracl.md)
  The value is an array of strings containing the list of bundle ID prefixes allowed to access this credential.
- [var kGSSICCreateNewCredential: String](kgssiccreatenewcredential.md)
  The value is a Boolean that indicates whether the caller wants to create a new credential and not overwrite a credential with the same name.
- [var kGSSICAppleSourceApp: String](kgssicapplesourceapp.md)
  The value is a dictionary indicating attributes of the app that the credential is for (only applies to AppVPN).
- [var kGSSICAuthenticationContext: String](kgssicauthenticationcontext.md)
  The value indicates whether to allow the authentication UI or a context to pass a pre-evaluated authentication context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/kgssicverifycredentialacceptorname)*