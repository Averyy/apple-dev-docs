# gss_indicate_mechs(_:_:)

**Framework**: GSS  
**Kind**: func

Returns the list of supported underlying security mechanisms.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func gss_indicate_mechs(_ minor_status: UnsafeMutablePointer<OM_uint32>, _ mech_set: UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32
```

#### Return Value

A status code set to [`GSS_S_COMPLETE`](gss_s_complete.md) on completion.

## Parameters

- `minor_status`: A pointer to the secondary status result that provides additional information in case of failure.
- `mech_set`: A pointer the function uses to output the available set of mechanism identifiers. Release the set with a call to   when you are done with it.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_indicate_mechs(_:_:))*