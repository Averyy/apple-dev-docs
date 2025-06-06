# cssm_csp_operational_statistics

**Framework**: Security  
**Kind**: struct

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct cssm_csp_operational_statistics
```

## Topics

### Initializers
- [init()](cssm_csp_operational_statistics-swift.struct/init.md)
- [init(UserAuthenticated: CSSM_BOOL, DeviceFlags: CSSM_CSP_FLAGS, TokenMaxSessionCount: uint32, TokenOpenedSessionCount: uint32, TokenMaxRWSessionCount: uint32, TokenOpenedRWSessionCount: uint32, TokenTotalPublicMem: uint32, TokenFreePublicMem: uint32, TokenTotalPrivateMem: uint32, TokenFreePrivateMem: uint32)](cssm_csp_operational_statistics-swift.struct/init(userauthenticated:deviceflags:tokenmaxsessioncount:tokenopenedsessioncount:tokenmaxrwsessioncount:tokenopenedrwsessioncount:tokentotalpublicmem:tokenfreepublicmem:tokentotalprivatemem:tokenfreeprivatemem:).md)
### Instance Properties
- [var DeviceFlags: CSSM_CSP_FLAGS](cssm_csp_operational_statistics-swift.struct/deviceflags.md)
- [var TokenFreePrivateMem: uint32](cssm_csp_operational_statistics-swift.struct/tokenfreeprivatemem.md)
- [var TokenFreePublicMem: uint32](cssm_csp_operational_statistics-swift.struct/tokenfreepublicmem.md)
- [var TokenMaxRWSessionCount: uint32](cssm_csp_operational_statistics-swift.struct/tokenmaxrwsessioncount.md)
- [var TokenMaxSessionCount: uint32](cssm_csp_operational_statistics-swift.struct/tokenmaxsessioncount.md)
- [var TokenOpenedRWSessionCount: uint32](cssm_csp_operational_statistics-swift.struct/tokenopenedrwsessioncount.md)
- [var TokenOpenedSessionCount: uint32](cssm_csp_operational_statistics-swift.struct/tokenopenedsessioncount.md)
- [var TokenTotalPrivateMem: uint32](cssm_csp_operational_statistics-swift.struct/tokentotalprivatemem.md)
- [var TokenTotalPublicMem: uint32](cssm_csp_operational_statistics-swift.struct/tokentotalpublicmem.md)
- [var UserAuthenticated: CSSM_BOOL](cssm_csp_operational_statistics-swift.struct/userauthenticated.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_csp_operational_statistics-swift.struct)*