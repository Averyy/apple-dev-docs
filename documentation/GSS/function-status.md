# Function Status

**Framework**: GSS

Evaluate return values that most GSS-API functions use to indicate the outcome of an operation.

#### Overview

The functions of the GSS-API return two status codes. The major status code, delivered as the function’s return value, provides a mechanism-independent status output. A value of [`GSS_S_COMPLETE`](gss_s_complete.md) typically indicates success, but the code is actually composed of several fields that enable communicating a more nuanced result.  Always check the major status code to determine if an operation succeeds.

The minor status code provides additional information, often mechanism-specific, when an operation fails. This result returns using the [`OM_uint32`](om_uint32.md) pointer given as the function’s first argument. Examine this value to further debug a problem. For example, many functions allocate memory as a side effect of their main task. If memory allocation fails, the entire operation fails. But while the major status indicates a generic problem, a minor status of `ENOMEM` indicates that failed memory allocation is the exact culprit.

Three bitfields bundled together make up major status codes in a single [`OM_uint32`](om_uint32.md) value. These fields are:

When a function successfully runs to completion, it returns zero for all of these fields. As a convenience, you can compare the result directly with the status code [`GSS_S_COMPLETE`](gss_s_complete.md) to test for this condition.

![Diagram of the three bitfields that make up the status codes in a value: the 8 bit calling error, the 8 bit routine error, and the 16 bit supplementary information.](https://docs-assets.developer.apple.com/published/e80920a4de046d204e8222153b7debcf/media-3402053%402x.png)

For any other result, use one of the available extraction macros (such as [`GSS_CALLING_ERROR`](gss_calling_error.md)) to obtain a value that you compare against one of the known error codes. For example, you can test for a failure to read one of the function inputs as follows:

```objc
OM_uint32 major = <# Some GSS call #>
if (GSS_CALLING_ERROR(major) == GSS_S_CALL_INACCESSIBLE_READ) {
    // Handle the error
}
```

Use the [`gss_display_status(_:_:_:_:_:_:)`](gss_display_status(_:_:_:_:_:_:).md) function to retrieve a human readable string corresponding to a given status result.

## Topics

### Status and Error Creation
- [typealias OM_uint32](om_uint32.md)
  A 32-bit unsigned integer.
- [typealias OM_uint64](om_uint64.md)
  A 64-bit unsigned integer.
- [typealias gss_uint32](gss_uint32.md)
  A 32-bit unsigned integer.
- [typealias gss_status_id_t](gss_status_id_t.md)
  A pointer to a status result.
- [var GSS_C_MECH_CODE: Int32](gss_c_mech_code.md)
  A flag that indicates the status code comes from a call to an underlying mechanism, such as Kerberos.
- [var GSS_C_GSS_CODE: Int32](gss_c_gss_code.md)
  A flag that indicates the named status code comes from a GSS-API call.
- [var GSS_S_COMPLETE: Int32](gss_s_complete.md)
  The operation completed without error.
- [func gss_display_status(UnsafeMutablePointer<OM_uint32>, OM_uint32, Int32, gss_OID?, UnsafeMutablePointer<OM_uint32>, gss_buffer_t) -> OM_uint32](gss_display_status(_:_:_:_:_:_:).md)
  Returns a human readable string for a status code.
- [func GSSCreateError(gss_const_OID, OM_uint32, OM_uint32) -> Unmanaged<CFError>?](gsscreateerror(_:_:_:).md)
  Returns an error object based on GSS-API major and minor status codes.
### Calling Errors
- [var GSS_S_CALL_BAD_STRUCTURE: UInt](gss_s_call_bad_structure.md)
  Improperly formatted parameter.
- [var GSS_S_CALL_INACCESSIBLE_READ: UInt](gss_s_call_inaccessible_read.md)
  A required input parameter could not be read.
- [var GSS_S_CALL_INACCESSIBLE_WRITE: UInt](gss_s_call_inaccessible_write.md)
  A required output parameter failed to write.
### Routine Errors
- [var GSS_S_BAD_MECH: UInt](gss_s_bad_mech.md)
  Unsupported mechanism.
- [var GSS_S_BAD_NAME: UInt](gss_s_bad_name.md)
  Invalid name.
- [var GSS_S_BAD_NAMETYPE: UInt](gss_s_bad_nametype.md)
  Unsupported name type.
- [var GSS_S_BAD_MIC: UInt](gss_s_bad_mic.md)
  Failed token integrity check.
- [var GSS_S_BAD_SIG: UInt](gss_s_bad_sig.md)
  Failed token integrity check.
- [var GSS_S_BAD_STATUS: UInt](gss_s_bad_status.md)
  Invalid status selector.
- [var GSS_S_BAD_BINDINGS: UInt](gss_s_bad_bindings.md)
  Channel bindings mismatch.
- [var GSS_S_NO_CRED: UInt](gss_s_no_cred.md)
  No valid credentials.
- [var GSS_S_NO_CONTEXT: UInt](gss_s_no_context.md)
  No valid security context.
- [var GSS_S_DEFECTIVE_TOKEN: UInt](gss_s_defective_token.md)
  Defective token.
- [var GSS_S_DEFECTIVE_CREDENTIAL: UInt](gss_s_defective_credential.md)
  Defective credential.
- [var GSS_S_CREDENTIALS_EXPIRED: UInt](gss_s_credentials_expired.md)
  Expired credential.
- [var GSS_S_CONTEXT_EXPIRED: UInt](gss_s_context_expired.md)
  Expired context.
- [var GSS_S_FAILURE: UInt](gss_s_failure.md)
  An unspecified error.
- [var GSS_S_BAD_QOP: UInt](gss_s_bad_qop.md)
  Unsupported QOP value.
- [var GSS_S_UNAUTHORIZED: UInt](gss_s_unauthorized.md)
  Unauthorized operation.
- [var GSS_S_UNAVAILABLE: UInt](gss_s_unavailable.md)
  Unavailable operation.
- [var GSS_S_DUPLICATE_ELEMENT: UInt](gss_s_duplicate_element.md)
  A duplicate credential element requested.
- [var GSS_S_NAME_NOT_MN: UInt](gss_s_name_not_mn.md)
  The name contains multimechanism elements.
- [var GSS_S_BAD_MECH_ATTR: UInt](gss_s_bad_mech_attr.md)
  Unknown mechanism attribute.
- [var GSS_S_CRED_UNAVAIL: UInt](gss_s_cred_unavail.md)
  Unavailable credential.
### Masks and Offsets
- [var GSS_C_CALLING_ERROR_MASK: UInt](gss_c_calling_error_mask.md)
  A mask with a width that matches the calling error field.
- [var GSS_C_CALLING_ERROR_OFFSET: Int32](gss_c_calling_error_offset.md)
  The offset of the calling error field within the major status code.
- [var GSS_C_ROUTINE_ERROR_MASK: UInt](gss_c_routine_error_mask.md)
  A mask with a width that matches the routine error field.
- [var GSS_C_ROUTINE_ERROR_OFFSET: Int32](gss_c_routine_error_offset.md)
  The offset of the routine error field within the major status code.
- [var GSS_C_SUPPLEMENTARY_MASK: UInt](gss_c_supplementary_mask.md)
  A mask with a width that matches the supplementary information field.
- [var GSS_C_SUPPLEMENTARY_OFFSET: Int32](gss_c_supplementary_offset.md)
  The offset of the supplementary information field within the major status code.

## See Also

- [Allocating and Releasing Objects](allocating-and-releasing-objects.md)
  Manage memory and object lifetimes.
- [Buffer Management](buffer-management.md)
  Allocate and deallocate buffers with structures that hold a variety of data.
- [Context Services](context-services.md)
  Use context services to manage secure operations between endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/function-status)*