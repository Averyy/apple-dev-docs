# CSSM_APPLE_TP_SSL_OPTIONS

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct CSSM_APPLE_TP_SSL_OPTIONS
```

```c
typedef struct { ... } CSSM_APPLE_TP_SSL_OPTIONS;
```

## Topics

### Initializers
- [init()](./cssm_apple_tp_ssl_options/init%28%29.md)
- [init(Version: uint32, ServerNameLen: uint32, ServerName: UnsafePointer<CChar>!, Flags: uint32)](./cssm_apple_tp_ssl_options/init%28version,servernamelen,servername,flags%29.md)
### Instance Properties
- [var Flags: uint32](./cssm_apple_tp_ssl_options/flags.md)
- [var ServerName: UnsafePointer<CChar>!](./cssm_apple_tp_ssl_options/servername.md)
- [var ServerNameLen: uint32](./cssm_apple_tp_ssl_options/servernamelen.md)
- [var Version: uint32](./cssm_apple_tp_ssl_options/version.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_apple_tp_ssl_options)*