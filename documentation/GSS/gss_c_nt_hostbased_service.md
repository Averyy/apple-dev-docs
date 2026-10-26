# GSS_C_NT_HOSTBASED_SERVICE

**Framework**: GSS  
**Kind**: macro  
**Role**: Macro

A name used to specify services provided by host computers in the service/hostname format.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```c
#define GSS_C_NT_HOSTBASED_SERVICE
```

#### Discussion

The format of the name is `service@hostname`.

## See Also

### Name Types
- [GSS_C_NO_NAME](./gss_c_no_name.md)
  An empty name object.
- [GSS_C_NT_USER_NAME](./gss_c_nt_user_name.md)
  A name that specifies a user on a local system in the username format.
- [GSS_C_NT_MACHINE_UID_NAME](./gss_c_nt_machine_uid_name.md)
  A name used to specify a user on the local system by way of a numeric identifier.
- [GSS_C_NT_STRING_UID_NAME](./gss_c_nt_string_uid_name.md)
  A name that specifies a user on the local system by way of a string representation of a numeric identifier.
- [GSS_C_NT_HOSTBASED_SERVICE_X](./gss_c_nt_hostbased_service_x.md)
  A service that is related to a particular host.
- [GSS_C_NT_ANONYMOUS](./gss_c_nt_anonymous.md)
  A name that refers to an anonymous principal.
- [GSS_C_NT_EXPORT_NAME](./gss_c_nt_export_name.md)
  A name of the type exported by the export name function.
- [GSS_KRB5_NT_PRINCIPAL_NAME](./gss_krb5_nt_principal_name.md)
  A name composed as a single-string representation of a Kerberos name.
- [GSS_KRB5_NT_PRINCIPAL](./gss_krb5_nt_principal.md)
  A name composed as a single-string representation of a Kerberos name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_c_nt_hostbased_service)*