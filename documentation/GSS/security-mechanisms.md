# Security Mechanisms

**Framework**: GSS

Provide a security mechanism for your implementation.

#### Overview

For more information on the attributes of a mechanism, see [`RFC 5587`](https://developer.apple.comhttps://tools.ietf.org/html/rfc5587).

## Topics

### Queries
- [func gss_indicate_mechs(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](gss_indicate_mechs(_:_:).md)
  Returns the list of supported underlying security mechanisms.
- [func gss_indicate_mechs_by_attrs(UnsafeMutablePointer<OM_uint32>, gss_const_OID_set?, gss_const_OID_set?, gss_const_OID_set?, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](gss_indicate_mechs_by_attrs(_:_:_:_:_:).md)
  Returns the set of mechanisms that fulfill the given criteria.
- [func gss_display_mech_attr(UnsafeMutablePointer<OM_uint32>, gss_const_OID, gss_buffer_t?, gss_buffer_t?, gss_buffer_t?) -> OM_uint32](gss_display_mech_attr(_:_:_:_:_:).md)
  Returns a human-readable name and description of a mechanism attribute.
- [func gss_inquire_attrs_for_mech(UnsafeMutablePointer<OM_uint32>, gss_const_OID, UnsafeMutablePointer<gss_OID_set?>?, UnsafeMutablePointer<gss_OID_set?>?) -> OM_uint32](gss_inquire_attrs_for_mech(_:_:_:_:).md)
  Returns the supported attributes for one or all mechanisms.
- [func gss_inquire_mech_for_saslname(UnsafeMutablePointer<OM_uint32>, gss_buffer_t?, UnsafeMutablePointer<gss_OID?>) -> OM_uint32](gss_inquire_mech_for_saslname(_:_:_:).md)
  Returns the GSS-API mechanism identifier for a given Simple Authentication and Security Layer (SASL) protocol name.
- [func gss_inquire_saslname_for_mech(UnsafeMutablePointer<OM_uint32>, gss_OID, gss_buffer_t?, gss_buffer_t?, gss_buffer_t?) -> OM_uint32](gss_inquire_saslname_for_mech(_:_:_:_:_:).md)
  Returns the Simple Authentication and Security Layer (SASL) protocol name for a given GSS-API mechanism.

## See Also

- [Credential Management](credential-management.md)
  Securely establish connections between endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/security-mechanisms)*