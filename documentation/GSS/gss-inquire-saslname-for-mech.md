# gss_inquire_saslname_for_mech(_:_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Returns the Simple Authentication and Security Layer (SASL) protocol name for a given GSS-API mechanism.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
func gss_inquire_saslname_for_mech(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ desired_mech: gss_OID, _ sasl_mech_name: gss_buffer_t?, _ mech_name: gss_buffer_t?, _ mech_description: gss_buffer_t?) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success or [`GSS_S_BAD_MECH`](gss_s_bad_mech.md) if the desired mechanism is unsupported. See [`Function Status`](function-status.md) for a complete enumeration of status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `desired_mech`: The GSS-API mechanism to query.
- `sasl_mech_name`: A buffer the function fills with the SASL G2 protocol name. Release this buffer with a call to   when you are done with it.
- `mech_name`: A buffer the function fills with a human readable version of the GSS-API protocol name. Release this buffer with a call to   when you are done with it.
- `mech_description`: A buffer the function fills with a description of the GSS-API protocol name. Release this buffer with a call to   when you are done with it.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_inquire_saslname_for_mech(_:_:_:_:_:))*