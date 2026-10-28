# Security Mechanisms

**Framework**: GSS  
**Role**: API Collection

Provide a security mechanism for your implementation.

## Overview

For more information on the attributes of a mechanism, see [RFC 5587](https://tools.ietf.org/html/rfc5587).

## Topics

### Queries
- [func gss_indicate_mechs(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](./gss_indicate_mechs%28_,_%29.md)
  Returns the list of supported underlying security mechanisms.
- [func gss_indicate_mechs_by_attrs(UnsafeMutablePointer<OM_uint32>, gss_const_OID_set?, gss_const_OID_set?, gss_const_OID_set?, UnsafeMutablePointer<gss_OID_set?>) -> OM_uint32](./gss_indicate_mechs_by_attrs%28_,_,_,_,_%29.md)
  Returns the set of mechanisms that fulfill the given criteria.
- [func gss_display_mech_attr(UnsafeMutablePointer<OM_uint32>, gss_const_OID, gss_buffer_t?, gss_buffer_t?, gss_buffer_t?) -> OM_uint32](./gss_display_mech_attr%28_,_,_,_,_%29.md)
  Returns a human-readable name and description of a mechanism attribute.
- [func gss_inquire_attrs_for_mech(UnsafeMutablePointer<OM_uint32>, gss_const_OID, UnsafeMutablePointer<gss_OID_set?>?, UnsafeMutablePointer<gss_OID_set?>?) -> OM_uint32](./gss_inquire_attrs_for_mech%28_,_,_,_%29.md)
  Returns the supported attributes for one or all mechanisms.
- [func gss_inquire_mech_for_saslname(UnsafeMutablePointer<OM_uint32>, gss_buffer_t?, UnsafeMutablePointer<gss_OID?>) -> OM_uint32](./gss_inquire_mech_for_saslname%28_,_,_%29.md)
  Returns the GSS-API mechanism identifier for a given Simple Authentication and Security Layer (SASL) protocol name.
- [func gss_inquire_saslname_for_mech(UnsafeMutablePointer<OM_uint32>, gss_OID, gss_buffer_t?, gss_buffer_t?, gss_buffer_t?) -> OM_uint32](./gss_inquire_saslname_for_mech%28_,_,_,_,_%29.md)
  Returns the Simple Authentication and Security Layer (SASL) protocol name for a given GSS-API mechanism.
### Standard Mechanisms
- [GSS_KRB5_MECHANISM](./gss_krb5_mechanism.md)
  The Kerberos Version 5 Mechanism (KRB5).
- [GSS_NTLM_MECHANISM](./gss_ntlm_mechanism.md)
  The Microsoft NT LAN Manager Mechanism (NTLM).
- [GSS_IAKERB_MECHANISM](./gss_iakerb_mechanism.md)
  The Initial and Pass Through Authentication Using Kerberos V5 and the GSS-API Mechanism (IAKERB).
- [GSS_PKU2U_MECHANISM](./gss_pku2u_mechanism.md)
  The Public Key Cryptography Based User-to-User Mechanism (PKU2U).
- [GSS_SPNEGO_MECHANISM](./gss_spnego_mechanism.md)
  The Simple and Protected GSSAPI Negotiation Mechanism (SPNEGO).
- [GSS_SCRAM_MECHANISM](./gss_scram_mechanism.md)
  The Salted Challenge Response Authentication Mechanism (SCRAM).
### Heimdal Mechanisms
- [GSS_SASL_DIGEST_MD5_MECHANISM](./gss_sasl_digest_md5_mechanism.md)
  The Simple Authentication and Security Layer (SASL) Mechanism with Digest-MD5.
- [GSS_NETLOGON_MECHANISM](./gss_netlogon_mechanism.md)
  The Microsoft Net Logon Mechanism.
- [GSS_APPL_LKDC_SUPPORTED](./gss_appl_lkdc_supported.md)
  Local KDC is supported.
### Netlogon Set
- [GSS_NETLOGON_SET_SESSION_KEY_X](./gss_netlogon_set_session_key_x.md)
  The Netlogon set session key value.
- [GSS_NETLOGON_SET_SIGN_ALGORITHM_X](./gss_netlogon_set_sign_algorithm_x.md)
  The Netlogon algorithm key value.
- [GSS_NETLOGON_NT_NETBIOS_DNS_NAME](./gss_netlogon_nt_netbios_dns_name.md)
  The Netlogon NetBIOS DNS name value.
### Mechanisms and Authentication
- [GSS_C_MA_MECH_CONCRETE](./gss_c_ma_mech_concrete.md)
  A mechanism that is neither a psuedo-mechanism nor a composite mechanism.
- [GSS_C_MA_MECH_PSEUDO](./gss_c_ma_mech_pseudo.md)
  A pseudo-mechanism.
- [GSS_C_MA_MECH_COMPOSITE](./gss_c_ma_mech_composite.md)
  A mechanism that is a composite of other mechanisms.
- [GSS_C_MA_MECH_NEGO](./gss_c_ma_mech_nego.md)
  A mechanism that negotiates other mechanisms.
- [GSS_C_MA_MECH_GLUE](./gss_c_ma_mech_glue.md)
  An OID that is for the GSS-API rather than for a mechanism.
- [GSS_C_MA_NOT_MECH](./gss_c_ma_not_mech.md)
  A known OID that is neither a GSS-API mechanism nor an identifier of the GSS-API itself.
- [GSS_C_MA_DEPRECATED](./gss_c_ma_deprecated.md)
  A mechanism that is no longer used.
- [GSS_C_MA_NOT_DFLT_MECH](./gss_c_ma_not_dflt_mech.md)
  A mechanism that is not suitable for use as a default mechanism.
- [GSS_C_MA_ITOK_FRAMED](./gss_c_ma_itok_framed.md)
  The given mechanism’s initial context tokens are properly framed.
- [GSS_C_MA_AUTH_INIT](./gss_c_ma_auth_init.md)
  Support for authentication of initiator to acceptor.
- [GSS_C_MA_AUTH_TARG](./gss_c_ma_auth_targ.md)
  Support for authentication of acceptor to initiator.
- [GSS_C_MA_AUTH_INIT_INIT](./gss_c_ma_auth_init_init.md)
  Support for initial authentication of initiator to acceptor.
- [GSS_C_MA_AUTH_TARG_INIT](./gss_c_ma_auth_targ_init.md)
  Support for initial authentication of acceptor to initiator.
- [GSS_C_MA_AUTH_INIT_ANON](./gss_c_ma_auth_init_anon.md)
  Anonymous support as a target principal name.
- [GSS_C_MA_AUTH_TARG_ANON](./gss_c_ma_auth_targ_anon.md)
  Anonymous support as a target principal name.
- [GSS_C_MA_DELEG_CRED](./gss_c_ma_deleg_cred.md)
  Support for credential delegation.
- [GSS_C_MA_INTEG_PROT](./gss_c_ma_integ_prot.md)
  Support for per-message integrity protection.
- [GSS_C_MA_CONF_PROT](./gss_c_ma_conf_prot.md)
  Support for per-message confidentiality protection.
- [GSS_C_MA_MIC](./gss_c_ma_mic.md)
  Support for Message Integrity Code (MIC) tokens.
- [GSS_C_MA_WRAP](./gss_c_ma_wrap.md)
  Support for WRAP tokens.
- [GSS_C_MA_PROT_READY](./gss_c_ma_prot_ready.md)
  Support for per-message protection prior to full context establishment.
- [GSS_C_MA_REPLAY_DET](./gss_c_ma_replay_det.md)
  Support for replay detection.
- [GSS_C_MA_OOS_DET](./gss_c_ma_oos_det.md)
  Support for out-of-sequence detection.
- [GSS_C_MA_CBINDINGS](./gss_c_ma_cbindings.md)
  Support for channel bindings.
- [GSS_C_MA_PFS](./gss_c_ma_pfs.md)
  Support for perfect forward security.
- [GSS_C_MA_COMPRESS](./gss_c_ma_compress.md)
  Support for compression of data inputs to the wrap function.
- [GSS_C_MA_CTX_TRANS](./gss_c_ma_ctx_trans.md)
  Support for security context importing and exporting.
- [GSS_C_MA_SASL_MECH_NAME](./gss_c_ma_sasl_mech_name.md)
  The name of the SASL mechanism.
- [GSS_C_MA_MECH_NAME](./gss_c_ma_mech_name.md)
  The name of the GSS-API mechanism.
- [GSS_C_MA_MECH_DESCRIPTION](./gss_c_ma_mech_description.md)
  The long description of the mechanism.

## See Also

### Credentials
- [Credential Management](./credential-management.md)
  Securely establish connections between endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/security-mechanisms)*