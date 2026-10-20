# ctx_key

**Framework**: GSS  
**Kind**: property  
**Role**: Instance Property

The Kerberos session context key.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var ctx_key: gss_krb5_lucid_key_t
```

```c
gss_krb5_lucid_key_t ctx_key;
```

## See Also

### Key Properties
- [var acceptor_subkey: gss_krb5_lucid_key_t](./acceptor_subkey.md)
  The Kerberos session acceptor subkey.
- [var have_acceptor_subkey: OM_uint32](./have_acceptor_subkey.md)
  The flag that indicates if the Kerberos session acceptor subkey is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_krb5_cfx_keydata/ctx_key)*