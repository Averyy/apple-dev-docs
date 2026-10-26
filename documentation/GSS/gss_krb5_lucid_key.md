# gss_krb5_lucid_key

**Framework**: GSS  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
struct gss_krb5_lucid_key
```

```c
struct gss_krb5_lucid_key;
```

## Topics

### Initializers
- [init()](./gss_krb5_lucid_key/init%28%29.md)
- [init(type: OM_uint32, length: OM_uint32, data: UnsafeMutableRawPointer?)](./gss_krb5_lucid_key/init%28type,length,data%29.md)
### Instance Properties
- [var data: UnsafeMutableRawPointer?](./gss_krb5_lucid_key/data.md)
  The actual key data.
- [var length: OM_uint32](./gss_krb5_lucid_key/length.md)
  The length of the key data.
- [var type: OM_uint32](./gss_krb5_lucid_key/type.md)
  The key encryption type.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Structures
- [struct gss_krb5_cfx_keydata](./gss_krb5_cfx_keydata.md)
- [struct gss_krb5_lucid_context_v1](./gss_krb5_lucid_context_v1.md)
- [struct gss_krb5_lucid_context_version](./gss_krb5_lucid_context_version.md)
- [struct gss_krb5_rfc1964_keydata](./gss_krb5_rfc1964_keydata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_krb5_lucid_key)*