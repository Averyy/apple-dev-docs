# GSS_C_ACCEPT

**Framework**: GSS  
**Kind**: var

The value that indicates a credential that can accept a security context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var GSS_C_ACCEPT: Int32 { get }
```

## See Also

- [var GSS_C_INDEFINITE: UInt](gss_c_indefinite.md)
  The value that indicates the maximum permitted lifetime when used in a time request.
- [var GSS_C_INITIATE: Int32](gss_c_initiate.md)
  The value that indicates a credential that can initiate a security context.
- [var GSS_C_BOTH: Int32](gss_c_both.md)
  The value that indicates a credential that can both initiate and accept security contexts.
- [var GSS_C_OPTION_MASK: Int32](gss_c_option_mask.md)
  The masking constant for options.
- [var GSS_C_CRED_NO_UI: Int32](gss_c_cred_no_ui.md)
  The value that indicates no UI.
- [typealias gss_auth_identity_t](gss_auth_identity_t.md)
  A pointer to an opaque object used to manage authentication identities.
- [typealias gss_const_cred_id_t](gss_const_cred_id_t.md)
  A pointer to an immutable opaque type that you use to exchange a credential object with GSS-API functions.
- [typealias gss_cred_id_t](gss_cred_id_t.md)
  A pointer to an opaque type that you use to exchange a credential object with GSS-API functions.
- [typealias gss_cred_usage_t](gss_cred_usage_t.md)
  A credential usage value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_c_accept)*