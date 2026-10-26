# GSS_C_BOTH

**Framework**: GSS  
**Kind**: var  
**Role**: Global Variable

The value that indicates a credential that can both initiate and accept security contexts.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var GSS_C_BOTH: Int32 { get }
```

```c
#define GSS_C_BOTH
```

## See Also

### Credential Masks and Macros
- [var GSS_C_INDEFINITE: UInt](./gss_c_indefinite.md)
  The value that indicates the maximum permitted lifetime when used in a time request.
- [var GSS_C_INITIATE: Int32](./gss_c_initiate.md)
  The value that indicates a credential that can initiate a security context.
- [var GSS_C_ACCEPT: Int32](./gss_c_accept.md)
  The value that indicates a credential that can accept a security context.
- [var GSS_C_OPTION_MASK: Int32](./gss_c_option_mask.md)
  The masking constant for options.
- [var GSS_C_CRED_NO_UI: Int32](./gss_c_cred_no_ui.md)
  The value that indicates no UI.
- [typealias gss_auth_identity_t](./gss_auth_identity_t.md)
  A pointer to an opaque object used to manage authentication identities.
- [typealias gss_const_cred_id_t](./gss_const_cred_id_t.md)
  A pointer to an immutable opaque type that you use to exchange a credential object with GSS-API functions.
- [typealias gss_cred_id_t](./gss_cred_id_t.md)
  A pointer to an opaque type that you use to exchange a credential object with GSS-API functions.
- [typealias gss_cred_usage_t](./gss_cred_usage_t.md)
  A credential usage value.
- [GSS_C_CRED_PASSWORD](./gss_c_cred_password.md)
  The value that indicates a password-based credential.
- [GSS_C_CRED_CERTIFICATE](./gss_c_cred_certificate.md)
  The value that indicates a certificate-based credential.
- [GSS_C_CRED_SecIdentity](./gss_c_cred_secidentity.md)
  The value that indicates a security identity-based credential.
- [GSS_C_CRED_HEIMBASE](./gss_c_cred_heimbase.md)
  The value that indicates a Heimdal-based credential.
- [GSS_C_NO_CREDENTIAL](./gss_c_no_credential.md)
  The value that indicates an empty credential object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_c_both)*