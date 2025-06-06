# Kerberos Implementation

**Framework**: GSS

Establish secure connections using the Kerberos implementation of GSS-API.

## Topics

### Contexts and Keys
- [typealias gss_krb5_cfx_keydata_t](gss_krb5_cfx_keydata_t.md)
  The structure of a Kerberos context and acceptor-asserted key.
- [typealias gss_krb5_lucid_context_v1_t](gss_krb5_lucid_context_v1_t.md)
  The structure of a Kerberos context.
- [typealias gss_krb5_lucid_context_version_t](gss_krb5_lucid_context_version_t.md)
  The structure for determining the returned Kerberos lucid context structure version.
- [typealias gss_krb5_lucid_key_t](gss_krb5_lucid_key_t.md)
  The structure for a Kerberos encryption key.
- [typealias gss_krb5_rfc1964_keydata_t](gss_krb5_rfc1964_keydata_t.md)
  The structure for an RFC 1964-compliant Kerberos encryption key.
### Identity and Settings
- [func gss_krb5_export_lucid_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t?>, OM_uint32, UnsafeMutablePointer<UnsafeMutableRawPointer>?) -> OM_uint32](gss_krb5_export_lucid_sec_context(_:_:_:_:).md)
  Returns a non-opaque version of the internal context information.
- [func gsskrb5_extract_authz_data_from_sec_context(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_buffer_t) -> OM_uint32](gsskrb5_extract_authz_data_from_sec_context(_:_:_:_:).md)
  Extracts Kerberos authorization data stored within the context.
- [func gss_krb5_ccache_name(UnsafeMutablePointer<OM_uint32>, UnsafePointer<CChar>?, UnsafeMutablePointer<UnsafePointer<CChar>?>?) -> OM_uint32](gss_krb5_ccache_name(_:_:_:).md)
  Sets the internal Kerberos 5 credential cache name.
- [func gss_krb5_free_lucid_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutableRawPointer) -> OM_uint32](gss_krb5_free_lucid_sec_context(_:_:).md)
  Frees allocated storage associated with an exported context.
- [func gss_krb5_set_allowable_enctypes(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, OM_uint32, UnsafeMutablePointer<Int32>) -> OM_uint32](gss_krb5_set_allowable_enctypes(_:_:_:_:).md)
  Limits the keys that can be exported to the specified types.
- [func gsskrb5_register_acceptor_identity(UnsafePointer<CChar>) -> OM_uint32](gsskrb5_register_acceptor_identity(_:).md)
  Sets the Kerberos 5 file-based key that the acceptor will use.
- [func krb5_gss_register_acceptor_identity(UnsafePointer<CChar>) -> OM_uint32](krb5_gss_register_acceptor_identity(_:).md)
  Sets the Kerberos 5 file-based key that the acceptor will use.
- [func gss_krb5_copy_ccache(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, OpaquePointer) -> OM_uint32](gss_krb5_copy_ccache(_:_:_:).md)
  Copies Kerberos 5 credentials into the passed cache.

## See Also

- [Token Management](token-management.md)
  Establish secure communication with tokens.
- [Message Protection](message-protection.md)
  Provide cryptographic protection to secure message integrity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/kerberos-implementation)*