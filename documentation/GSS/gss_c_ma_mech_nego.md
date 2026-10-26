# GSS_C_MA_MECH_NEGO

**Framework**: GSS  
**Kind**: macro  
**Role**: Macro

A mechanism that negotiates other mechanisms.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```c
#define GSS_C_MA_MECH_NEGO
```

## See Also

### Mechanisms and Authentication
- [GSS_C_MA_MECH_CONCRETE](./gss_c_ma_mech_concrete.md)
  A mechanism that is neither a psuedo-mechanism nor a composite mechanism.
- [GSS_C_MA_MECH_PSEUDO](./gss_c_ma_mech_pseudo.md)
  A pseudo-mechanism.
- [GSS_C_MA_MECH_COMPOSITE](./gss_c_ma_mech_composite.md)
  A mechanism that is a composite of other mechanisms.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_c_ma_mech_nego)*