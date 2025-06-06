# gss_display_mech_attr(_:_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Returns a human-readable name and description of a mechanism attribute.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_display_mech_attr(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ mech_attr: gss_const_OID, _ name: gss_buffer_t?, _ short_desc: gss_buffer_t?, _ long_desc: gss_buffer_t?) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success or [`GSS_S_BAD_MECH`](gss_s_bad_mech.md) if the desired mechanism is unsupported. See [`Function Status`](function-status.md) for a complete enumeration of status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `mech_attr`: The mechanism attribute to examine. See Mechanisms and Authentication in   for a list of possible values.
- `name`: A buffer the function fills with a human readable version of the mechanism attribute. Release this buffer with a call to   when you are done with it.
- `short_desc`: A buffer the function fills with a short description of the mechanism attribute. Release this buffer with a call to   when you are done with it.
- `long_desc`: A buffer the function fills with a longer description of the mechanism attribute. Release this buffer with a call to   when you are done with it.

## See Also

- [func gss_indicate_mechs(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](gss_indicate_mechs(_:_:).md)
  Returns the list of supported underlying security mechanisms.
- [func gss_indicate_mechs_by_attrs(UnsafeMutablePointer<OM_uint32>, gss_const_OID_set?, gss_const_OID_set?, gss_const_OID_set?, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](gss_indicate_mechs_by_attrs(_:_:_:_:_:).md)
  Returns the set of mechanisms that fulfill the given criteria.
- [func gss_inquire_attrs_for_mech(UnsafeMutablePointer<OM_uint32>, gss_const_OID, UnsafeMutablePointer<gss_OID_set?>?, UnsafeMutablePointer<gss_OID_set?>?) -> OM_uint32](gss_inquire_attrs_for_mech(_:_:_:_:).md)
  Returns the supported attributes for one or all mechanisms.
- [func gss_inquire_mech_for_saslname(UnsafeMutablePointer<OM_uint32>, gss_buffer_t?, UnsafeMutablePointer<gss_OID?>) -> OM_uint32](gss_inquire_mech_for_saslname(_:_:_:).md)
  Returns the GSS-API mechanism identifier for a given Simple Authentication and Security Layer (SASL) protocol name.
- [func gss_inquire_saslname_for_mech(UnsafeMutablePointer<OM_uint32>, gss_OID, gss_buffer_t?, gss_buffer_t?, gss_buffer_t?) -> OM_uint32](gss_inquire_saslname_for_mech(_:_:_:_:_:).md)
  Returns the Simple Authentication and Security Layer (SASL) protocol name for a given GSS-API mechanism.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_display_mech_attr(_:_:_:_:_:))*