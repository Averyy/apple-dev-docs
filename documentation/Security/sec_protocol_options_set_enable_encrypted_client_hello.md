# sec_protocol_options_set_enable_encrypted_client_hello

**Framework**: Security  
**Kind**: func  
**Role**: Function

## Declaration

```c
void sec_protocol_options_set_enable_encrypted_client_hello(sec_protocol_options_t options, bool enable_encrypted_client_hello);
```

#### Discussion

For experimental use only. When this is enabled, the Encrypted Client Hello extension will be sent on the Client Hello if TLS 1.3 is among the supported TLS versions. Default false.

## Parameters

- `options`: A `sec_protocol_options_t` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_options_set_enable_encrypted_client_hello)*