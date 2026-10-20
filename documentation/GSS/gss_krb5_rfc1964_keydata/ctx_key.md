# ctx_key

**Framework**: GSS  
**Kind**: property  
**Role**: Instance Property

The context key (Kerberos session key or subkey).

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

### Key Data Members
- [var seal_alg: OM_uint32](./seal_alg.md)
  The seal/encrypt algorithm.
- [var sign_alg: OM_uint32](./sign_alg.md)
  The signing algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_krb5_rfc1964_keydata/ctx_key)*