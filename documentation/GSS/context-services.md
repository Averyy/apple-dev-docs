# Context Services

**Framework**: GSS

Use context services to manage secure operations between endpoints.

#### Overview

You use these flags as input to [`gss_init_sec_context(_:_:_:_:_:_:_:_:_:_:_:_:_:)`](gss_init_sec_context(_:_:_:_:_:_:_:_:_:_:_:_:_:).md) to request certain context services. You also receive them as output from both that function and [`gss_accept_sec_context(_:_:_:_:_:_:_:_:_:_:_:)`](gss_accept_sec_context(_:_:_:_:_:_:_:_:_:_:_:).md), indicating which services are actually engaged. Requesting a service does not guarantee its availability.

Because these flags represent the bits of an integer, you combine them with a bitwise `OR` and pull them apart using bitwise `AND`, as shown below.

```objc
OM_uint32 req_flags = GSS_C_DELEG_FLAG | GSS_C_MUTUAL_FLAG;
OM_uint32 ret_flags = 0;
//
// Call gss_init_sec_context() with req_flags; get ret_flags back
//
BOOL deleg  = (ret_flags & GSS_C_DELEG_FLAG)  ? YES : NO;
BOOL mutual = (ret_flags & GSS_C_MUTUAL_FLAG) ? YES : NO;
```

## Topics

### Flags
- [var GSS_C_DELEG_FLAG: Int32](gss_c_deleg_flag.md)
  A flag that permits delegation of the initiator’s credentials by the acceptor.
- [var GSS_C_MUTUAL_FLAG: Int32](gss_c_mutual_flag.md)
  A flag that authenticates the credentials of both initiator and acceptor.
- [var GSS_C_REPLAY_FLAG: Int32](gss_c_replay_flag.md)
  A flag that detects repeated messages.
- [var GSS_C_SEQUENCE_FLAG: Int32](gss_c_sequence_flag.md)
  A flag that detects out of sequence messages.
- [var GSS_C_CONF_FLAG: Int32](gss_c_conf_flag.md)
  A flag that makes confidentiality services (that is, encryption) available for transferred messages.
- [var GSS_C_INTEG_FLAG: Int32](gss_c_integ_flag.md)
  A flag that makes integrity services (that is, cryptographic signatures) available for transferred messages.
- [var GSS_C_ANON_FLAG: Int32](gss_c_anon_flag.md)
  A flag that ensures the initiator remains anonymous to the acceptor.
- [var GSS_C_PROT_READY_FLAG: Int32](gss_c_prot_ready_flag.md)
  A flag that provides an early indication of the availability of confidentiality and integrity services.
- [var GSS_C_TRANS_FLAG: Int32](gss_c_trans_flag.md)
  A flag that indicates that a context can is exportable, for example to transfer it to another process on the same machine.
- [var GSS_C_DCE_STYLE: Int32](gss_c_dce_style.md)
  A flag that causes an extra AP reply to be sent from the client back to the server after receiving the server’s AP reply.
- [var GSS_C_IDENTIFY_FLAG: Int32](gss_c_identify_flag.md)
  A flag that indicates identification of the client by name and ID only.
- [var GSS_C_EXTENDED_ERROR_FLAG: Int32](gss_c_extended_error_flag.md)
  A flag that indicates that the client wants to be informed of extended error information.
- [var GSS_C_DELEG_POLICY_FLAG: Int32](gss_c_deleg_policy_flag.md)
  A flag that indicates delegation is permissible if the mechanism policy allows it.
### Address Families
- [var GSS_C_AF_NS: Int32](gss_c_af_ns.md)
  The Xerox NS address type.
- [var GSS_C_AF_BSC: Int32](gss_c_af_bsc.md)
  The BISYNC 2780/3780 address type.
- [var GSS_C_AF_DLI: Int32](gss_c_af_dli.md)
  The direct data link interface address type.
- [var GSS_C_AF_DSS: Int32](gss_c_af_dss.md)
  The distributed system services address type.
- [var GSS_C_AF_LAT: Int32](gss_c_af_lat.md)
  The LAT address type.
- [var GSS_C_AF_NBS: Int32](gss_c_af_nbs.md)
  The nbs address type.
- [var GSS_C_AF_OSI: Int32](gss_c_af_osi.md)
  The OSI TP4 address type.
- [var GSS_C_AF_PUP: Int32](gss_c_af_pup.md)
  The PUP protocols (for example, BSP) address type.
- [var GSS_C_AF_SNA: Int32](gss_c_af_sna.md)
  The IBM SNA address type.
- [var GSS_C_AF_X25: Int32](gss_c_af_x25.md)
  The X.25 address type.
- [var GSS_C_AF_ECMA: Int32](gss_c_af_ecma.md)
  The ECMA address type.
- [var GSS_C_AF_INET: Int32](gss_c_af_inet.md)
  The Internet (for example, IP) address type.
- [var GSS_C_AF_CCITT: Int32](gss_c_af_ccitt.md)
  The CCITT protocols address type.
- [var GSS_C_AF_CHAOS: Int32](gss_c_af_chaos.md)
  The MIT CHAOS protocol address type.
- [var GSS_C_AF_INET6: Int32](gss_c_af_inet6.md)
  The IPv6 address type.
- [var GSS_C_AF_LOCAL: Int32](gss_c_af_local.md)
  The host-local address type.
