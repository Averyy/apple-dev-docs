# Object Identifiers

**Framework**: GSS  
**Role**: API Collection

Store security mechanisms, QOPs (Quality of Protection values), and name types.

## Topics

### Object IDs
- [typealias gss_OID](./gss_oid.md)
  A pointer to the OID descriptor that exchanges object identifiers with many GSS-API functions.
- [typealias gss_OID_set](./gss_oid_set.md)
  A pointer to a descriptor that manages an array of OID descriptors.
- [typealias gss_OID_desc](./gss_oid_desc.md)
  The OID descriptor that exchanges object identifiers with many GSS-API functions.
- [typealias gss_const_OID](./gss_const_oid.md)
  A pointer to an immutable OID descriptor exchanges object identifiers with many GSS-API functions.
- [typealias gss_const_OID_set](./gss_const_oid_set.md)
  A pointer to an immutable descriptor manages an array of OID descriptors.
- [struct gss_OID_desc_struct](./gss_oid_desc_struct.md)
  The structure for an OID descriptor that exchanges object identifiers with many GSS-API functions.
- [typealias gss_OID_set_desc](./gss_oid_set_desc.md)
  The descriptor that manages an array of OID descriptors.
- [struct gss_OID_set_desc_struct](./gss_oid_set_desc_struct.md)
  The structure for an OID set descriptor that manages an array of OID descriptors.
### Quality of Protection Constants
- [var GSS_C_QOP_DEFAULT: Int32](./gss_c_qop_default.md)
  The default Quality of Protection for per-message services.
- [var GSS_KRB5_CONF_C_QOP_DES: Int32](./gss_krb5_conf_c_qop_des.md)
  The Kerberos 5 Qualty of Service 56-bit DES encryption.
- [var GSS_KRB5_CONF_C_QOP_DES3_KD: Int32](./gss_krb5_conf_c_qop_des3_kd.md)
  The Kerberos 5 Qualty of Service 168-bit DES3 encryption with key derivation.
### Creation and Release
- [func gss_create_empty_oid_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](./gss_create_empty_oid_set%28_,_%29.md)
  Allocates a new, empty set to hold object identifiers.
- [func gss_add_oid_set_member(UnsafeMutablePointer<OM_uint32>, gss_const_OID, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32](./gss_add_oid_set_member%28_,_,_%29.md)
  Adds an object identifier into an OID set.
- [func gss_release_oid_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](./gss_release_oid_set%28_,_%29.md)
  Releases the memory associated with an OID set.
- [func gss_release_oid(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID?>) -> OM_uint32](./gss_release_oid%28_,_%29.md)
  Releases the memory associated with an object identifier.
### Conversion and Duplication
- [func gss_oid_to_str(UnsafeMutablePointer<OM_uint32>, gss_OID, gss_buffer_t) -> OM_uint32](./gss_oid_to_str%28_,_,_%29.md)
  Converts an OID object to a human-readable string.
- [func gss_test_oid_set_member(UnsafeMutablePointer<OM_uint32>, gss_const_OID, gss_OID_set, UnsafeMutablePointer<Int32>) -> OM_uint32](./gss_test_oid_set_member%28_,_,_,_%29.md)
  Returns a flag that indicates if an OID is present in an OID set.
- [func gss_oid_equal(gss_const_OID?, gss_const_OID?) -> Int32](./gss_oid_equal%28_,_%29.md)
  Returns a flag that indicates whether two object identifiers are the same.
- [func gss_duplicate_oid(UnsafeMutablePointer<OM_uint32>, gss_OID, UnsafeMutablePointer<gss_OID?>) -> OM_uint32](./gss_duplicate_oid%28_,_,_%29.md)
  Copies an OID into a new object.

## See Also

### Names and Object Identifiers
- [Name Handling](./name-handling.md)
  Manage names for GSS-API principals such as a person, a machine, or an application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/object-identifiers)*