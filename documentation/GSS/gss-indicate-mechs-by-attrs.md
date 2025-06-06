# gss_indicate_mechs_by_attrs(_:_:_:_:_:)

**Framework**: GSS  
**Kind**: func

Returns the set of mechanisms that fulfill the given criteria.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
func gss_indicate_mechs_by_attrs(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ desired_mech_attrs: gss_const_OID_set?, _ except_mech_attrs: gss_const_OID_set?, _ critical_mech_attrs: gss_const_OID_set?, _ mechs: UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on success. See [`Function Status`](function-status.md) for a complete enumeration of status outputs.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `desired_mech_attrs`: A set of attributes, given by their OID, that a mechanism must have in order to appear in the results. See Mechanisms and Authentication in   for a list of possible values.
- `except_mech_attrs`: A set of attributes, given by their OID, that the mechanism must not have in order to appear in the results. See Mechanisms and Authentication in   for a list of possible values.
- `critical_mech_attrs`: A set of attributes, given by their OID, that the mechanism must know about, but not necessarily have, in order to appear in the results. See Mechanisms and Authentication in   for a list of possible values.
- `mechs`: A pointer the function uses to return a new set of mechanisms that meet the given criteria. Release the set’s memory using a call to   after you are done using it.

## See Also

- [func gss_indicate_mechs(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](gss_indicate_mechs(_:_:).md)
  Returns the list of supported underlying security mechanisms.
- [func gss_display_mech_attr(UnsafeMutablePointer<OM_uint32>, gss_const_OID, gss_buffer_t?, gss_buffer_t?, gss_buffer_t?) -> OM_uint32](gss_display_mech_attr(_:_:_:_:_:).md)
  Returns a human-readable name and description of a mechanism attribute.
- [func gss_inquire_attrs_for_mech(UnsafeMutablePointer<OM_uint32>, gss_const_OID, UnsafeMutablePointer<gss_OID_set?>?, UnsafeMutablePointer<gss_OID_set?>?) -> OM_uint32](gss_inquire_attrs_for_mech(_:_:_:_:).md)
  Returns the supported attributes for one or all mechanisms.
- [func gss_inquire_mech_for_saslname(UnsafeMutablePointer<OM_uint32>, gss_buffer_t?, UnsafeMutablePointer<gss_OID?>) -> OM_uint32](gss_inquire_mech_for_saslname(_:_:_:).md)
  Returns the GSS-API mechanism identifier for a given Simple Authentication and Security Layer (SASL) protocol name.
- [func gss_inquire_saslname_for_mech(UnsafeMutablePointer<OM_uint32>, gss_OID, gss_buffer_t?, gss_buffer_t?, gss_buffer_t?) -> OM_uint32](gss_inquire_saslname_for_mech(_:_:_:_:_:).md)
  Returns the Simple Authentication and Security Layer (SASL) protocol name for a given GSS-API mechanism.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_indicate_mechs_by_attrs(_:_:_:_:_:))*