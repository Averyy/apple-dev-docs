# registerPort:name:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Registers a given port as a network service with the specified name in the local domain.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Apple discourages the use of this symbol.

## Declaration

```objc
- (BOOL) registerPort:(NSPort *) port name:(NSString *) name;
```

#### Return Value

[`true`](../../Swift/true.md) if successful, [`false`](../../Swift/false.md) otherwise.

#### Discussion

Invokes [`registerPort:name:nameServerPortNumber:`](./registerport_name_nameserverportnumber_.md) with 0 as the name server port number.

## Parameters

- `port`: The port to make available.
- `name`: The name for the port.

## See Also

### Registering and Removing Ports
- [- registerPort:name:nameServerPortNumber:](./registerport_name_nameserverportnumber_.md)
  Registers a given port as a network service with the specified name in the local domain.
- [- removePortForName:](./removeportforname_.md)
  Unregisters the port for a given name on the local host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssocketportnameserver/registerport:name:)*