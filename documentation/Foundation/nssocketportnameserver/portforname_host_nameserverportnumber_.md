# portForName:host:nameServerPortNumber:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Looks up and returns the port registered under the specified name on a specified host.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Apple discourages the use of this symbol.

## Declaration

```objc
- (NSPort *) portForName:(NSString *) name host:(NSString *) host nameServerPortNumber:(uint16_t) portNumber;
```

#### Return Value

The port associated with `portName` on the host `hostName`. Returns `nil` if no such port exists.

## Parameters

- `name`: The name of the desired port.
- `host`: The name of the host. `hostName` is an Internet domain name (for example, “`sales.anycorp.com`”) or IP address (IPv4 or IPv6). If `hostName` is `nil` or empty, the local host is checked. If `hostName` is `@”*”`, all hosts on the local network are checked.
- `portNumber`: The `portNumber` parameter is ignored.

## See Also

### Related Documentation
- [- registerPort:name:nameServerPortNumber:](./registerport_name_nameserverportnumber_.md)
  Registers a given port as a network service with the specified name in the local domain.
### Looking up Ports
- [- portForName:](./portforname_.md)
  Looks up and returns the port registered under the specified name on the local host.
- [- portForName:host:](./portforname_host_.md)
  Looks up and returns the port registered under the specified name on a specified host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssocketportnameserver/portforname:host:nameserverportnumber:)*