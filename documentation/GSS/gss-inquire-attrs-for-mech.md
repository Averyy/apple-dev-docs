# gss_inquire_attrs_for_mech(_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Returns the supported attributes for one or all mechanisms.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_inquire_attrs_for_mech(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ mech: gss_const_OID, _ mech_attr: UnsafeMutablePointer<gss_OID_set?>?, _ known_mech_attrs: UnsafeMutablePointer<gss_OID_set?>?) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success or [`GSS_S_BAD_MECH`](gss_s_bad_mech.md) if the desired mechanism is unsupported. See [`Function Status`](function-status.md) for a complete enumeration of status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `mech`: The mechanism to examine, or   to examine all mechanisms.
- `mech_attr`: A pointer the function uses to return the list of mechanism attributes supported by the mechanism. See Mechanisms and Authentication in   for a list of possible values. Pass   to ignore this output. If you do receive a set, release its memory with a call to   when you are done with it.

## See Also

- [func gss_indicate_mechs(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](gss_indicate_mechs(_:_:).md)
  Returns the list of supported underlying security mechanisms.
- [func gss_indicate_mechs_by_attrs(UnsafeMutablePointer<OM_uint32>, gss_const_OID_set?, gss_const_OID_set?, gss_const_OID_set?, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](gss_indicate_mechs_by_attrs(_:_:_:_:_:).md)
  Returns the set of mechanisms that fulfill the given criteria.
- [func gss_display_mech_attr(UnsafeMutablePointer<OM_uint32>, gss_const_OID, gss_buffer_t?, gss_buffer_t?, gss_buffer_t?) -> OM_uint32](gss_display_mech_attr(_:_:_:_:_:).md)
  Returns a human-readable name and description of a mechanism attribute.
- [func gss_inquire_mech_for_saslname(UnsafeMutablePointer<OM_uint32>, gss_buffer_t?, UnsafeMutablePointer<gss_OID?>) -> OM_uint32](gss_inquire_mech_for_saslname(_:_:_:).md)
  Returns the GSS-API mechanism identifier for a given Simple Authentication and Security Layer (SASL) protocol name.
- [func gss_inquire_saslname_for_mech(UnsafeMutablePointer<OM_uint32>, gss_OID, gss_buffer_t?, gss_buffer_t?, gss_buffer_t?) -> OM_uint32](gss_inquire_saslname_for_mech(_:_:_:_:_:).md)
  Returns the Simple Authentication and Security Layer (SASL) protocol name for a given GSS-API mechanism.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_inquire_attrs_for_mech(_:_:_:_:))*