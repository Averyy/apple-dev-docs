# CSSM_APPLE_TP_SMIME_OPTIONS

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct CSSM_APPLE_TP_SMIME_OPTIONS
```

```c
typedef struct { ... } CSSM_APPLE_TP_SMIME_OPTIONS;
```

## Topics

### Initializers
- [init()](./cssm_apple_tp_smime_options/init%28%29.md)
- [init(Version: uint32, IntendedUsage: uint16, SenderEmailLen: uint32, SenderEmail: UnsafePointer<CChar>!)](./cssm_apple_tp_smime_options/init%28version,intendedusage,senderemaillen,senderemail%29.md)
### Instance Properties
- [var IntendedUsage: uint16](./cssm_apple_tp_smime_options/intendedusage.md)
- [var SenderEmail: UnsafePointer<CChar>!](./cssm_apple_tp_smime_options/senderemail.md)
- [var SenderEmailLen: uint32](./cssm_apple_tp_smime_options/senderemaillen.md)
- [var Version: uint32](./cssm_apple_tp_smime_options/version.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_apple_tp_smime_options)*