# sec_protocol_options_set_peer_authentication_optional

**Framework**: Security  
**Kind**: func  
**Role**: Function

## Declaration

```c
void sec_protocol_options_set_peer_authentication_optional(sec_protocol_options_t options, bool peer_authentication_optional);
```

#### Discussion

When this is enabled, the endpoint requests the peer certificate, but if none is provided, the endpoint still proceeds with the connection. Default false for servers; always false for clients (clients ignore this option). If peer_authentication_required is set to true via sec_protocol_options_set_peer_authentication_required(), peer_authentication_optional will be disregarded and the peer certificate will be required.

## Parameters

- `options`: A `sec_protocol_options_t` instance.
- `peer_authentication_optional`: Flag to enable or disable requested peer authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_options_set_peer_authentication_optional)*