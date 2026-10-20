# CSSM_APPLE_TP_CRL_OPTIONS

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct CSSM_APPLE_TP_CRL_OPTIONS
```

```c
typedef struct { ... } CSSM_APPLE_TP_CRL_OPTIONS;
```

## Topics

### Initializers
- [init()](./cssm_apple_tp_crl_options/init%28%29.md)
- [init(Version: uint32, CrlFlags: CSSM_APPLE_TP_CRL_OPT_FLAGS, crlStore: UnsafeMutablePointer<cssm_dl_db_handle>!)](./cssm_apple_tp_crl_options/init%28version,crlflags,crlstore%29.md)
### Instance Properties
- [var CrlFlags: CSSM_APPLE_TP_CRL_OPT_FLAGS](./cssm_apple_tp_crl_options/crlflags.md)
- [var Version: uint32](./cssm_apple_tp_crl_options/version.md)
- [var crlStore: UnsafeMutablePointer<cssm_dl_db_handle>!](./cssm_apple_tp_crl_options/crlstore.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_apple_tp_crl_options)*