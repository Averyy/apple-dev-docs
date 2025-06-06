# gss_krb5_export_lucid_sec_context(_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Returns a non-opaque version of the internal context information.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_krb5_export_lucid_sec_context(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ context_handle: UnsafeMutablePointer<gss_ctx_id_t?>, _ version: OM_uint32, _ rctx: UnsafeMutablePointer<UnsafeMutableRawPointer>?) -> OM_uint32
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_krb5_export_lucid_sec_context(_:_:_:_:))*