# registerPort:name:nameServerPortNumber:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Registers a given port as a network service with the specified name in the local domain.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Apple discourages the use of this symbol.

## Declaration

```objc
- (BOOL) registerPort:(NSPort *) port name:(NSString *) name nameServerPortNumber:(uint16_t) portNumber;
```

## Return Value

[`true`](../../Swift/true.md) if successful, [`false`](../../Swift/false.md) otherwise.

## Discussion

If your application has already registered a port under the name `portName`, this method replaces it with `port`.

If the local domain already has a port named `portName` registered, this method could return [`true`](../../Swift/true.md) before the name collision is detected. To detect a potential name collision, you can invoke [`portForName:host:`](./portforname_host_.md) with a `host` argument of `@"*"` to test if `portName` is already taken. This, however, leaves a race condition wherein another process can register a port under `portName` after [`portForName:host:`](./portforname_host_.md) returns but before you register `port`. If this is an unacceptable risk for your application, you can also invoke [`portForName:host:`](./portforname_host_.md) some finite time after registering your port to test if you get the same port back.

## Parameters

- `port`: The port to make available.
- `name`: The name for the port.
- `portNumber`: The `portNumber` parameter is ignored.

## See Also

### Related Documentation
- [- portForName:host:nameServerPortNumber:](./portforname_host_nameserverportnumber_.md)
  Looks up and returns the port registered under the specified name on a specified host.
### Registering and Removing Ports
- [- registerPort:name:](./registerport_name_.md)
  Registers a given port as a network service with the specified name in the local domain.
- [- removePortForName:](./removeportforname_.md)
  Unregisters the port for a given name on the local host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssocketportnameserver/registerport:name:nameserverportnumber:)*