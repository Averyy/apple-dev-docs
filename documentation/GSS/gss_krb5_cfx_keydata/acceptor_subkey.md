# acceptor_subkey

**Framework**: GSS  
**Kind**: property  
**Role**: Instance Property

The Kerberos session acceptor subkey.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var acceptor_subkey: gss_krb5_lucid_key_t
```

```c
gss_krb5_lucid_key_t acceptor_subkey;
```

## See Also

### Key Properties
- [var ctx_key: gss_krb5_lucid_key_t](./ctx_key.md)
  The Kerberos session context key.
- [var have_acceptor_subkey: OM_uint32](./have_acceptor_subkey.md)
  The flag that indicates if the Kerberos session acceptor subkey is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_krb5_cfx_keydata/acceptor_subkey)*