- [var GSS_C_AF_DECnet: Int32](gss_c_af_decnet.md)
  The DECnet address type.
- [var GSS_C_AF_HYLINK: Int32](gss_c_af_hylink.md)
  The NSC Hyperchannel address type.
- [var GSS_C_AF_UNSPEC: Int32](gss_c_af_unspec.md)
  The unspecified address type.
- [var GSS_C_AF_DATAKIT: Int32](gss_c_af_datakit.md)
  The datakit protocols address type.
- [var GSS_C_AF_IMPLINK: Int32](gss_c_af_implink.md)
  ARPAnet IMP address type.
- [var GSS_C_AF_NULLADDR: Int32](gss_c_af_nulladdr.md)
  No address specified.
- [var GSS_C_AF_APPLETALK: Int32](gss_c_af_appletalk.md)
  The AppleTalk address type.
### Apple Source App Keys
- [var kGSSICAppleSourceAppPID: String](kgssicapplesourceapppid.md)
  A number that indicates the process ID of the app.
- [var kGSSICAppleSourceAppAuditToken: String](kgssicapplesourceappaudittoken.md)
  The audit token of the app’s process.
- [var kGSSICAppleSourceAppSigningIdentity: String](kgssicapplesourceappsigningidentity.md)
  The bundle signing identity of the app.
### Channel Bindings
- [typealias gss_ctx_id_t](gss_ctx_id_t.md)
  A pointer to an opaque type that you use to communicate context pointers with GSS-API functions.
- [struct gss_channel_bindings_struct](gss_channel_bindings_struct.md)
  The structure defining a channel bindings descriptor that specifies the communications channel used to carry a context.
- [typealias gss_channel_bindings_t](gss_channel_bindings_t.md)
  A pointer to a channel bindings descriptor that specifies the communications channel used to carry a context.
- [typealias gss_const_channel_bindings_t](gss_const_channel_bindings_t.md)
  A pointer to an immutable channel bindings descriptor that you use to specify the communications channel used to carry a context.
### Creation and Deletion
- [func gss_init_sec_context(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t?, UnsafeMutablePointer<gss_ctx_id_t?>, gss_name_t, gss_OID?, OM_uint32, OM_uint32, gss_channel_bindings_t?, gss_buffer_t?, UnsafeMutablePointer<gss_OID?>?, gss_buffer_t, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<OM_uint32>?) -> OM_uint32](gss_init_sec_context(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Initiates a security context with a peer.
- [func gss_accept_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t?>, gss_cred_id_t?, gss_buffer_t?, gss_channel_bindings_t?, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<gss_OID?>?, gss_buffer_t, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<gss_cred_id_t?>?) -> OM_uint32](gss_accept_sec_context(_:_:_:_:_:_:_:_:_:_:_:).md)
  Accepts a security context initiated by a peer.
- [func gss_delete_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t?>, gss_buffer_t?) -> OM_uint32](gss_delete_sec_context(_:_:_:).md)
  Deletes a security context.
- [func gss_release_cred(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t?>) -> OM_uint32](gss_release_cred(_:_:).md)
  Releases the memory of a credential.
- [func gss_process_context_token(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t) -> OM_uint32](gss_process_context_token(_:_:_:).md)
  Processes a token from a peer asynchronously.
- [func gss_set_sec_context_option(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t>?, gss_OID, gss_buffer_t?) -> OM_uint32](gss_set_sec_context_option(_:_:_:_:).md)
  Sets an option on a context.
### Inquiry and Limits
- [func gss_context_time(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, UnsafeMutablePointer<OM_uint32>) -> OM_uint32](gss_context_time(_:_:_:).md)
  Returns the amount of time remaining before a context expires.
- [func gss_inquire_context(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<gss_name_t?>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<gss_OID?>?, UnsafeMutablePointer<OM_uint32>?, UnsafeMutablePointer<Int32>?, UnsafeMutablePointer<Int32>?) -> OM_uint32](gss_inquire_context(_:_:_:_:_:_:_:_:_:).md)
  Returns information about a security context.
- [func gss_inquire_sec_context_by_oid(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_OID, UnsafeMutablePointer<gss_buffer_set_t>?) -> OM_uint32](gss_inquire_sec_context_by_oid(_:_:_:_:).md)
  Returns information about a particular part of a context.
- [func gss_wrap_size_limit(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_qop_t, OM_uint32, UnsafeMutablePointer<OM_uint32>) -> OM_uint32](gss_wrap_size_limit(_:_:_:_:_:_:).md)
  Returns the largest allowable wrap size for a given set of constraints.
### Import and Export
- [func gss_export_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t?>, gss_buffer_t?) -> OM_uint32](gss_export_sec_context(_:_:_:).md)
  Transfers a security context to another process.
- [func gss_import_sec_context(UnsafeMutablePointer<OM_uint32>, gss_buffer_t, UnsafeMutablePointer<gss_ctx_id_t?>) -> OM_uint32](gss_import_sec_context(_:_:_:).md)
  Imports a security context from another process.

## See Also

- [Allocating and Releasing Objects](allocating-and-releasing-objects.md)
  Manage memory and object lifetimes.
- [Function Status](function-status.md)
  Evaluate return values that most GSS-API functions use to indicate the outcome of an operation.
- [Buffer Management](buffer-management.md)
  Allocate and deallocate buffers with structures that hold a variety of data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/context-services)*